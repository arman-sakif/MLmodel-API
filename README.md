# Iris Species Classifier API

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
[![Hugging Face Spaces](https://img.shields.io/badge/Hugging%20Face%20Spaces-Deployed-yellow?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/spaces/YOUR_HUGGINGFACE_USERNAME/iris-classifier-api-colab)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

This project provides a comprehensive, end-to-end demonstration of how to train a machine learning model and deploy it as a secure, authenticated RESTful API on Hugging Face Spaces using a custom Docker image. The entire development and deployment process is streamlined within a Google Colab notebook, making it easy to replicate and adapt for your own projects.

## 📋 Table of Contents

* [🚀 Features](#-features)
* [💻 Technologies Used](#-technologies-used)
* [📁 Project Structure](#-project-structure)
* [🚀 Setup and Deployment](#-setup-and-deployment)
    * [1. Open and Run the Google Colab Notebook](#1-open-and-run-the-google-colab-notebook)
    * [2. Configure Hugging Face Space Secrets](#2-configure-hugging-face-space-secrets)
    * [3. Monitor Deployment](#3-monitor-deployment)
* [🧪 How to Test the API](#-how-to-test-the-api)
    * [Using `test_iris_api.py`](#using-test_iris_apipy)
    * [Using `curl`](#using-curl)
* [🌐 API Endpoints](#-api-endpoints)
* [🔒 Authentication](#-authentication)
* [💡 Future Improvements](#-future-improvements)
* [🤝 Contributing](#-contributing)
* [❓ Troubleshooting](#-troubleshooting)
* [📄 License](#-license)

## 🚀 Features

* **Iris Classification:** Trains a Logistic Regression model on the classic Iris dataset to accurately classify flower species.
* **FastAPI Integration:** Serves the trained model via a blazing-fast and automatically documented RESTful API using FastAPI.
* **Authenticated API:** Ensures confidentiality by securing the API endpoint with HTTP Basic Authentication. Credentials are safely managed using Hugging Face Spaces Secrets (environment variables).
* **Dockerized Deployment:** Encapsulates the entire application within a Docker container, guaranteeing consistent behavior across different environments.
* **Free Cloud Deployment:** Leverages Hugging Face Spaces' generous free tier for cost-effective and accessible API hosting.
* **Google Colab Workflow:** Provides a self-contained Google Colab notebook (`.ipynb`) that guides you through every step, from model training and file generation to seamless deployment.

## 💻 Technologies Used

* **Python:** The core programming language.
* **scikit-learn:** For machine learning model training and inference.
* **FastAPI:** A modern, fast (high-performance) web framework for building APIs.
* **Uvicorn:** An ASGI server that runs the FastAPI application.
* **Docker:** For creating portable and self-contained application environments.
* **Hugging Face Spaces:** The cloud platform used for deploying and hosting the API.
* **`huggingface_hub`:** A Python library for programmatic interaction with the Hugging Face Hub (Spaces, Models, Datasets).
* **`requests`:** A popular Python library for making HTTP requests to test the API.

## 📁 Project Structure
