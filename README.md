# Data Science Project
This project is a production-ready, modular implementation of a complete ML pipeline, from raw data ingestion to model deployment, enhanced with ZenML for MLOps orchestration. The pipeline ensures reproducibility, scalability, and traceability by leveraging ZenML's capabilities for:

Workflow automation (data loading, validation, preprocessing, training, evaluation)

Experiment tracking (metrics, parameters, artifacts)

Model deployment (MLflow, Seldon, or custom serving)

Metadata storage (tracking pipeline runs, data versions, and model lineage)
# Project Objective
To build a robust ML pipeline that:

Ingests raw data

Validates its structure and schema

Transforms data via preprocessing and feature engineering

Trains and evaluates machine learning models

Serves predictions through a web API (Flask or FastAPI)

# Pipeline Workflow
Package metadata and setup config if you want to pip-install your project locally or share it as a module.
<pre>
ml_project/
│
├── data/
│   ├── raw/                   <em># Raw data files</em>
│   ├── processed/             <em># Processed data</em>
│   └── artifacts/             <em># Model artifacts</em>
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── src/
│   ├── pipelines/             <em># ZenML pipelines</em>
│   │   ├── training_pipeline.py
│   │   ├── deployment_pipeline.py
│   │   └── batch_prediction_pipeline.py
│   │
│   ├── steps/                 <em># ZenML steps</em>
│   │   ├── data_loader.py
│   │   ├── data_validation.py
│   │   ├── data_preprocessor.py
│   │   ├── feature_engineer.py
│   │   ├── model_trainer.py
│   │   ├── evaluator.py
│   │   └── deployer.py
│   │
│   ├── utils/                 <em># Utility functions</em>
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── helpers.py
│   │
│   ├── models/                <em># Custom model code</em>
│   │   ├── base_model.py
│   │   └── custom_models.py
│   │
│   └── serving/              <em># Model serving</em>
│       ├── app.py            <em># FastAPI app</em>
│       └── schemas.py        <em># Pydantic models</em>
│
├── tests/                    <em># Unit tests</em>
├── .env                      <em># Environment vars</em>
├── requirements.txt          <em># Dependencies</em>
├── zenml_pipeline.yaml       <em># ZenML config</em>
└── README.md
</pre>
# Project Structure
## config/
config.yaml: Central configuration for file paths, parameters, and schema details.

## logs/
Stores logs from pipeline executions (e.g., run.log) for debugging and traceability.

## research/
Jupyter notebooks for prototyping and testing each stage of the pipeline.

Code is validated here before being refactored into the modular pipeline.

## src/DataScience/
Modular pipeline code:

data_ingestion.py

data_validation.py

data_transformation.py

model_trainer.py

model_evaluation.py

##  Key Files
main.py
Entry point to orchestrate the full ML pipeline from start to finish.

app.py
Flask or FastAPI app to serve model predictions via API endpoints.

template.py
Generates project scaffolding and reusable code templates.

Dockerfile
Containerizes the entire project for easy deployment and reproducibility.

.gitignore
Ignores unnecessary files (__pycache__, .env, logs, etc.) in version control.

params.yaml
Stores hyperparameters and configuration for different pipeline stages (e.g., model type, split ratio).

schema.yaml
Defines expected schema for input data — used during validation.

setup.py
Enables local installation of the project as a Python package.

requirements.txt
Lists all Python dependencies required for the project.


