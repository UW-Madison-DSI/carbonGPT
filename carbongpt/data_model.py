from enum import StrEnum, auto
from pathlib import Path

from pydantic import BaseModel


class Group(StrEnum):
    TREATMENT = auto()
    CONTROL = auto()


class TopSoilOrganicCarbon(BaseModel):
    """Topsoil organic carbon weight measurements."""

    measurement_value: float
    measurement_name: str
    measurement_year: str
    measurement_depth: str
    measurement_unit: str
    group: Group


class TopSoilOrganicCarbonChange(BaseModel):
    """Change in topsoil organic carbon weight measurements."""

    measurement_change_value: float
    measurement_relative_to: str
    measurement_name: str
    measurement_year: str
    measurement_depth: str
    measurement_unit: str


class Location(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
    measurements: list[TopSoilOrganicCarbon | TopSoilOrganicCarbonChange]


class Paper(BaseModel):
    title: str
    authors: str
    year: int
    doi: str
    locations: list[Location]

    def save(self, path: Path) -> None:
        with open(path, "w") as f:
            f.write(self.model_dump_json(indent=2))
