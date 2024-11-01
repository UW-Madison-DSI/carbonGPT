from pathlib import Path

from llama_parse import LlamaParse, ResultType


def pdf2md(pdf: Path, save_path: Path) -> str:
    """Convert a PDF to a markdown string"""

    parser = LlamaParse(result_type=ResultType.MD)
    document = parser.load_data(str(pdf))

    md = "\n".join([doc.text for doc in document])
    with open(save_path, "w") as f:
        f.write(md)
    return md
