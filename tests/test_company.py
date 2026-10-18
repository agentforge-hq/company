from __future__ import annotations

import copy
import datetime as dt
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import company


class CompanyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.config = copy.deepcopy(company.config_for(company.ROOT))
        paths = set(self.config['common_context'])
        for profile in self.config['roles'].values():
            paths.update(profile['context'])
            paths.add(profile['mandate'])
        for relative in paths:
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            owner = path.parts[-2] if path.parts[-2] in self.config['roles'] else 'founder'
            path.write_text(self.document(owner))
        (self.root / 'evidence/claims.json').write_text(json.dumps({'claims': [{'id': 'C-001'}]}))
        (self.root / '.company/work-items.json').write_text(
            json.dumps({'items': [{'id': 'AF-001', 'owner': 'product', 'depends_on': [], 'status': 'planned'}]})
        )
        (self.root / '.company/config.json').write_text(json.dumps(self.config))
        self.package = company.brief(self.root, 'product', 'Review one milestone', self.config)

    def document(self, owner: str) -> str:
        return (
            f'---\nowner: {owner}\nstatus: draft\nreviewed: 2026-10-18\n'
            'review_after: 2026-10-25\n---\nVerify one useful outcome.\n'
        )

    def proposal(self) -> dict:
        document = next(d for d in self.package['documents'] if d['path'] == 'product/roadmap.md')
        return {
            'summary': 'Refine the milestone',
            'changes': [
                {
                    'path': document['path'],
                    'original_sha256': document['sha256'],
                    'content': document['content'].replace(
                        'Verify one useful outcome.', 'Verify one accepted outcome.'
                    ),
                    'reason': 'Clarify the observable criterion',
                    'evidence': ['C-001'],
                }
            ],
            'handoffs': [],
            'uncertainties': [],
        }

    def test_brief_is_scoped_and_offline(self) -> None:
        paths = {d['path'] for d in self.package['documents']}
        self.assertIn('product/README.md', paths)
        self.assertNotIn('marketing/README.md', paths)
        self.assertFalse(self.package['network_used'])
        self.assertLess(self.package['input_bytes'], self.config['runtime']['max_input_bytes'])

    def test_unknown_role_and_oversized_task_rejected(self) -> None:
        for role, task in [('founder', 'Rewrite the vision'), ('product', 'x' * 2001)]:
            with self.assertRaises(ValueError):
                company.brief(self.root, role, task, self.config)

    def test_context_budget_enforced(self) -> None:
        self.config['runtime']['max_input_bytes'] = 10
        with self.assertRaises(ValueError):
            company.brief(self.root, 'product', 'Task', self.config)

    def test_traversal_and_symlinks_rejected(self) -> None:
        for relative in ('../secret', '/tmp/secret', 'product/../../secret'):
            with self.assertRaises(ValueError):
                company.safe_path(self.root, relative)
        (self.root / 'product/link.md').symlink_to('/etc/passwd')
        with self.assertRaises(ValueError):
            company.safe_path(self.root, 'product/link.md')

    def test_status_reports_due_documents_without_writing(self) -> None:
        before = (self.root / 'vision.md').read_bytes()
        result = company.status(self.root, dt.date(2026, 11, 1))
        self.assertIn('vision.md', result['review_due'])
        self.assertEqual(before, (self.root / 'vision.md').read_bytes())
        self.assertFalse(result['errors'])

    def test_status_detects_bad_metadata_and_link(self) -> None:
        (self.root / 'bad.md').write_text('No owner')
        (self.root / 'product/roadmap.md').write_text(self.document('product') + '[Missing](absent.md)')
        result = company.status(self.root, dt.date(2026, 10, 18))
        self.assertEqual(len(result['errors']), 2)

    def test_live_disabled_before_network(self) -> None:
        with patch.object(company.urllib.request, 'build_opener') as opener:
            with self.assertRaises(ValueError):
                company.request_xai(self.package, self.config)
        opener.assert_not_called()

    def test_live_requires_approved_exact_context(self) -> None:
        self.config['runtime'].update(enabled=True, approved_monthly_usd=10)
        with patch.object(company.urllib.request, 'build_opener') as opener:
            with self.assertRaises(ValueError):
                company.request_xai(self.package, self.config)
        opener.assert_not_called()

    def test_live_requires_environment_key_and_model(self) -> None:
        self.config['runtime'].update(
            enabled=True, approved_monthly_usd=10, approved_context_paths=[d['path'] for d in self.package['documents']]
        )
        with patch.dict(os.environ, {}, clear=True), self.assertRaises(ValueError):
            company.request_xai(self.package, self.config)

    def test_one_request_without_tools_or_storage(self) -> None:
        self.config['runtime'].update(
            enabled=True, approved_monthly_usd=10, approved_context_paths=[d['path'] for d in self.package['documents']]
        )
        response = {'status': 'completed', 'output': []}
        with patch.dict(os.environ, {'XAI_API_KEY': 'test-only-key', 'XAI_MODEL': 'configured-model'}):
            with patch.object(company.urllib.request, 'build_opener') as opener:
                stream = opener.return_value.open.return_value.__enter__.return_value
                stream.read.return_value = json.dumps(response).encode()
                self.assertEqual(company.request_xai(self.package, self.config), response)
                request = opener.return_value.open.call_args.args[0]
                payload = json.loads(request.data)
                self.assertFalse(payload['store'])
                self.assertNotIn('tools', payload)
                self.assertEqual(payload['max_output_tokens'], 2000)
                self.assertEqual(opener.return_value.open.call_count, 1)

    def test_extracts_rest_response(self) -> None:
        proposal = self.proposal()
        response = {
            'status': 'completed',
            'output': [{'type': 'message', 'content': [{'type': 'output_text', 'text': json.dumps(proposal)}]}],
        }
        self.assertEqual(company.extract_proposal(response), proposal)

    def test_rejects_incomplete_response(self) -> None:
        with self.assertRaises(ValueError):
            company.extract_proposal({'status': 'incomplete', 'output': []})

    def test_valid_proposal_renders_diff_without_editing(self) -> None:
        before = (self.root / 'product/roadmap.md').read_bytes()
        diff = company.validate_proposal(self.root, self.package, self.proposal(), self.config)
        self.assertIn('--- a/product/roadmap.md', diff)
        self.assertIn('+Verify one accepted outcome.', diff)
        self.assertEqual(before, (self.root / 'product/roadmap.md').read_bytes())

    def test_cross_role_and_vision_changes_rejected(self) -> None:
        for relative in ('marketing/README.md', 'vision.md', '.github/workflows/checks.yml'):
            proposal = self.proposal()
            proposal['changes'][0]['path'] = relative
            with self.assertRaises(ValueError):
                company.validate_proposal(self.root, self.package, proposal, self.config)

    def test_stale_change_and_fabricated_evidence_rejected(self) -> None:
        for field, value in [('original_sha256', '0' * 64), ('evidence', ['fabricated-source'])]:
            proposal = self.proposal()
            proposal['changes'][0][field] = value
            with self.assertRaises(ValueError):
                company.validate_proposal(self.root, self.package, proposal, self.config)

    def test_owner_cannot_be_escalated(self) -> None:
        proposal = self.proposal()
        proposal['changes'][0]['content'] = self.document('founder')
        with self.assertRaises(ValueError):
            company.validate_proposal(self.root, self.package, proposal, self.config)

    def test_changed_context_is_rejected_even_with_a_new_fingerprint(self) -> None:
        import hashlib

        proposal = self.proposal()
        path = self.root / 'product/roadmap.md'
        path.write_text(path.read_text() + '\nChanged after the brief.\n')
        proposal['changes'][0]['original_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
        with self.assertRaises(ValueError):
            company.validate_proposal(self.root, self.package, proposal, self.config)

    def test_serialized_request_budget_rejected_before_network(self) -> None:
        self.config['runtime'].update(
            enabled=True,
            approved_monthly_usd=10,
            max_input_bytes=1,
            approved_context_paths=[d['path'] for d in self.package['documents']],
        )
        with patch.dict(os.environ, {'XAI_API_KEY': 'test-only-key', 'XAI_MODEL': 'configured-model'}):
            with patch.object(company.urllib.request, 'build_opener') as opener:
                with self.assertRaises(ValueError):
                    company.request_xai(self.package, self.config)
        opener.assert_not_called()

    def test_change_count_and_proposal_byte_limits(self) -> None:
        proposal = self.proposal()
        proposal['changes'] *= 4
        with self.assertRaises(ValueError):
            company.validate_proposal(self.root, self.package, proposal, self.config)
        self.config['runtime']['max_proposal_bytes'] = 10
        with self.assertRaises(ValueError):
            company.validate_proposal(self.root, self.package, self.proposal(), self.config)

    def test_handoff_is_a_bounded_request_to_another_role(self) -> None:
        proposal = self.proposal()
        proposal['handoffs'] = [{'role': 'engineering', 'task': 'Verify one acceptance test', 'evidence': ['C-001']}]
        company.validate_proposal(self.root, self.package, proposal, self.config)
        proposal['handoffs'][0]['role'] = 'product'
        with self.assertRaises(ValueError):
            company.validate_proposal(self.root, self.package, proposal, self.config)

    def test_saved_run_contains_review_artifacts_not_input_bodies(self) -> None:
        proposal = self.proposal()
        diff = company.validate_proposal(self.root, self.package, proposal, self.config)
        run = company.save_run(self.root, self.package, proposal, diff, {'id': 'response-id'}, False)
        value = json.loads((run / 'proposal.json').read_text())
        self.assertEqual(value['status'], 'needs-human-review')
        self.assertFalse(value['canonical_documents_changed'])
        self.assertNotIn('documents', value)
        self.assertTrue((run / 'proposal.diff').exists())


if __name__ == '__main__':
    unittest.main()
