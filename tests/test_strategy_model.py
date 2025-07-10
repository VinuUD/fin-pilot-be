import pytest
from pydantic import ValidationError
from app.models.strategy import StrategyRequest, AssetCategory

def test_valid_strategy():
    strategy = StrategyRequest(
        name="Balanced Portfolio",
        assets=[
            {"category": AssetCategory.TECHNOLOGY, "weight": 40.0},
            {"category": AssetCategory.HEALTHCARE, "weight": 30.0},
            {"category": AssetCategory.ENERGY, "weight": 30.0},
        ]
    )
    assert strategy.name == "Balanced Portfolio"

def test_invalid_total_weight():
    with pytest.raises(ValidationError) as exc_info:
        StrategyRequest(
            name="Invalid Portfolio",
            assets=[
                {"category": AssetCategory.TECHNOLOGY, "weight": 60.0},
                {"category": AssetCategory.HEALTHCARE, "weight": 30.0},
            ]
        )
    assert "Total weight must be 100" in str(exc_info.value)

def test_weight_out_of_range():
    with pytest.raises(ValidationError) as exc_info:
        StrategyRequest(
            name="Too Heavy",
            assets=[
                {"category": AssetCategory.TECHNOLOGY, "weight": 120.0},
                {"category": AssetCategory.HEALTHCARE, "weight": -20.0},
            ]
        )
    assert "less than or equal to 100" in str(exc_info.value)
    assert "greater than or equal to 0" in str(exc_info.value)

def test_missing_category():
    with pytest.raises(ValidationError) as exc_info:
        StrategyRequest(
            name="Missing Category",
            assets=[
                {"weight": 100.0}  # Missing category
            ]
        )
    assert "field required" in str(exc_info.value).lower()