import requests
import time
import logging

class TranslationClient:
    def __init__(self, base_url, initial_delay=1, max_delay=30, max_retries=10):
        """
        Initializes the TranslationClient with adaptive polling parameters.

        Parameters:
        - base_url (str): The base URL of the server to connect to.
        - initial_delay (int): Starting delay in seconds between polls (default is 1 second).
        - max_delay (int): Maximum delay in seconds (default is 30 seconds).
        - max_retries (int): Maximum number of retries (default is 10).
        """
        self.base_url = base_url
        self.initial_delay = initial_delay
        self.max_delay = max_delay
        self.max_retries = max_retries

        # Configure logging for clear, user-friendly output
        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

    def get_status(self):
        """Method to check job status from the server."""
        try:
            response = requests.get(f"{self.base_url}/status")
            response.raise_for_status()
            return response.json()["result"]
        except requests.RequestException as e:
            logging.error(f"Error accessing the server: {e}")
            return "error"

    def wait_for_completion(self):
        """
        Polls the server with adaptive delay until job completes or errors out.
        
        Returns:
        - str: The final job status, either "completed" or "error".
        """
        delay = self.initial_delay
        for attempt in range(1, self.max_retries + 1):
            # Get the current job status
            status = self.get_status()
            
            # Log the current status and attempt information
            logging.info(
                f"Attempt {attempt}: Status - {status} (Next attempt in {delay} seconds)"
            )

            # Check for terminal statuses
            if status == "completed":
                logging.info("Job completed successfully.")
                return status
            elif status == "error":
                logging.info("Job encountered an error.")
                return status

            # Wait for the next attempt
            time.sleep(delay)

            # Increase the delay (exponential backoff) with a cap at max_delay
            delay = min(delay * 2, self.max_delay)

        logging.warning("Max retries reached. Job did not complete.")
        return "incomplete"

# Usage Example
if __name__ == "__main__":
    client = TranslationClient("http://127.0.0.1:8000/vid_trans_api")
    client.wait_for_completion()