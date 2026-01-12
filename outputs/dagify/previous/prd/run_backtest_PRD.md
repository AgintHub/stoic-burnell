# run_backtest PRD

## Description
Executes a strategy backtest to generate strategy key performance metrics such as the cumulative return, Sharpe ratio, maximum drawdown, and win rate.


## Conceptual Info

This node executes a strategy backtest to generate key performance metrics.

## Docstring

### Summary
Runs a strategy backtest with the specified data and strategy logic to obtain the strategy's key performance metrics.

### Parameters

- **data** (List[dict]): A list of dictionaries representing the historical market data used for backtesting.
- **strategy_logic** (str): A string representing the strategy's trade logic.
- **risk_management_rules** (dict): A dictionary containing the strategy's risk management rules.

### Returns

dict: A dictionary containing the strategy's key performance metrics.

### Examples

```python
>>> data = [...]
>>> strategy_logic = '...'
>>> risk_management_rules = {'...' : '...'}
>>> backtest_metrics = run_backtest(data, strategy_logic, risk_management_rules)
>>> print(backtest_metrics)
{'cumulative_return': ..., 'sharpe_ratio': ..., 'max_drawdown': ..., 'win_rate': ...}
```
