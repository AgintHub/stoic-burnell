# evaluate_backtest_risk PRD

## Description
Delivers a detailed risk analysis and evaluation of market exposures from the backtested strategy returns, including metrics such as volatility, Value-at-Risk, Expected Shortfall, and tail risk, while also assessing position concentration and liquidity impact.


## Conceptual Info

Evaluates the risks associated with the backtested trading strategy, offering insights into potential losses, concentration, and market impact.

## Docstring

### Summary
Analyzes the backtest results to derive a detailed risk assessment.

### Parameters

- **backtest_output** (dict): Output from the backtest calculation, containing cumulative_return, sharpe_ratio, max_drawdown, and win_rate.

### Returns

dict: Contains risk metrics extracted from the backtest output, including: volatility, Value-at-Risk, Expected Shortfall, max_drawdown, tail risk, position concentration, and liquidity impact.

### Raises

- AssertionError: Raised when the input parameters violate assumptions underlying the risk analysis, such as nonsensical confidence levels.
