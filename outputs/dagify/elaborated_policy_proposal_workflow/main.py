import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.fetch_household_expenditure_data import fetch_household_expenditure_data
from code.analyze_trends_and_benchmark import analyze_trends_and_benchmark
from code.compute_category_location_breakdowns import compute_category_location_breakdowns
from code.compute_index_series import compute_index_series
from code.define_alternative_inflation_index import define_alternative_inflation_index
from code.draft_policy_proposal import draft_policy_proposal
from code.elaborate_policy_proposal import elaborate_policy_proposal
from code.generate_historical_timeline import generate_historical_timeline
from code.produce_final_report import produce_final_report

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

fetch_household_expenditure_data_async = make_async(fetch_household_expenditure_data)
analyze_trends_and_benchmark_async = make_async(analyze_trends_and_benchmark)
compute_category_location_breakdowns_async = make_async(compute_category_location_breakdowns)
compute_index_series_async = make_async(compute_index_series)
define_alternative_inflation_index_async = make_async(define_alternative_inflation_index)
draft_policy_proposal_async = make_async(draft_policy_proposal)
elaborate_policy_proposal_async = make_async(elaborate_policy_proposal)
generate_historical_timeline_async = make_async(generate_historical_timeline)
produce_final_report_async = make_async(produce_final_report)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: fetch_household_expenditure_data
    async def run_fetch_household_expenditure_data():
        # Call the async version of fetch_household_expenditure_data with results from dependencies
        return await fetch_household_expenditure_data_async(user_input)

    # Run level 0 nodes in parallel
    results['fetch_household_expenditure_data'] = await run_fetch_household_expenditure_data()

    # Level 1: define_alternative_inflation_index, compute_category_location_breakdowns
    async def run_define_alternative_inflation_index():
        # Call the async version of define_alternative_inflation_index with results from dependencies
        return await define_alternative_inflation_index_async(results['fetch_household_expenditure_data'])

    async def run_compute_category_location_breakdowns():
        # Call the async version of compute_category_location_breakdowns with results from dependencies
        return await compute_category_location_breakdowns_async(results['fetch_household_expenditure_data'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_define_alternative_inflation_index(), run_compute_category_location_breakdowns())
    results['define_alternative_inflation_index'] = level_1_results[0]
    results['compute_category_location_breakdowns'] = level_1_results[1]

    # Level 2: compute_index_series
    async def run_compute_index_series():
        # Call the async version of compute_index_series with results from dependencies
        return await compute_index_series_async(results['fetch_household_expenditure_data'], results['define_alternative_inflation_index'])

    # Run level 2 nodes in parallel
    results['compute_index_series'] = await run_compute_index_series()

    # Level 3: generate_historical_timeline
    async def run_generate_historical_timeline():
        # Call the async version of generate_historical_timeline with results from dependencies
        return await generate_historical_timeline_async(results['compute_index_series'], results['compute_category_location_breakdowns'])

    # Run level 3 nodes in parallel
    results['generate_historical_timeline'] = await run_generate_historical_timeline()

    # Level 4: analyze_trends_and_benchmark
    async def run_analyze_trends_and_benchmark():
        # Call the async version of analyze_trends_and_benchmark with results from dependencies
        return await analyze_trends_and_benchmark_async(results['generate_historical_timeline'])

    # Run level 4 nodes in parallel
    results['analyze_trends_and_benchmark'] = await run_analyze_trends_and_benchmark()

    # Level 5: draft_policy_proposal
    async def run_draft_policy_proposal():
        # Call the async version of draft_policy_proposal with results from dependencies
        return await draft_policy_proposal_async(results['analyze_trends_and_benchmark'])

    # Run level 5 nodes in parallel
    results['draft_policy_proposal'] = await run_draft_policy_proposal()

    # Level 6: elaborate_policy_proposal
    async def run_elaborate_policy_proposal():
        # Call the async version of elaborate_policy_proposal with results from dependencies
        return await elaborate_policy_proposal_async(results['draft_policy_proposal'])

    # Run level 6 nodes in parallel
    results['elaborate_policy_proposal'] = await run_elaborate_policy_proposal()

    # Level 7: produce_final_report
    async def run_produce_final_report():
        # Call the async version of produce_final_report with results from dependencies
        return await produce_final_report_async(results['elaborate_policy_proposal'])

    # Run level 7 nodes in parallel
    results['produce_final_report'] = await run_produce_final_report()

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
