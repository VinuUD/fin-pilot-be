from fastapi import HTTPException, APIRouter, Body
router = APIRouter()
from app.storage.json_store import (
    save_strategy, get_all_strategies,
    get_strategy_by_name, delete_strategy
)
from app.models.strategy import StrategyRequest, StrategyResponse

@router.post("/strategies")
def save(strategy: StrategyRequest = Body(..., example={
    "name": "Growth Portfolio",
    "assets": [
        {"category": "Technology", "weight": 50},
        {"category": "Healthcare", "weight": 30},
        {"category": "Energy", "weight": 20}
    ]
})):
    save_strategy(strategy)
    return {"status": "saved"}

@router.get("/strategies")
def list_strategies():
    return get_all_strategies()

@router.get("/strategies/{name}")
def load(name: str):
    strategy = get_strategy_by_name(name)
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return strategy

@router.delete("/strategies/{name}")
def delete(name: str):
    success = delete_strategy(name)
    if not success:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return {"status": "deleted"}

@router.post("/simulate")
def simulate(strategy: StrategyRequest) -> StrategyResponse:
    # Placeholder logic
    return StrategyResponse(
        name=strategy.name,
        return_=12.5,
        sharpe=1.2
    )