from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse
from django.utils.timezone import now
import random

# Configurable random delay range (seconds)
MIN_DELAY = 5
MAX_DELAY = 15
job_start_time = now()
delay_time = random.uniform(MIN_DELAY, MAX_DELAY)  # Set a random delay time within the range

def status_view(request):
    elapsed_time = (now() - job_start_time).total_seconds()

    if elapsed_time < delay_time:
        return JsonResponse({"result": "pending", "estimated_time_remaining": delay_time - elapsed_time})

    # Simulation: 70% chance of success, 30% chance of error
    status = random.choices(["completed", "error"], weights=[0.7, 0.3], k=1)[0]
    return JsonResponse({"result": status})