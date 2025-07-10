import json
from pathlib import Path
from typing import List, Optional

from app.models.strategy import StrategyRequest

DATA_PATH = Path("data/strategies.json")
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

def _load_json() -> List[dict]:
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def _save_json(data: List[dict]):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

def save_strategy(strategy: StrategyRequest):
    print(strategy.dict())
    data = _load_json()
    data = [s for s in data if s["name"] != strategy.name]
    data.append(strategy.dict())
    _save_json(data)

def get_all_strategies() -> List[dict]:
    return _load_json()

def get_strategy_by_name(name: str) -> Optional[dict]:
    return next((s for s in _load_json() if s["name"] == name), None)

def delete_strategy(name: str) -> bool:
    data = _load_json()
    new_data = [s for s in data if s["name"] != name]
    if len(new_data) == len(data):
        return False
    _save_json(new_data)
    return True