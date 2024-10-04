from enum import StrEnum, auto

from pydantic import BaseModel


class Group(StrEnum):
    TREATMENT = auto()
    CONTROL = auto()


class SoilOrganicCarbonMeasurement(BaseModel):
    group: Group
    group_details: str
    measurement_name: str
    measurement_year: str
    measurement_month: str
    measurement_depth: str
    soil_organic_carbon_gram_per_kg: float
    details: str


class Site(BaseModel):
    name: str
    location: str
    latitude: float
    longitude: float
    measurements: list[SoilOrganicCarbonMeasurement]


class Paper(BaseModel):
    title: str
    authors: str
    year: int
    doi: str
    sites: list[Site]
