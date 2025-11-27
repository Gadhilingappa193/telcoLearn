import requests  

def fetch_data_from_api(url):
    try:
        print(f"\nFetching: {url}")
        response = requests.get(url, timeout=3)   # 3-second timeout
        response.raise_for_status()               # raises HTTPError for bad responses

        # return JSON data if valid
        return response.json()

    except requests.exceptions.Timeout:
        print("Error: Request timed out")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")

    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the server")

    except Exception as e:
        print(f"Unexpected Error: {e}")

#testing

# Good URL (JSON placeholder API)
good_url = "https://jsonplaceholder.typicode.com/posts/1"

# Bad URL (invalid domain)
bad_url = "https://wrong-domain-example-12345.com/api"

print("Testing a GOOD URL:")
print(fetch_data_from_api(good_url))

print("\nTesting a BAD URL:")
print(fetch_data_from_api(bad_url))