import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.acquire_market_data import acquire_market_data
from code.clean_and_prepare_data import clean_and_prepare_data
from code.define_strategy_objectives import define_strategy_objectives
from code.deploy_strategy import deploy_strategy
from code.design_execution_logic import design_execution_logic
from code.design_monitoring_and_alerts import design_monitoring_and_alerts
from code.design_order_management import design_order_management
from code.design_risk_controls import design_risk_controls
from code.design_strategy_logic import design_strategy_logic
from code.engineer_features import engineer_features
from code.evaluate_backtest_performance import evaluate_backtest_performance
from code.evaluate_backtest_risk import evaluate_backtest_risk
from code.generate_reports import generate_reports
from code.identify_data_sources import identify_data_sources
from code.optimize_strategy_parameters import optimize_strategy_parameters
from code.run_backtest import run_backtest
from code.set_up_code_repository import set_up_code_repository
from code.set_up_data_storage import set_up_data_storage
from code.setup_backtest_environment import setup_backtest_environment
from code.simulate_live_performance import simulate_live_performance
from code.validate_acquired_data import validate_acquired_data

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

acquire_market_data_async = make_async(acquire_market_data)
clean_and_prepare_data_async = make_async(clean_and_prepare_data)
define_strategy_objectives_async = make_async(define_strategy_objectives)
deploy_strategy_async = make_async(deploy_strategy)
design_execution_logic_async = make_async(design_execution_logic)
design_monitoring_and_alerts_async = make_async(design_monitoring_and_alerts)
design_order_management_async = make_async(design_order_management)
design_risk_controls_async = make_async(design_risk_controls)
design_strategy_logic_async = make_async(design_strategy_logic)
engineer_features_async = make_async(engineer_features)
evaluate_backtest_performance_async = make_async(evaluate_backtest_performance)
evaluate_backtest_risk_async = make_async(evaluate_backtest_risk)
generate_reports_async = make_async(generate_reports)
identify_data_sources_async = make_async(identify_data_sources)
optimize_strategy_parameters_async = make_async(optimize_strategy_parameters)
run_backtest_async = make_async(run_backtest)
set_up_code_repository_async = make_async(set_up_code_repository)
set_up_data_storage_async = make_async(set_up_data_storage)
setup_backtest_environment_async = make_async(setup_backtest_environment)
simulate_live_performance_async = make_async(simulate_live_performance)
validate_acquired_data_async = make_async(validate_acquired_data)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: define_strategy_objectives
    async def run_define_strategy_objectives():
        # Call the async version of define_strategy_objectives with results from dependencies
        return await define_strategy_objectives_async(user_input)

    # Run level 0 nodes in parallel
    results['define_strategy_objectives'] = await run_define_strategy_objectives()

    # Level 1: identify_data_sources, set_up_code_repository
    async def run_identify_data_sources():
        # Call the async version of identify_data_sources with results from dependencies
        return await identify_data_sources_async(results['define_strategy_objectives'])

    async def run_set_up_code_repository():
        # Call the async version of set_up_code_repository with results from dependencies
        return await set_up_code_repository_async(results['define_strategy_objectives'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_identify_data_sources(), run_set_up_code_repository())
    results['identify_data_sources'] = level_1_results[0]
    results['set_up_code_repository'] = level_1_results[1]

    # Level 2: set_up_data_storage, acquire_market_data
    async def run_set_up_data_storage():
        # Call the async version of set_up_data_storage with results from dependencies
        return await set_up_data_storage_async(results['identify_data_sources'])

    async def run_acquire_market_data():
        # Call the async version of acquire_market_data with results from dependencies
        return await acquire_market_data_async(results['identify_data_sources'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_set_up_data_storage(), run_acquire_market_data())
    results['set_up_data_storage'] = level_2_results[0]
    results['acquire_market_data'] = level_2_results[1]

    # Level 3: validate_acquired_data
    async def run_validate_acquired_data():
        # Call the async version of validate_acquired_data with results from dependencies
        return await validate_acquired_data_async(results['acquire_market_data'])

    # Run level 3 nodes in parallel
    results['validate_acquired_data'] = await run_validate_acquired_data()

    # Level 4: clean_and_prepare_data
    async def run_clean_and_prepare_data():
        # Call the async version of clean_and_prepare_data with results from dependencies
        return await clean_and_prepare_data_async(results['validate_acquired_data'])

    # Run level 4 nodes in parallel
    results['clean_and_prepare_data'] = await run_clean_and_prepare_data()

    # Level 5: engineer_features
    async def run_engineer_features():
        # Call the async version of engineer_features with results from dependencies
        return await engineer_features_async(results['clean_and_prepare_data'])

    # Run level 5 nodes in parallel
    results['engineer_features'] = await run_engineer_features()

    # Level 6: design_strategy_logic
    async def run_design_strategy_logic():
        # Call the async version of design_strategy_logic with results from dependencies
        return await design_strategy_logic_async(results['engineer_features'])

    # Run level 6 nodes in parallel
    results['design_strategy_logic'] = await run_design_strategy_logic()

    # Level 7: design_execution_logic, setup_backtest_environment
    async def run_design_execution_logic():
        # Call the async version of design_execution_logic with results from dependencies
        return await design_execution_logic_async(results['design_strategy_logic'])

    async def run_setup_backtest_environment():
        # Call the async version of setup_backtest_environment with results from dependencies
        return await setup_backtest_environment_async(results['design_strategy_logic'])

    # Run level 7 nodes in parallel
    level_7_results = await asyncio.gather(run_design_execution_logic(), run_setup_backtest_environment())
    results['design_execution_logic'] = level_7_results[0]
    results['setup_backtest_environment'] = level_7_results[1]

    # Level 8: design_order_management, run_backtest
    async def run_design_order_management():
        # Call the async version of design_order_management with results from dependencies
        return await design_order_management_async(results['design_execution_logic'])

    async def run_run_backtest():
        # Call the async version of run_backtest with results from dependencies
        return await run_backtest_async(results['setup_backtest_environment'], results['clean_and_prepare_data'])

    # Run level 8 nodes in parallel
    level_8_results = await asyncio.gather(run_design_order_management(), run_run_backtest())
    results['design_order_management'] = level_8_results[0]
    results['run_backtest'] = level_8_results[1]

    # Level 9: evaluate_backtest_risk, evaluate_backtest_performance
    async def run_evaluate_backtest_risk():
        # Call the async version of evaluate_backtest_risk with results from dependencies
        return await evaluate_backtest_risk_async(results['run_backtest'])

    async def run_evaluate_backtest_performance():
        # Call the async version of evaluate_backtest_performance with results from dependencies
        return await evaluate_backtest_performance_async(results['run_backtest'])

    # Run level 9 nodes in parallel
    level_9_results = await asyncio.gather(run_evaluate_backtest_risk(), run_evaluate_backtest_performance())
    results['evaluate_backtest_risk'] = level_9_results[0]
    results['evaluate_backtest_performance'] = level_9_results[1]

    # Level 10: optimize_strategy_parameters, design_risk_controls
    async def run_optimize_strategy_parameters():
        # Call the async version of optimize_strategy_parameters with results from dependencies
        return await optimize_strategy_parameters_async(results['evaluate_backtest_performance'], results['evaluate_backtest_risk'])

    async def run_design_risk_controls():
        # Call the async version of design_risk_controls with results from dependencies
        return await design_risk_controls_async(results['evaluate_backtest_risk'])

    # Run level 10 nodes in parallel
    level_10_results = await asyncio.gather(run_optimize_strategy_parameters(), run_design_risk_controls())
    results['optimize_strategy_parameters'] = level_10_results[0]
    results['design_risk_controls'] = level_10_results[1]

    # Level 11: design_monitoring_and_alerts, simulate_live_performance
    async def run_design_monitoring_and_alerts():
        # Call the async version of design_monitoring_and_alerts with results from dependencies
        return await design_monitoring_and_alerts_async(results['design_risk_controls'])

    async def run_simulate_live_performance():
        # Call the async version of simulate_live_performance with results from dependencies
        return await simulate_live_performance_async(results['optimize_strategy_parameters'])

    # Run level 11 nodes in parallel
    level_11_results = await asyncio.gather(run_design_monitoring_and_alerts(), run_simulate_live_performance())
    results['design_monitoring_and_alerts'] = level_11_results[0]
    results['simulate_live_performance'] = level_11_results[1]

    # Level 12: generate_reports
    async def run_generate_reports():
        # Call the async version of generate_reports with results from dependencies
        return await generate_reports_async(results['evaluate_backtest_performance'], results['evaluate_backtest_risk'], results['design_monitoring_and_alerts'])

    # Run level 12 nodes in parallel
    results['generate_reports'] = await run_generate_reports()

    # Level 13: deploy_strategy
    async def run_deploy_strategy():
        # Call the async version of deploy_strategy with results from dependencies
        return await deploy_strategy_async(results['design_order_management'], results['design_risk_controls'], results['design_monitoring_and_alerts'], results['set_up_data_storage'], results['set_up_code_repository'], results['generate_reports'])

    # Run level 13 nodes in parallel
    results['deploy_strategy'] = await run_deploy_strategy()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()
