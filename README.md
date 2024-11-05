# Simulated Video Translation Server for HeyGen

**HeyGen (Software Engineer, University Graduate) Take-Home Assignment**

**Author:** Benjamin Liang

This project is a simulated video translation server for HeyGen’s take-home assignment. It includes a Django-based server that mimics a video translation backend with dynamically-updated job statuses and a client library that polls the server for job completion status using adaptive polling based on server feedback.


## Directory Structure:
```
├── heygen_video_translation
│   ├── heygen_video_translation
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       ├── asgi.py
│       ├── wsgi.py
│   ├── vid_trans_api
│       ├── __init__.py
│       ├── migrations
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       ├── views.py
│   ├── manage.py
│   ├── client.py
│   ├── test_integration.py
│   ├── db.sqlite3
│   ├── requirements.txt
├── README.md
```

## Introduction:
This project simulates a backend server with dynamic video translation statuses. The server returns statuses such as ```"pending"```, ```"completed"```, or ```"error"``` with a configurable random delay before completion. The client library provided can be used to interact with this server, polling the job status at adaptive intervals to balance efficiency with prompt updates.
  
## Server Attributes:
- **Possible Statuses:** ```"pending"```, ```"completed"```, or ```"error"```
- **Configurable Random Delay:** Each job status check is delayed by a random amount of time within a specified configurable range, simulating a real-world video translation service.

## Key Files:
- ```manage.py```: Django management script to run the server.
- ```vid_trans_api/urls.py```: Contains URL routing for the API, defining the endpoint for checking job status.
- ```vid_trans_api/views.py```: Implements the ```status_view``` function, which simulates the status and delay.
- ```client.py```: The client library that polls the server for job status using dynamic polling based on real-time server feedback.
- ```test_integration.py```: Integration test that runs multiple polling sessions to verify server responses and polling behavior.
- ```requirements.txt```: Lists all dependencies required for this project.

## Running the Server:
**1) Install Dependencies:**
- Run the following command from the outer ```heygen_video_translation``` directory: ```pip install -r requirements.txt```

**2) Start the Django Server:**
- Use manage.py to start the server: ```python manage.py runserver```
- The server will be accessible at ```http://127.0.0.1:8000```, and the API endpoint for viewing job status is located at ```http://127.0.0.1:8000/vid_trans_api/status```.
- Polling the server is simulated every time the API endpoint webpage is refreshed (user calls client library).

**3) Run Integration Tests:**
- To verify the server and client interaction, run: ```python test_integration.py```
- This script will start the server, perform multiple polling sessions using the client library, and print the progression + final status of each session.

## Core Features:
- **Simulated Server:** The server simulates the video translation backend, returning one of three statuses (```"pending"```, ```"completed"```, or ```"error"```) based on a randomly assigned delay.
- **Dynamic Polling:** The client library polls the server adaptively, using dynamic intervals based on server-provided feedback on estimated completion time.
- **Integration Testing:** The ```test_integration.py``` script tests multiple polling sessions, restarting the server between sessions to ensure independent job processing.

## Ease for Third-Party Use:
The client library (```client.py```) is designed with third-party integration in mind:

- **Configurable Parameters:** Users can adjust polling intervals (```min_polling_interval```, ```max_polling_interval```) and set a maximum number of retries to configure the polling frequency, intervals, and duration.
- **Informative Logging:** Each polling attempt is logged with clear, timestamped messages showing the current status, attempt number, and the time until the next poll.
- **Flexible Package:** The client is structured as a single, self-contained Python class that can be easily included into other projects, and its parameters make it adaptable to different backend server configurations.

## Customer-Centric Design:
This project demonstrates a customer-centric approach by addressing both efficiency and transparency:

- **Efficiency:** Dynamic polling based on signals from server - reduces polling when job is far from being completed & increases frequency when completion is near. This reduces unnecessary server load and optimizes client response time.
- **Transparency:** The server includes ```"estimated_time_remaining"``` in responses, allowing the client to communicate real-time status updates and completion estimates to end-users. This keeps users well-informed without overwhelming the server with requests.

## Future Improvements:
- **Error Handling:** Future enhancements in error handling could include distinguishing between possible type of errors: whether retryable (ex. network issues) or non-retryable (ex. server-side failures).
- **Configurable Server Delay:** Incorporate increased customization by allowing clients to set the polling delay range through an API parameter, enabling more flexible server delay testing.

