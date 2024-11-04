import subprocess
import time

# Start the Django server as a subprocess
server_process = subprocess.Popen(["python", "manage.py", "runserver"])
time.sleep(1)  # Allow server time to start

try:
    # Run client code to interact with the Django server
    from client import TranslationClient
    client = TranslationClient("http://127.0.0.1:8000/vid_trans_api")
    result = client.wait_for_completion()
    print(f"Final Result: {result}")
finally:
    # Clean up by terminating the server process
    server_process.terminate()