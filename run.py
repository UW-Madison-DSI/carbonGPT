from pathlib import Path

import nest_asyncio
from dotenv import load_dotenv
from openai import OpenAI

from carbongpt.data_model import Paper

load_dotenv()
nest_asyncio.apply()


def extract(text: str) -> Paper:
    """Extract Paper structure from text."""

    client = OpenAI()
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "Extract research paper information. Get all topsoil (< 20 cm deep) organic carbon (TOC) measurements in the units of mass fractions/concentrations (e.g., g/kg, mg/g, mg/ha...) from the paper. Also, extract changes in TOC over time due to land cover and land use change or long-term treatments if they are available.",
            },
            {"role": "user", "content": text},
        ],
        response_format=Paper,
        temperature=0.0,
    )

    if completion.choices[0].message.parsed is None:
        raise ValueError("Failed to extract paper structure.")
    return completion.choices[0].message.parsed


def main():
    # pdf_files = Path("data/pdfs/").glob("*.pdf")
    # for pdf in pdf_files:
    #     pdf2md(pdf, Path(f"data/markdowns/{pdf.stem}.md"))

    markdown_files = list(Path("data/markdowns/").glob("*.md"))
    for markdown in markdown_files:
        extracted = extract(markdown.read_text())
        extracted.save(Path("data/extracted") / f"{markdown.stem}.json")


if __name__ == "__main__":
    main()
