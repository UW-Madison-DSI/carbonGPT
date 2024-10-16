from enum import StrEnum, auto

from pydantic import BaseModel


class Group(StrEnum):
    TREATMENT = auto()
    CONTROL = auto()


class TopSoilOrganicCarbon(BaseModel):
    """Top soil organic carbon measurement in weights."""

    value: float
    measurement: str
    measurement_year: str
    measurement_depth: str
    measurement_unit: str
    group: Group


class TopSoilOrganicCarbonChange(BaseModel):
    change: float
    measurement: str
    measurement_year: str
    measurement_depth: str
    measurement_unit: str


class Location(BaseModel):
    name: str
    location: str
    latitude: float
    longitude: float
    measurements: list[TopSoilOrganicCarbon | TopSoilOrganicCarbonChange]


class Paper(BaseModel):
    title: str
    authors: str
    year: int
    doi: str
    locations: list[Location]
