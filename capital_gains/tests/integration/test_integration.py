import glob
import io
import json
import os
import sys
import unittest
from unittest import TestCase
from unittest.mock import patch

from src.infra.cli import run

# Path raiz do projeto
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, ROOT)


class IntegrationTestCase(TestCase):
    """Dynamic integration tests generated from JSON files in directory .cases"""

    def run_case(self, case_path):
        # Load the case JSON
        with open(case_path, "r") as f:
            case = json.load(f)

        input_data = case["input"]
        expected_output = case["expected"]

        fake_stdin = io.StringIO(json.dumps(input_data))
        fake_stdout = io.StringIO()

        with patch("sys.stdin", fake_stdin):
            with patch("sys.stdout", fake_stdout):
                run()  # run the CLI

        # Read printed output
        output_raw = fake_stdout.getvalue().strip()
        try:
            output_json = json.loads(output_raw)
        except json.JSONDecodeError:
            raise AssertionError(
                f"Output is not valid JSON.\nRaw output:\n{output_raw}"
            )

        # Validate expected vs output
        self.assertEqual(
            output_json,
            expected_output,
            msg=f"\nMismatch in case: {case_path}\nExpected: {expected_output}\nGot: {output_json}"
        )

    def test_all_cases(self):
        case_files = sorted(glob.glob("tests/integration/cases/*.json"))
        self.assertGreater(len(case_files), 0, "No integration cases found!")

        for case_path in case_files:
            with self.subTest(case=case_path):
                self.run_case(case_path)


if __name__ == "__main__":
    unittest.main()
