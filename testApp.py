# test_iris_api.py
import requests
import base64
import json

# --- Configuration ---
# Replace with your actual Hugging Face Space URL
# Example: "https://your-username-iris-classifier-api-colab.hf.space/"
API_BASE_URL = "https://your-username-iris-classifier-api-colab.hf.space"

# Replace with the API_USERNAME and API_PASSWORD you set as secrets
API_USERNAME = "testuser"
API_PASSWORD = "testpass"

# --- Sample Iris Features for Prediction ---
# You can change these values to test different inputs
sample_features = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

# --- API Endpoint ---
PREDICT_ENDPOINT = f"{API_BASE_URL.rstrip('/')}/predict" # Ensure no double slashes

# --- Main Application Logic ---
def test_api():
    print(f"Testing API at: {PREDICT_ENDPOINT}")
    print(f"Using username: {API_USERNAME}")

    # Encode credentials for Basic Authentication
    credentials = f"{API_USERNAME}:{API_PASSWORD}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    auth_header = f"Basic {encoded_credentials}"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": auth_header
    }

    print(f"\nSending request with features: {sample_features}")

    try:
        response = requests.post(PREDICT_ENDPOINT, headers=headers, json=sample_features)

        # Check if the request was successful (status code 2xx)
        response.raise_for_status()

        # Parse and print the JSON response
        prediction_result = response.json()
        print("\n--- API Response ---")
        print(json.dumps(prediction_result, indent=4))
        print("--------------------")

    except requests.exceptions.HTTPError as http_err:
        print(f"\nHTTP error occurred: {http_err}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"\nConnection error occurred: {conn_err}")
        print("Please check if the API_BASE_URL is correct and the API is running.")
    except requests.exceptions.Timeout as timeout_err:
        print(f"\nTimeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"\nAn unexpected error occurred: {req_err}")
    except json.JSONDecodeError:
        print(f"\nFailed to decode JSON response. Response text: {response.text}")

if __name__ == "__main__":
    test_api()
