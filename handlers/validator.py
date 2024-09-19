## Validation model

import requests
import logging

logging.basicConfig(level=logging.INFO)

# validating the apis
def validate_api_keys(api_keys):
    """
    Validate a list of API keys by making a request to the API endpoint.
    
    :param api_keys: List of API keys to validate
    :return: True if all API keys are valid, False otherwise
    """
    for key in api_keys:
        try:
            response = requests.get("API_ENDPOINT", headers={"authorization": f"Bearer {key}"})
            if response.status_code != 200:
                logging.error(f"Invalid API key: {key}")
                return False
        except Exception as e:
            logging.error(f"API validation error for key {key}: {str(e)}")
            return False
    return True