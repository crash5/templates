from pathlib import Path

import polars as pl
from polars.testing import assert_frame_equal


SCRIPT_DIR = Path(__file__).parent


def test_one(tmp_path):
    input_path = SCRIPT_DIR / "e2e/input"
    expected_result_path = SCRIPT_DIR / "e2e/expected"

    output_path = tmp_path / "e2e"
    output_path.mkdir()

    # TODO: add test scenario
