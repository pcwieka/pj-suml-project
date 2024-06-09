# PJ SUML Project

This repository hosts a machine learning project aimed at predicting obesity levels based on various health and lifestyle factors. 

The project utilizes the [Obesity or CVD Risk dataset](https://www.kaggle.com/datasets/aravindpcoder/obesity-or-cvd-risk-classifyregressorcluster) from Kaggle.

Built using Kedro, a powerful data and analytics pipeline framework, the project is fully containerized with Docker to ensure seamless deployment and scalability. 

Additionally, a user-friendly UI application is provided, allowing users to input their data and receive predictions regarding their obesity levels.

## Project structure 

### Kedro
The main part of the project. Responsible for the machine learning of the model. It is organized into several Kedro pipelines:

- **data preparation**: Handles data cleaning, transformation, and feature engineering.
- **model training**: Responsible for training the selected machine learning model (method: manual).
- **automl**: Implements automated machine learning techniques to optimize model selection and hyperparameters (method: autogluon).
- **champion challenger**: Compares models to select the best performing one.
- **model deployment**: Deploys the model to pickle file.

### API

The API is implemented using FastAPI and provides an endpoint for predicting obesity levels.

### UI

The UI is implemented using Streamlit and provides a user-friendly form for predicting obesity levels.

## Dockerized Environment
The entire environment is containerized using Docker, ensuring consistency and ease of deployment across different platforms. The key Docker containers/images include:

- **kedro**: Contains the Kedro project and manages the execution of pipelines.
- **model**: Persists the trained model and is used by the API container. The model is saved here by the Kedro pipeline.
- **api**: Provides an API with a predict method for making predictions using the trained model.
- **ui**: A Streamlit application that provides a user-friendly form for predicting obesity levels.

See the [Makefile](Makefile) in the root of the project.

Run `make all` to build and start all containers.

Alternatively you can execute the commands one by one:

```
make build
make up
```

Then run kedro training pipelines:

```
make kedro-run
```

Run `make down` to remove all the containers after you are done.

### API
Use the [API](api/README.md) to use the model for predictions. It's already started in the docker container, use only requests.

### UI
Use the [UI](ui/README.md) to load the form to predict the obesity level. It's already started in the docker container, visit:
TODO: enter the UI URL here.

## Local environment
### Install dependencies using Conda

Install conda environment from the [official website](https://www.anaconda.com/products/individual).

```
conda env create -f conda.yml
```

```
conda env update -f conda.yml
```

```
conda activate pj-suml-project
```

### Run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

To run Kedro Viz:

```
kedro viz
```

### Run API

See the [API doc](api/README.md) for more details how to start it.

### Run UI

See the [UI doc](ui/README.md) for more details how to start it.
