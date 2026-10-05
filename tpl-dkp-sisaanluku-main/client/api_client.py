import requests
import json
# TODO: 
# Import requests library
# Define fetch_data function, that takes an API URL as parameter
# Use try - except structure to
# - make a GET request to the given URL with athe requests library,
# - raise an exception if the response status code indicates an error,
# - return the response data as JSON
# - print an error message if something goes wrong with the request, and return None.


def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.ConnectionError:
        print("Could not connect to the API.")
    except requests.exceptions.HTTPError as http_err:
        status = http_err.response.status_code if http_err.response is not None else "unknown"
        print(f"HTTP error: {status} - {http_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
        return None
    except json.JSONDecodeError:
        print("The server returned invalid JSON.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


