from ._analyze_trends_and_benchmark.validate_and_parse_csv import validate_and_parse_csv
from ._analyze_trends_and_benchmark.calculate_year_over_year_inflation import calculate_year_over_year_inflation
from ._analyze_trends_and_benchmark.fetch_current_cpi_baseline import fetch_current_cpi_baseline
from ._analyze_trends_and_benchmark.benchmark_against_cpi import benchmark_against_cpi
from ._analyze_trends_and_benchmark.generate_trend_summary import generate_trend_summary

from pydantic import BaseModel, Field
from typing import List


class GenerateHistoricalTimelineOutput(BaseModel):
    """Pydantic model for generate_historical_timeline node outputs."""
    timeline_report_csv: str = (
        Field(..., description="CSV string of the historical timeline with columns: Year, Index, CategoryTotals, LocationTotals.")
    )
    is_timeline_successful: bool = (
        Field(..., description="Flag indicating whether the timeline was generated successfully from the index series and breakdown CSVs.")
    )


class AnalyzeTrendsAndBenchmarkOutput(BaseModel):
    """Pydantic model for analyze_trends_and_benchmark node outputs."""
    inflation_rate_years: List[int] = (
        Field(..., description="Years corresponding to calculated inflation rates.")
    )
    inflation_rate_values: List[float] = (
        Field(..., description="Inflation rates as percent changes for each calculated year.")
    )
    trend_summary: str = (
        Field(..., description="Narrative summary of inflation trends and benchmarking results.")
    )
    is_analysis_successful: bool = (
        Field(..., description="Flag indicating whether inflation trend analysis and benchmarking were completed successfully.")
    )


def analyze_trends_and_benchmark(generate_historical_timeline_input: GenerateHistoricalTimelineOutput, **kwargs) -> AnalyzeTrendsAndBenchmarkOutput:
    """
    Analyzes year-to-year inflation rates from a historical timeline, summarizes
    long-term inflation trends, and benchmarks these trends against the current
    CPI.

    Parameters
    ----------
    timeline_report_csv : str
        CSV string of the historical timeline with columns: Year, Index,
        CategoryTotals, LocationTotals.

    Returns
    -------
    {inflation_rate_years: List[int], inflation_rate_values: List[float], trend_summary: str, is_analysis_successful: bool}
        A dictionary containing the years of calculated inflation rates, the
        corresponding inflation rate values, a narrative summary of
        inflation trends and benchmarking results, and a flag indicating the
        success of the analysis.

    Raises
    ------
    ValueError
        If the input timeline report CSV is empty or malformed.

    Examples
    --------
    >>> analyze_trends_and_benchmark(timeline_report_csv='Year,Index,CategoryTot
    als,LocationTotals\n2020,100,1000,500\n2021,105,1100,550')
    {'inflation_rate_years': [2020, 2021], 'inflation_rate_values': [0.0, 5.0],
    'trend_summary': 'Inflation trend summary and benchmarking results.',
    'is_analysis_successful': True}

    """
    csv_data: str = generate_historical_timeline_input.timeline_report_csv
    
    validated_data: dict = validate_and_parse_csv(csv_string=csv_data)
    
    if not validated_data["is_valid"]:
        return AnalyzeTrendsAndBenchmarkOutput(
            inflation_rate_years=[],
            inflation_rate_values=[],
            trend_summary="Analysis failed due to malformed CSV data.",
            is_analysis_successful=False
        )
    
    parsed_timeline: List[dict] = validated_data["parsed_data"]
    
    inflation_calculations: dict = calculate_year_over_year_inflation(timeline_data=parsed_timeline)
    
    years: List[int] = inflation_calculations["years"]
    rates: List[float] = inflation_calculations["rates"]
    
    current_cpi_data: dict = fetch_current_cpi_baseline()
    
    benchmark_results: dict = benchmark_against_cpi(inflation_rates=rates, years=years, cpi_data=current_cpi_data)
    
    trend_analysis: str = generate_trend_summary(inflation_data=inflation_calculations, benchmark_data=benchmark_results)
    
    return AnalyzeTrendsAndBenchmarkOutput(
        inflation_rate_years=years,
        inflation_rate_values=rates,
        trend_summary=trend_analysis,
        is_analysis_successful=True
    )