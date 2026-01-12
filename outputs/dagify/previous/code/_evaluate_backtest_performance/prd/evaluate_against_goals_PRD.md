# evaluate_against_goals PRD

## Description
Determines whether a trading strategy's performance metrics meet predefined thresholds based on input performance data.


## Conceptual Info

This shim evaluates a strategy's performance metrics against specified thresholds to decide if it meets set goals.

## Docstring

### Summary
Evaluates strategy performance metrics against provided thresholds and returns a boolean indicating success or failure.

### Parameters

- **cumulative_return** (str): String representing the cumulative return of the strategy.
- **sharpe_ratio** (str): String representing the Sharpe ratio of the strategy.
- **max_drawdown** (str): String representing the maximum drawdown experienced by the strategy.
- **win_rate** (str): String representing the win rate of trades executed by the strategy.
- **thresholds** (str): String formatted thresholds against which the performance metrics are evaluated.

### Returns

str: String 'true' or 'false' indicating if performance goals are met.

### Raises

- ValueError: Raised if input strings are improperly formatted or cannot be parsed into numerical values for comparison.
- TypeError: Raised if input parameters are not strings as expected.

### Examples

```python
>>> evaluate_against_goals('0.15', '1.2', '0.2', '0.6', '{"return": 0.1, "sharpe": 1.0, "max_drawdown": 0.3, "win_rate": 0.55}')
true
```

```python
>>> evaluate_against_goals('0.05', '0.8', '0.4', '0.4', '{"return": 0.02, "sharpe": 0.5, "max_drawdown": 0.5, "win_rate": 0.45}')
false
```
