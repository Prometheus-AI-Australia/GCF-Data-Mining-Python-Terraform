# Data Mining System Build With Google Cloud Functions

## Introduction
The Data Mining System has been built with the intent to showcase how one can
build data mining systems within GCP using their serverless compute engine,
GCF.

This application periodically polls the [Binance](https://www.binance.com/en) 
Crypocurrency exchange to collect financial information on different 
cryptocurrencies that are being traded. This information is then written down
into a Google Cloud Storage bucket where it can be further processed by 
downstream ETL systems.

## Configuration
There are two primary areas to configure the application:

- `src/infrastructure/configuration/<ENVIRONMENT>`
    - `backend.tfvars` - defines the backend configuration (bucket, prefix, etc.)
    - `deployment.tfvars` - defines deployment configuration (GCF name, etc.)
- `src/function/config.py` - contains a configuration object which can be edited.

## Deployment
**Note**: You **must** have `GOOGLE_APPLICATION_CREDENTIALS` set in your 
environment running before you go to deploy. This is what Terraform uses to
access your GCP environment. You may also need to create the deployment bucket 
you have configured if it hasn't already been created.

After you've set everything up, you can run the following command to deploy the
application into your configured GCP environment.

```bash
make deploy
```

## Testing
All Python tests are managed via [pytest](https://docs.pytest.org/en/stable/). 
To run the testing suite for the first time, you must perform the following 
steps:

1. Initialise your environment (`make init`).
2. Activate your python virtual environment (`conda activate gcf-data-mining`).
3. Run the testing suite (`make tests`).

For subsequent runs you can simply run the testing command:

```bash
make tests
```