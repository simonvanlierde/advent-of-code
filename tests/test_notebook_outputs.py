"""Guard against committing puzzle inputs through notebook cell outputs."""

import json
from pathlib import Path

import pytest

NOTEBOOKS = sorted((Path(__file__).parents[1] / "notebooks").rglob("*.ipynb"))

# Answers, timings and small example traces stay under this; a printed input grid does not.
MAX_OUTPUT_LINES = 30


def _output_text(output: dict) -> str:
    text = output.get("text") or output.get("data", {}).get("text/plain", "")
    return "".join(text)


@pytest.mark.parametrize("notebook", NOTEBOOKS, ids=lambda p: str(p.relative_to(p.parents[1])))
def test_no_long_text_outputs(notebook: Path) -> None:
    cells = json.loads(notebook.read_text(encoding="utf-8"))["cells"]
    long_cells = [
        index
        for index, cell in enumerate(cells)
        for output in cell.get("outputs", [])
        if len(_output_text(output).splitlines()) > MAX_OUTPUT_LINES
    ]
    assert not long_cells, f"cells {long_cells} print more than {MAX_OUTPUT_LINES} lines; clear them before committing"
