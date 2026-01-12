from ._design_strategy_logic.analyze_feature_relevance import analyze_feature_relevance
from ._design_strategy_logic.develop_expert_framework import develop_expert_framework
from ._design_strategy_logic.design_entry_signals import design_entry_signals
from ._design_strategy_logic.design_exit_rules import design_exit_rules
from ._design_strategy_logic.determine_position_sizing import determine_position_sizing
from ._design_strategy_logic.calculate_risk_limits import calculate_risk_limits
from ._design_strategy_logic.build_decision_tree import build_decision_tree
from ._design_strategy_logic.optimize_strategy_performance import optimize_strategy_performance

from pydantic import BaseModel, Field
from typing import List


class EngineerFeaturesOutput(BaseModel):
    """Pydantic model for engineer_features node outputs."""
    feature_list: List[str] = (
        Field(..., description = (
            "List of feature names engineered for the strategy")
        )
    )
    feature_formulas: List[str] = (
        Field(..., description = (
            "Formulas or descriptions for each feature in the feature list")
        )
    )
    feature_descriptions: List[str] = (
        Field(..., description = (
            "Descriptions of each feature in the feature list")
        )
    )


class DesignStrategyLogicOutput(BaseModel):
    """Pydantic model for design_strategy_logic node outputs."""
    entry_signals: List[str] = (
        Field(..., description="List of conditions for entering a trade")
    )
    exit_rules: List[str] = (
        Field(..., description="List of conditions for exiting a trade")
    )
    position_sizing: str = (
        Field(..., description = (
            "Method for determining position size (e.g., fixed, risk-based)")
        )
    )
    risk_limits: List[float] = (
        Field(..., description = (
            "List of risk limits (e.g., stop-loss, take-profit levels)")
        )
    )
    decision_tree: str = (
        Field(..., description = (
            "High-level overview of the decision-making process")
        )
    )


def design_strategy_logic(engineer_features_input: EngineerFeaturesOutput, **kwargs) -> DesignStrategyLogicOutput:
    analyzed_features = analyze_feature_relevance(features=engineer_features_input.feature_list, formulas=engineer_features_input.feature_formulas)
    strategy_framework = develop_expert_framework(feature_analysis=analyzed_features, feature_descriptions=engineer_features_input.feature_descriptions)
    entry_conditions: List[str] = design_entry_signals(framework=strategy_framework, features=engineer_features_input.feature_list)
    exit_conditions: List[str] = design_exit_rules(framework=strategy_framework, entry_signals=entry_conditions)
    sizing_method: str = determine_position_sizing(framework=strategy_framework, risk_tolerance=kwargs.get('risk_tolerance', 'medium'))
    risk_parameters: List[float] = calculate_risk_limits(framework=strategy_framework, position_sizing=sizing_method)
    decision_process: str = build_decision_tree(entry_signals=entry_conditions, exit_rules=exit_conditions, position_sizing=sizing_method, risk_limits=risk_parameters)
    optimized_strategy = optimize_strategy_performance(entry_signals=entry_conditions, exit_rules=exit_conditions, position_sizing=sizing_method, risk_limits=risk_parameters)
    return DesignStrategyLogicOutput(
        entry_signals=optimized_strategy['entry_signals'],
        exit_rules=optimized_strategy['exit_rules'],
        position_sizing=optimized_strategy['position_sizing'],
        risk_limits=optimized_strategy['risk_limits'],
        decision_tree=decision_process
    )