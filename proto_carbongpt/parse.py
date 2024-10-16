from pathlib import Path

from llama_parse import LlamaParse


def pdf2md(pdf: Path) -> str:
    """Convert a PDF to a markdown string"""

    parser = LlamaParse(result_type="markdown")  # type: ignore
    document = parser.load_data(pdf)  # type: ignore

    md = "\n".join([doc.text for doc in document])
    with open(f"data/markdowns/{pdf.stem}.md", "w") as f:
        f.write(md)
    return md
