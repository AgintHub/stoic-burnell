# _run_backtest - Complete PRD Documentation

## Overview
PRDs for nodes in the '_run_backtest' module.

## Table of Contents

- [initialize_backtest_engine](#initialize_backtest_engine)

- [prepare_strategy_data](#prepare_strategy_data)

- [parse_simulation_parameters](#parse_simulation_parameters)

- [load_trading_strategy](#load_trading_strategy)

- [execute_backtest](#execute_backtest)

- [calculate_performance_metrics](#calculate_performance_metrics)

- [extract_cumulative_return](#extract_cumulative_return)

- [calculate_sharpe_ratio](#calculate_sharpe_ratio)

- [calculate_max_drawdown](#calculate_max_drawdown)

- [calculate_win_rate](#calculate_win_rate)



---

## initialize_backtest_engine

### Description
This shim initializes and configures the backtesting engine based on the specified framework and configuration.

### Conceptual Info

This shim sets up the backtesting environment by initializing the chosen framework with the provided configuration details.

### Docstring

**Summary:** Initializes a backtesting engine based on the specified framework and configuration string.

**Parameters:**

- framework (str): The name of the backtesting framework to initialize (e.g., 'Zipline', 'backtrader').
- config (str): Configuration parameters or settings for the backtesting framework, typically in a serialized string format.
**Returns:** str - A string identifier or representation of the initialized backtest engine object.

**Raises:**

- ValueError: If the framework name or configuration string is invalid or missing.
- TypeError: If the input parameters are of incorrect types.
**Examples:**

```python
>>> initialize_backtest_engine('backtrader', '{ "setting": "value" }')
'backtest_engine_instance_id_12345'
```

```python
>>> initialize_backtest_engine('Zipline', '{}')
'zipline_engine_obj_67890'
```



---

## prepare_strategy_data

### Description
This shim prepares strategy data to be used in a backtest, given a list of data adapters and the cleaned data.

### Conceptual Info

The `prepare_strategy_data` shim prepares strategy data by combining cleaned data and data adapters, and returns the prepared data as a string.

### Docstring

**Summary:** Prepare strategy data from cleaned data and data adapters.

**Parameters:**

- data_adapters (LIST_STR): List of data adapters used in the strategy data preparation.
- cleaned_data (STR): Cleaned data used in the strategy data preparation.
**Returns:** STR - Strategy data ready for backtesting in string format, including data adapters and cleaned data.

**Raises:**

- ValueError: When input data adapters or cleaned data are invalid or missing.
- TypeError: When input data adapters or cleaned data are of incorrect types.
**Examples:**

```python
>>> data_adapters = ['CSV', 'database connection']
>>> cleaned_data = 'cleaned_data.csv'
>>> output = prepare_strategy_data(data_adapters, cleaned_data)
'Strategy data prepared with data adapters CSV and database connection, and cleaned data cleaned_data.csv.'
```

```python
>>> data_adapters = ['Pandas', 'database connection']
>>> cleaned_data = 'cleaned_data.csv'
>>> output = prepare_strategy_data(data_adapters, cleaned_data)
'Strategy data prepared with data adapters Pandas and database connection, and cleaned data cleaned_data.csv.'
```



---

## parse_simulation_parameters

### Description
This shim function extracts and interprets simulation parameters from a serialized string input into a structured format for use in backtesting workflows.

### Conceptual Info

The shim parses a string containing simulation parameters into a structured format that can be utilized by backtesting components.

### Docstring

**Summary:** The function takes a string of simulation parameters, parses it into a structured representation, and returns the formatted string. It ensures that the input string conforms to expected parameter formats and handles potential parsing errors.

**Parameters:**

- parameters (str): A string containing simulation parameters such as start/end dates, initial capital, frequency, etc.
**Returns:** str - A formatted or serialized string representing the parsed simulation parameters suitable for downstream use.

**Raises:**

- ValueError: Raised if the input string cannot be parsed into valid simulation parameters.
- TypeError: Raised if the input parameter is not of type str.
**Examples:**

```python
>>> parse_simulation_parameters('start_date=2020-01-01;end_date=2020-12-31;initial_capital=100000')
'parsed_parameters_string_or_structured_format'
```

```python
>>> parse_simulation_parameters('invalid format')
ValueError
```



---

## load_trading_strategy

### Description
This shim loads a trading strategy based on provided strategy parameters within a larger trading backtest framework.

### Conceptual Info

This shim retrieves or constructs a trading strategy configuration based on input parameters for use in backtesting or live trading.

### Docstring

**Summary:** Loads a trading strategy based on provided strategy parameters; required to be implemented to parse and instantiate strategy data from parameters.

**Parameters:**

- strategy_params (str): A string containing serialized or configuration-based parameters that define the trading strategy to load.
**Returns:** str - A string representing the loaded trading strategy, suitable for execution within the backtest engine.

**Raises:**

- ValueError: Raised if strategy_params is invalid or cannot be parsed into a strategy.
- TypeError: Raised if strategy_params is not of type str.
**Examples:**

```python
>>> strategy_str = load_trading_strategy('{"type": "mean_reversion", "parameters": {"window": 20}}')
'strategy_representation_string_or_object'
```

```python
>>> strategy_str = load_trading_strategy('default_strategy_params')
'strategy_representation_string_or_object'
```



---

## execute_backtest

### Description
This shim executes a backtest of a trading strategy given environment setup, cleaned data, and configuration parameters, returning performance metrics.

### Conceptual Info

This shim encapsulates the complex process of running a backtest across configured environments, applying strategies, and calculating performance metrics, serving as a bridge between setup and analysis.

### Docstring

**Summary:** Executes a backtest of a trading strategy based on provided environment setup, cleaned data, and configuration parameters, returning performance metrics as a JSON string.

**Parameters:**

- setup_backtest_environment_input (SetupBacktestEnvironmentOutput): Object containing environment configuration such as backtesting framework, data adapters, simulation parameters, and additional configuration.
- clean_and_prepare_data_input (CleanAndPrepareDataOutput): Object containing information about data cleaning success, missing values handled, derived fields, and dataset readiness.
**Returns:** STR - A JSON-formatted string with performance metrics: cumulative return, Sharpe ratio, max drawdown, and win rate.

**Raises:**

- ValueError: Raised if input parameters fail validation or required fields are missing.
- TypeError: Raised if input parameters are of incorrect types.
**Examples:**

```python
>>> result = execute_backtest(setup_backtest_environment_input, clean_and_prepare_data_input)
>>> print(result)
'{"cumulative_return": 0.15, "sharpe_ratio": 1.2, "max_drawdown": 0.05, "win_rate": 0.6}'
```

```python
>>> result = execute_backtest(env_config, cleaned_data)
>>> print(result)
'{"cumulative_return": 0.25, "sharpe_ratio": 1.5, "max_drawdown": 0.03, "win_rate": 0.65}'
```



---

## calculate_performance_metrics

### Description
This shim retrieves and computes key performance metrics from backtest results to evaluate trading strategy effectiveness.

### Conceptual Info

This shim extracts and calculates essential performance metrics from backtest results to assess trading strategy performance.

### Docstring

**Summary:** Compute and return key performance metrics such as cumulative return, Sharpe ratio, max drawdown, and win rate from backtest results data.

**Parameters:**

- results (str): Serialized string representing the backtest results data structure from which performance metrics are derived.
**Returns:** str - A JSON string encapsulating the calculated metrics: cumulative_return (float), sharpe_ratio (float), max_drawdown (float), and win_rate (float).

**Raises:**

- ValueError: Raised if the input string 'results' is improperly formatted or missing required data fields.
- TypeError: Raised if the input 'results' is not of type str.
**Examples:**

```python
>>> performance_metrics_str = calculate_performance_metrics(results=serialized_results_str)
'{"cumulative_return": 0.15, "sharpe_ratio": 1.2, "max_drawdown": -0.05, "win_rate": 0.6}'
```

```python
>>> metrics_json = calculate_performance_metrics(results=serialized_results_str)
'{"cumulative_return": 0.25, "sharpe_ratio": 1.5, "max_drawdown": -0.1, "win_rate": 0.65}'
```



---

## extract_cumulative_return

### Description
This shim function extracts the total cumulative return metric from a performance metrics dictionary.

### Conceptual Info

The shim retrieves the cumulative return value from a metrics dictionary to be used in larger backtesting workflows.

### Docstring

**Summary:** Extracts the 'cumulative_return' float value from a metrics dictionary containing backtest performance results.

**Parameters:**

- metrics (str): A string identifier for the metrics, typically a JSON-formatted string or a key to locate the metrics dictionary containing performance data.
**Returns:** float - The total cumulative return metric as a floating-point number.

**Raises:**

- ValueError: Raised if the metrics input does not contain the 'cumulative_return' key or if the data is malformed.
- TypeError: Raised if the input 'metrics' is not a string or a compatible data structure.
**Examples:**

```python
>>> performance_metrics = {'cumulative_return': 0.15, 'sharpe_ratio': 1.2, 'max_drawdown': 0.05, 'win_rate': 0.6}
>>> output = extract_cumulative_return(metrics=performance_metrics)
0.15
```

```python
>>> performance_metrics = '{"cumulative_return": 0.25, "sharpe_ratio": 1.3}'
>>> output = extract_cumulative_return(metrics=performance_metrics)
0.25
```



---

## calculate_sharpe_ratio

### Description
This shim computes the Sharpe ratio of the trading strategy based on performance metrics.

### Conceptual Info

The shim calculates the Sharpe ratio, a key metric for evaluating the risk-adjusted return of a trading strategy, based on provided performance metrics.

### Docstring

**Summary:** This function computes the Sharpe ratio of the strategy from given performance metrics, requiring a metrics dictionary input and returning a float value representing the Sharpe ratio.

**Parameters:**

- metrics (str): A string identifier or JSON-formatted string representing the performance metrics dictionary, including return, risk measures, and other relevant data.
**Returns:** float - A floating-point number indicating the strategy's risk-adjusted return (Sharpe ratio).

**Raises:**

- ValueError: Raised if the metrics input is invalid or missing required information for calculation.
- TypeError: Raised if the input metrics is not of the expected string type.
**Examples:**

```python
>>> metrics_data = '{"return": 0.15, "volatility": 0.10, "risk_free_rate": 0.02}'
>>> sharpe = calculate_sharpe_ratio(metrics=metrics_data)
1.3
```

```python
>>> metrics_json = '{"return": 0.10, "volatility": 0.05, "risk_free_rate": 0.01}'
>>> result = calculate_sharpe_ratio(metrics=metrics_json)
2.0
```



---

## calculate_max_drawdown

### Description
A shim node that computes the maximum drawdown metric from given performance metrics data.

### Conceptual Info

This shim calculates the maximum drawdown metric based on performance metrics data to assess worst-case loss in strategy performance.

### Docstring

**Summary:** Computes the maximum drawdown value from the provided performance metrics data, given as a string, and returns it as a float.

**Parameters:**

- metrics (str): A string containing serialized or processed performance metrics data from which the maximum drawdown is extracted.
**Returns:** float - A float representing the maximum drawdown value, indicating the largest peak-to-trough decline observed.

**Raises:**

- ValueError: Raised if the input metrics data is invalid or cannot be parsed to extract the maximum drawdown.
- TypeError: Raised if the input is not of type str.
**Examples:**

```python
>>> calculate_max_drawdown('{"max_drawdown": 0.25}')
0.25
```

```python
>>> calculate_max_drawdown('metrics data with max drawdown of 0.15')
0.15
```



---

## calculate_win_rate

### Description
This shim calculates the win rate metric from the provided performance metrics data within the backtesting system.

### Conceptual Info

This shim extracts or computes the win rate metric from a set of performance metrics obtained during backtesting, facilitating evaluation of trading strategy profitability.

### Docstring

**Summary:** Calculates and returns the win rate metric from the provided performance metrics data, ensuring proper data validation and handling of metric extraction.

**Parameters:**

- metrics (str): A string containing performance metrics data from which the win rate will be extracted.
**Returns:** float - The win rate as a floating-point number representing the proportion of winning trades.

**Raises:**

- ValueError: Raised if the input metrics data is empty, malformed, or does not contain the win rate information.
- TypeError: Raised if the input is not of type str.
**Examples:**

```python
>>> metrics_data = '{"win_rate": 0.65, "sharpe_ratio": 1.2}'
>>> result = calculate_win_rate(metrics_data)
0.65
```

```python
>>> invalid_metrics = 'invalid data'
>>> calculate_win_rate(invalid_metrics)
ValueError: Unable to parse win rate from metrics data.
```

