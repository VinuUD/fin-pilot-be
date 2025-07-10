from app.models.strategy import StrategyRequest, StrategyResponse

def simulate_strategy(request: StrategyRequest) -> StrategyResponse:
    # Fake logic for now
    total_weight = sum(asset.weight for asset in request.assets)
    return_ = round(total_weight * 0.2, 2)
    sharpe = round(1 + total_weight % 10 / 10, 2)

    return StrategyResponse(
        name=request.name,
        return_=return_,
        sharpe=sharpe
    )