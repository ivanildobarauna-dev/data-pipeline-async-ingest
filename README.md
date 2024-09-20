## Data Consumer Pipeline: Data Pipeline for ingest data in near real time

![Project Status](https://img.shields.io/badge/status-development-yellow?style=for-the-badge&logo=github)
![Python Version](https://img.shields.io/badge/python-3.9-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&logo=mit)

![Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge&logo=python)
![pylint](https://img.shields.io/badge/pylint-10.00-green?style=for-the-badge&logo=python)

[//]: # "[![CI-CD](https://img.shields.io/github/actions/workflow/status/ivdatahub/data-consumer-pipeline/CI-CD.yaml?&style=for-the-badge&logo=githubactions&cacheSeconds=60&label=Tests)](https://github.com/data-consumer-pipeline/data-consumer-pipeline/actions/workflows/CI-CD.yml)"
[//]: # "[![IMAGE-DEPLOY](https://img.shields.io/github/actions/workflow/status/data-consumer-pipeline/data-consumer-pipeline/deploy-image.yml?&style=for-the-badge&logo=github&cacheSeconds=60&label=Registry)](https://github.com/data-consumer-pipeline/data-consumer-pipeline/actions/workflows/deploy-cloud-run.yaml)"
[//]: # "[![GCP-DEPLOY](https://img.shields.io/github/actions/workflow/status/data-consumer-pipeline/data-consumer-pipeline/deploy-cloud-run.yaml?&style=for-the-badge&logo=google&cacheSeconds=60&label=Deploy)](https://github.com/data-consumer-pipeline/data-consumer-pipeline/actions/workflows/deploy-cloud-run.yaml)"

[![Codecov](https://img.shields.io/codecov/c/github/data-consumer-pipeline/data-consumer-pipeline?style=for-the-badge&logo=codecov)](https://app.codecov.io/gh/data-consumer-pipeline/data-consumer-pipeline)

## Project Summary

Pipeline for processing and consuming streaming data from Pub/Sub, integrating with Dataflow for real-time data processing

## Development Stack

[![My Skills](https://skillicons.dev/icons?i=pycharm,python,github,gcp&perline=7)](https://skillicons.dev)

## Cloud Stack (GCP)

<img src="docs/icons/pubsub.png" Alt="Pub/Sub" width="50" height="50"><img src="docs/icons/dataflow.png" Alt="Dataflow" width="50" height="50"><img src="docs/icons/bigquery.png" Alt="BigQuery" width="50" height="50">

- Pub/Sub: Messaging service provided by GCP for sending and receiving messages between FastAPI and Dataflow pipeline.
- Dataflow: Serverless data processing service provided by GCP for executing the ETL process.
- BigQuery: Fully managed, serverless data warehouse provided by GCP for storing and analyzing large datasets.

## Continuous Integration and Continuous Deployment (CI/CD, DevOps)

![My Skills](https://skillicons.dev/icons?i=githubactions)

## Contributing

See the following docs:

- [Contributing Guide](https://github.com/ivdatahub/data-consumer-pipeline/blob/main/CONTRIBUTING.md)
- [Code Of Conduct](https://github.com/ivdatahub/data-consumer-pipeline/blob/main/CODE_OF_CONDUCT.md)

## Project Highlights:

- Hexagonal Architecture: Adoption of Hexagonal Architecture to decouple the core logic from external dependencies, ensuring that any current data source can be replaced seamlessly in case of unavailability. This is facilitated by the use of adapters, which act as intermediaries between the core application and the external services.

- Comprehensive Testing: Development of tests to ensure the quality and robustness of the code at various stages of the ETL process

- Configuration Management: Use of a configuration module to manage project_id and others env variables, providing flexibility and ease of adjustment.

- Continuous Integration and Continuous Deployment: Use of CI/CD pipelines to automate the build, test and deployment processes, ensuring that the application is always up-to-date and ready for use.

- Code Quality: Use of code quality tools such as linters and formatters to ensure that the codebase is clean, consistent and easy to read.

- Documentation: Creation of detailed documentation to facilitate the understanding and use of the application, including installation instructions, usage examples and troubleshooting guides.

# Data Pipeline Process:

1. Data Extraction: The data extraction process consists of making requests to the API to obtain the data. The requests are made in parallel workers using Cloud Dataflow to optimize the process. The data is extracted in JSON format.
2. Data Transformation: The data transformation process consists of converting the data to BigQuery Schema. The transformation is done using Cloud Dataflow in parallel workers to optimize the process.
3. Data Loading: The data loading process consists of loading the data into BigQuery. The data is loaded in parallel workers using Cloud Dataflow to optimize the process.
