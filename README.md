# Iris Species Classifier API

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
[![Hugging Face Spaces](https://img.shields.io/badge/Hugging%20Face%20Spaces-Deployed-yellow?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/spaces/armansakif/iris-classifier-api)


This project provides a comprehensive, end-to-end demonstration of how to train a machine learning model and deploy it as a secure, authenticated RESTful API on Hugging Face Spaces using a custom Docker image. The entire development and deployment process is streamlined within a Google Colab notebook, making it easy to replicate and adapt for your own projects.

## 📋 Table of Contents

* [Features](#-features)
* [Technologies Used](#-technologies-used)
* [Setup and Deployment](#-setup-and-deployment)
    * [1. Open and Run the Google Colab Notebook](#1-open-and-run-the-google-colab-notebook)
    * [2. Configure Hugging Face Space Secrets](#2-configure-hugging-face-space-secrets)
    * [3. Monitor Deployment](#3-monitor-deployment)
* [How to Test the API](#-how-to-test-the-api)
    * [Using `test_iris_api.py`](#using-test_iris_apipy)
    * [Using `curl`](#using-curl)
* [🌐 API Endpoints](#-api-endpoints)
* [🔒 Authentication](#-authentication)
* [❓ Troubleshooting](#-troubleshooting)

## Features

* **Iris Classification:** Trains a Logistic Regression model on the classic Iris dataset to accurately classify flower species.
* **FastAPI Integration:** Serves the trained model via a blazing-fast and automatically documented RESTful API using FastAPI.
* **Authenticated API:** Ensures confidentiality by securing the API endpoint with HTTP Basic Authentication. Credentials are safely managed using Hugging Face Spaces Secrets (environment variables).
* **Dockerized Deployment:** Encapsulates the entire application within a Docker container, guaranteeing consistent behavior across different environments.
* **Free Cloud Deployment:** Leverages Hugging Face Spaces' generous free tier for cost-effective and accessible API hosting.
* **Google Colab Workflow:** Provides a self-contained Google Colab notebook (`.ipynb`) that guides you through every step, from model training and file generation to seamless deployment.

## Technologies Used

* **Python:** The core programming language.
* **scikit-learn:** For machine learning model training and inference.
* **FastAPI:** A modern, fast (high-performance) web framework for building APIs.
* **Uvicorn:** An ASGI server that runs the FastAPI application.
* **Docker:** For creating portable and self-contained application environments.
* **Hugging Face Spaces:** The cloud platform used for deploying and hosting the API.
* **`huggingface_hub`:** A Python library for programmatic interaction with the Hugging Face Hub (Spaces, Models, Datasets).
* **`requests`:** A popular Python library for making HTTP requests to test the API.

## Setup and Deployment

The most straightforward way to get this project up and running is by executing the provided Google Colab notebook.

### 1. Open and Run the Google Colab Notebook

1.  Click on the following link to open the notebook in Google Colab:
    [**Open in Google Colab**](https://colab.research.google.com/drive/1CKnn2zjJ0YzCKwM_qfsdjJJityETWV3l?usp=sharing)
2.  Once opened, execute all cells sequentially by going to `Runtime > Run all`.
3.  The notebook will guide you through:
    * Installing necessary Python packages.
    * Training the Iris classification model and saving it to a local `./model` directory within the Colab environment.
    * Generating `app.py`, `Dockerfile`, and `requirements.txt` files based on the project's needs.
    * **(Optional)** Providing instructions and code to test the FastAPI locally using `ngrok` (for temporary public access during development).
    * Prompting you to enter your Hugging Face write token.
    * Programmatically creating a new Hugging Face Space (configured with the Docker SDK) under your namespace.
    * Uploading all essential project files (`app.py`, `Dockerfile`, `requirements.txt`, `model/` directory) to your newly created Hugging Face Space.

### 2. Configure Hugging Face Space Secrets

This is a **CRITICAL** step to ensure the security of your API's authentication credentials:

1.  After the Colab notebook successfully uploads your files, navigate to your Hugging Face Space page in your web browser. The URL will look like:
    `https://huggingface.co/spaces/YOUR_HUGGINGFACE_USERNAME/iris-classifier-api-colab`
2.  Click on the **"Settings"** tab for your Space.
3.  Scroll down to the **"Secrets"** section.
4.  Add two new secrets:
    * **Name:** `API_USERNAME`
        **Value:** Choose a strong, unique username that only your team will know.
    * **Name:** `API_PASSWORD`
        **Value:** Choose a strong, unique password for your API.
5.  These secrets are securely stored by Hugging Face and will be automatically injected as environment variables into your running Docker container. Your FastAPI application will then retrieve these values to validate incoming requests.

### 3. Monitor Deployment

* Once you've pushed the files and configured the secrets, Hugging Face Spaces will automatically detect the changes and begin building your Docker image and deploying your application.
* You can monitor the build process and runtime logs by clicking on the **"Logs"** tab on your Space page.
* When the status changes to "Running", your API is fully live and ready to receive requests!


## How to Test the API

You can test the deployed API using the provided `testApp.py` Python script or by directly using `curl` from your terminal.

### Using `test_iris_api.py` (in online ide)

1.  Go to https://www.onlinegdb.com/online_c_compiler and select language as Python3
2.  copy paste the contents of testApp.py and run

    You should see the prediction results in a clear JSON format.

### Using `curl`

You can also test the API directly from your terminal using `curl`.

1.  **Encode Credentials:** First, encode your API username and password in Base64:
    ```bash
    echo -n "YOUR_API_USERNAME:YOUR_API_PASSWORD" | base64
    # Example output: dGVzdHVzZXI6dGVzdHBhc3M= (This is for "testuser:testpass")
    ```
    Copy the resulting base64 encoded string.

2.  **Send POST Request:** Replace `YOUR_HUGGINGFACE_USERNAME-iris-classifier-api-colab.hf.space` with your actual Space's URL and `YOUR_BASE64_ENCODED_CREDENTIALS` with the string you generated in the previous step.

    ```bash
    curl -X POST "https://YOUR_HUGGINGFACE_USERNAME-iris-classifier-api-colab.hf.space/predict" \
         -H "accept: application/json" \
         -H "Content-Type: application/json" \
         -H "Authorization: Basic YOUR_BASE64_ENCODED_CREDENTIALS" \
         -d '{"sepal_length": 5.0, "sepal_width": 3.4, "petal_length": 1.5, "petal_width": 0.3}'
    ```

## API Endpoints

The deployed FastAPI application exposes the following endpoints:

* **`POST /predict`**
    * **Description:** Predicts the species of an Iris flower based on provided features.
    * **Authentication:** Requires HTTP Basic Authentication.
    * **Request Body (JSON):**
        ```json
        {
          "sepal_length": 5.1,
          "sepal_width": 3.5,
          "petal_length": 1.4,
          "petal_width": 0.2
        }
        ```
    * **Response Body (JSON):**
        ```json
        {
          "predicted_species": "setosa",
          "prediction_probabilities": {
            "setosa": 0.9999999999999999,
            "versicolor": 1.1102230246251565e-16,
            "virginica": 0.0
          }
        }
        ```

* **`GET /health`**
    * **Description:** A simple health check endpoint to verify the API is running and the model is loaded.
    * **Authentication:** None required.
    * **Response Body (JSON):**
        ```json
        {
          "status": "ok",
          "model_loaded": true
        }
        ```

You can also access the interactive API documentation (Swagger UI) directly in your browser at:
`https://YOUR_HUGGINGFACE_USERNAME-iris-classifier-api-colab.hf.space/docs`

## 🔒 Authentication

This API utilizes **HTTP Basic Authentication** for access control. This means that every request to the `/predict` endpoint must include an `Authorization` header containing your base64-encoded `username:password` string. The actual credentials (`API_USERNAME` and `API_PASSWORD`) are securely stored as environment variables (secrets) within your Hugging Face Space.


## ❓ Troubleshooting

* **`404 Not Found` when testing the API:**
    * **Cause:** This almost always means the `API_BASE_URL` in your `test_iris_api.py` script is incorrect.
    * **Solution:** Ensure `API_BASE_URL` is set to the correct Hugging Face Space subdomain URL (e.g., `https://YOUR_HUGGINGFACE_USERNAME-iris-classifier-api-colab.hf.space`), **not** the `huggingface.co/spaces/...` URL.

* **`401 Unauthorized` when testing the API:**
    * **Cause:** Incorrect `API_USERNAME` or `API_PASSWORD` in your `test_iris_api.py` script, or the secrets were not correctly set on Hugging Face Spaces.
    * **Solution:** Double-check your credentials in `test_iris_api.py` against the secrets you configured in your Hugging Face Space settings. Ensure your Hugging Face API token used for pushing has "write" permissions.

* **"You don't have the rights to create a space..." error during Colab push:**
    * **Cause:** The Hugging Face API token used in Colab does not have "write" permissions, or the `your_hf_username` variable in your Colab notebook does not exactly match your Hugging Face profile username.
    * **Solution:** Generate a new Hugging Face token with "write" permissions at <https://huggingface.co/settings/tokens> and update it in your Colab notebook. Verify your `your_hf_username` variable is correct (case-sensitive).
