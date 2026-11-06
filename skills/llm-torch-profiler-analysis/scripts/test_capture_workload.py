"""Regression coverage for capture metadata versus live workload defaults."""

import contextlib
import io
import json
import unittest

from analyze_llm_torch_profile import build_triage_parser, stage_workload_note


class CaptureWorkloadTest(unittest.TestCase):
    def test_capture_metadata_applies_to_every_stage(self):
        workload = {"input_tokens": 1536, "output_tokens": 96, "requests": 24, "concurrency": 6}
        args = build_triage_parser().parse_args([
            "--input", "trace.json", "--capture-workload-json", json.dumps(workload)
        ])
        for stage in ("extend", "prefill", "decode", "all", "unknown"):
            note = stage_workload_note(stage, args)
            self.assertIn("input_len=1536, output_len=96, requests=24, concurrency=6", note)
            self.assertIn("not per-stage tensor shapes", note)
            self.assertNotIn("4090", note)
            self.assertNotIn("2048", note)

    def test_existing_trace_without_metadata_does_not_use_live_defaults(self):
        for source in (["--input", "trace.json"], ["--mapping-input", "mapping.json", "--formal-input", "formal.json"]):
            args = build_triage_parser().parse_args(source)
            for stage in ("extend", "decode", "all"):
                note = stage_workload_note(stage, args)
                self.assertIn("unknown", note)
                self.assertIn("defaults are not trace evidence", note)
                self.assertNotIn("4090", note)
                self.assertNotIn("2048", note)

    def test_live_capture_preserves_configured_lengths(self):
        args = build_triage_parser().parse_args([
            "--url", "http://localhost:30000", "--prefill-input-len", "777",
            "--prefill-output-len", "2", "--decode-input-len", "3", "--decode-output-len", "55"
        ])
        self.assertEqual(stage_workload_note("extend", args), "input_len=777, output_len=2")
        self.assertEqual(stage_workload_note("decode", args), "input_len=3, output_len=55")

    def test_bad_capture_metadata_is_rejected(self):
        cases = ["invalid", "[]", "{}"]
        base = {"input_tokens": 1536, "output_tokens": 96, "requests": 24, "concurrency": 6}
        for key in base:
            for value in (0, -1, True, "6", 1.5, None):
                cases.append(json.dumps({**base, key: value}))
        for value in cases:
            with self.subTest(value=value), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit):
                    build_triage_parser().parse_args(["--capture-workload-json", value])


if __name__ == "__main__":
    unittest.main()
