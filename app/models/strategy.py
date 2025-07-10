from enum import Enum
from pydantic import BaseModel, Field, model_validator, ConfigDict
from typing import List

class AssetCategory(str, Enum):
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    ENERGY = "Energy"
    FINANCE = "Finance"

class Asset(BaseModel):
    category: AssetCategory
    weight: float = Field(..., ge=0, le=100)

    @model_validator(mode="before")
    @classmethod
    def map_category_alias(cls, values):
        alias_map = {
            "tech": "Technology",
            "health": "Healthcare",
            "energy": "Energy",
            "finance": "Finance"
        }
        if isinstance(values, dict) and "category" in values:
            values["category"] = alias_map.get(values["category"], values["category"])
        return values

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "category": "Technology",
                "weight": 50.0
            }
        }
    )

class StrategyRequest(BaseModel):
    name: str
    assets: List[Asset]

    @model_validator(mode="after")
    def validate_total_weight(cls, values):
        total_weight = sum(a.weight for a in values.assets)
        if total_weight != 100:
            raise ValueError(f"Total weight must be 100, got {total_weight}")
        return values

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Growth Portfolio",
                "assets": [
                    {"category": "Technology", "weight": 50.0},
                    {"category": "Healthcare", "weight": 30.0},
                    {"category": "Energy", "weight": 20.0}
                ]
            }
        }
    )

class StrategyResponse(BaseModel):
    name: str
    return_: float
    sharpe: float

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Growth Portfolio",
                "return_": 12.5,
                "sharpe": 1.35
            }
        }
    )