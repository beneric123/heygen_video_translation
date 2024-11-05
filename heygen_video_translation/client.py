import requests
import time
import logging

class TranslationClient:
    def __init__(self, base_url, min_polling_interval=1, max_polling_interval=10, max_retries=15):
        """
        Initializes TranslationClient with dynamic polling parameters.

        Parameters:
        - base_url (str): The base URL of the server to connect to.
        - min_polling_interval (int): Minimum polling interval in seconds (default is 1 second).
        - max_polling_interval (int): Maximum polling interval in seconds (default is 10 seconds).
        - max_retries (int): Maximum number of retries (default is 15).
        """
        self.base_url = base_url
        self.min_polling_interval = min_polling_interval
        self.max_polling_interval = max_polling_interval
        self.max_retries = max_retries

        # Configure logging
        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

    def get_status(self):
        """Checks job status from server."""
        try:
            response = requests.get(f"{self.base_url}/status")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error accessing the server: {e}")
            return {"result": "error"}

    def wait_for_completion(self):
        """
        Polls the server based on dynamic server signals until job either completes or errors.
        
        Returns:
        - str: Final job status, either "completed" or "error".
        """
        for attempt in range(1, self.max_retries + 1):
            # Get the current job status and estimated time remaining
            response = self.get_status()
            status = response.get("result", "error")
            estimated_time_remaining = response.get("estimated_time_remaining", self.min_polling_interval)

            # Log the current status and attempt information
            logging.info(
                f"Attempt {attempt}: Status - {status} (Next attempt in {estimated_time_remaining:.2f} seconds)"
            )

            # Check for completion or error
            if status == "completed":
                logging.info("Job completed successfully.")
                return status
            elif status == "error":
                logging.info("Job encountered an error.")
                return status

            # Calculate delay based on estimated time remaining, bounded by min and max polling intervals
            delay = min(max(estimated_time_remaining, self.min_polling_interval), self.max_polling_interval)
            time.sleep(delay)

        logging.warning("Max retries reached. Job did not complete.")
        return "incomplete"

if __name__ == "__main__":
    client = TranslationClient("http://127.0.0.1:8000/vid_trans_api")
    client.wait_for_completion()