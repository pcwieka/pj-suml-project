"""Project pipelines."""
from __future__ import annotations

import os
from pathlib import Path
import logging

from kedro.config import OmegaConfigLoader
from kedro.framework.project import settings
from kedro.pipeline import Pipeline

from .pipelines.automl import pipeline as automl_pipeline
from .pipelines.champion_challenger import create_pipeline as champion_challenger_pipeline
from .pipelines.data_preparation import create_pipeline as data_preparation_pipeline
from .pipelines.model_deployment import create_pipeline as model_deployment_pipeline
from .pipelines.model_training import create_pipeline as manual_training_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    project_path = Path(os.getcwd())
    conf_loader = OmegaConfigLoader(conf_source=str(project_path / settings.CONF_SOURCE))
    parameters = conf_loader["parameters"]

    if "model_selection" not in parameters:
        logging.error("Failed to find 'model_selection' in parameters.")
        return {}

    model_selection = parameters["model_selection"]

    pipelines = {}

    # Create and add the data preparation pipeline
    pipelines["data_preparation"] = data_preparation_pipeline()

    # Choose the appropriate training pipeline
    if model_selection['method'] == "autogluon":
        logging.info("Using AutoML model training pipeline.")
        pipelines["model_training"] = automl_pipeline.create_pipeline()
    else:
        logging.info("Using manual model training pipeline.")
        pipelines["model_training"] = manual_training_pipeline()

    # Add the champion vs challenger pipeline
    pipelines["champion_challenger"] = champion_challenger_pipeline()

    # Add the model deployment pipeline
    pipelines["model_deployment"] = model_deployment_pipeline()

    # Define the default pipeline
    pipelines["__default__"] = (
        pipelines["data_preparation"]
        + pipelines["model_training"]
        + pipelines["champion_challenger"]
        + pipelines["model_deployment"]
    )

    return pipelines
