# _evaluate_backtest_performance - Complete PRD Documentation

## Overview
PRDs for nodes in the '_evaluate_backtest_performance' module.

## Table of Contents

- [get_performance_thresholds](#get_performance_thresholds)

- [evaluate_against_goals](#evaluate_against_goals)

- [identify_strategy_strengths](#identify_strategy_strengths)

- [identify_strategy_weaknesses](#identify_strategy_weaknesses)



---

## get_performance_thresholds

### Description
This shim retrieves and returns performance threshold settings used to evaluate backtest performance against desired goals.

### Conceptual Info

The get_performance_thresholds shim fetches configuration parameters that define acceptable performance metrics for strategy evaluation, enabling flexible and configurable assessment criteria.

### Docstring

**Summary:** Retrieve and return performance thresholds used to evaluate whether a trading strategy meets predefined goals.

**Parameters:**

- kwargs (dict): Optional keyword arguments specifying configuration options or identifiers for obtaining performance thresholds.
**Returns:** str - A string representing a JSON-formatted dictionary with performance threshold parameters such as minimum return, maximum drawdown, minimum Sharpe ratio, and minimum win rate.

**Raises:**

- ValueError: Raised if the retrieved thresholds are invalid or malformed.
- TypeError: Raised if the returned object is not a string or cannot be serialized to a string.
**Examples:**

```python
>>> performance_thresholds_str = get_performance_thresholds()
>>> print(performance_thresholds_str)
'{"min_return": 0.05, "max_drawdown": 0.2, "min_sharpe": 1.0, "min_win_rate": 0.55}'
```

```python
>>> thresholds_json = get_performance_thresholds(dashboard_id='abc123')
>>> print(thresholds_json)
'{"min_return": 0.07, "max_drawdown": 0.15, "min_sharpe": 1.2, "min_win_rate": 0.6}'
```



---

## evaluate_against_goals

### Description
Determines whether a trading strategy's performance metrics meet predefined thresholds based on input performance data.

### Conceptual Info

This shim evaluates a strategy's performance metrics against specified thresholds to decide if it meets set goals.

### Docstring

**Summary:** Evaluates strategy performance metrics against provided thresholds and returns a boolean indicating success or failure.

**Parameters:**

- cumulative_return (str): String representing the cumulative return of the strategy.
- sharpe_ratio (str): String representing the Sharpe ratio of the strategy.
- max_drawdown (str): String representing the maximum drawdown experienced by the strategy.
- win_rate (str): String representing the win rate of trades executed by the strategy.
- thresholds (str): String formatted thresholds against which the performance metrics are evaluated.
**Returns:** str - String 'true' or 'false' indicating if performance goals are met.

**Raises:**

- ValueError: Raised if input strings are improperly formatted or cannot be parsed into numerical values for comparison.
- TypeError: Raised if input parameters are not strings as expected.
**Examples:**

```python
>>> evaluate_against_goals('0.15', '1.2', '0.2', '0.6', '{"return": 0.1, "sharpe": 1.0, "max_drawdown": 0.3, "win_rate": 0.55}')
true
```

```python
>>> evaluate_against_goals('0.05', '0.8', '0.4', '0.4', '{"return": 0.02, "sharpe": 0.5, "max_drawdown": 0.5, "win_rate": 0.45}')
false
```



---

## identify_strategy_strengths

### Description
This shim function analyzes the given strategy performance metrics to identify its key strengths.

### Conceptual Info

This shim analyzes strategy metrics such as cumulative return, Sharpe ratio, max drawdown, and win rate to determine the strategy's key strengths.

### Docstring

**Summary:** Determine the strengths of a trading strategy based on its performance metrics like return, risk-adjusted return, drawdowns, and win rate.

**Parameters:**

- cumulative_return (str): The total return of the strategy over the backtest period, provided as a string.
- sharpe_ratio (str): The risk-adjusted return measure indicating performance per unit of risk.
- max_drawdown (str): The maximum peak-to-trough decline during the backtest period.
- win_rate (str): The percentage of profitable trades, represented as a string.
**Returns:** str - A comma-separated string listing the primary strengths identified from the metrics, such as 'Consistent Growth', 'High Risk-Adjusted Return', 'Low Drawdowns', 'High Win Rate'.

**Raises:**

- ValueError: Raised if any of the input metrics are not valid numeric strings or are missing.
- TypeError: Raised if any input parameters are of incorrect types.
**Examples:**

```python
>>> identify_strategy_strengths('0.15', '1.2', '-0.05', '0.65')
'Consistent Growth, High Risk-Adjusted Return, Low Drawdowns, High Win Rate'
```

```python
>>> identify_strategy_strengths('0.05', '0.8', '-0.1', '0.4')
'Moderate Growth, Decent Risk-Adjusted Return, Manageable Drawdowns, Moderate Win Rate'
```



---

## identify_strategy_weaknesses

### Description
Identifies the weaknesses of a trading strategy based on its cumulative return, sharpe ratio, max drawdown, and win rate.

### Conceptual Info

This shim node identifies the weaknesses of a trading strategy based on its performance metrics.

### Docstring

**Summary:** Identifies the weaknesses of a trading strategy based on its cumulative return, sharpe ratio, max drawdown, and win rate.

**Parameters:**

- cumulative_return (str): Cumulative return of the trading strategy
- sharpe_ratio (str): Sharpe ratio of the trading strategy
- max_drawdown (str): Maximum drawdown of the trading strategy
- win_rate (str): Win rate of the trading strategy
**Returns:** dict - Return a dictionary containing the weaknesses of the trading strategy as a list and the performance metrics as separate values.

**Raises:**

- ValueError: Raised when the input performance metrics are invalid.
- TypeError: Raised when the input performance metrics are of incorrect type.
**Examples:**

```python
>>> shim_input = {'cumulative_return': '0.5', 'sharpe_ratio': '1.2', 'max_drawdown': '0.3', 'win_rate': '0.6'}
>>> identify_strategy_weaknesses(**shim_input)
{'output': ['weak strength 1', 'weak strength 2'], 'cumulative_return': 0.5, 'sharpe_ratio': 1.2, 'max_drawdown': 0.3, 'win_rate': 0.6}
```

