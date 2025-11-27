# Step 1: Using the same file from previous task
import requests


# Step 2: Create custom exception class
class APIResponseError(Exception):
    pass
    # /def __init__(self, message):
        # super().__init__(message)


# Step 3: Modify network function to raise this custom exception
def fetch_api_data(url):
    try:
        response = requests.get(url, timeout=3)

        # Status code failure
        if response.status_code != 200:
            raise APIResponseError(f"Invalid Status Code: {response.status_code}")

        # Try JSON conversion
        try:
            return response.json()
        except ValueError:
            raise APIResponseError("Response is not JSON format")

    except requests.exceptions.ConnectionError:
        raise APIResponseError("Host unreachable / No internet connection")
    except requests.exceptions.Timeout:
        raise APIResponseError("Request timed out")
    except Exception as e:
        raise APIResponseError(f"Unexpected error: {str(e)}")


# Step 5: Testing with good & bad URLs
urls = [
    "https://jsonplaceholder.typicode.com/todos/1",  # Good JSON
    "https://www.google.com",                        # Non-JSON response
    "https://wrong-url-test-invalid.com"             # Host unreachable
]

for url in urls:
    print("\nTesting URL:", url)
    try:
        result = fetch_api_data(url)
        print("SUCCESS:", result)
    except APIResponseError as e:
        print("ERROR:", e)
