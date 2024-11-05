import subprocess
import time
from client import TranslationClient

# Define the number of polling sessions to test
NUM_SESSIONS = 5

# Loop through multiple polling sessions
for session in range(1, NUM_SESSIONS + 1):
    print(f"\nPolling Session {session}:")

    # Start Django server as subprocess, reset every session
    server_process = subprocess.Popen(["python", "manage.py", "runserver"])
    time.sleep(2)

    try:
        # Test run code - set up client, trial run server
        client = TranslationClient("http://127.0.0.1:8000/vid_trans_api")
        result = client.wait_for_completion()

        print(f"Final Result for Session {session}: {result}")

    finally:
        # Clean up by terminating the server process
        server_process.terminate()
        time.sleep(2)