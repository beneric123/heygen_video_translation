from django.shortcuts import render

# Create your views here.


import random
from django.http import JsonResponse
from django.utils.timezone import now

# Delay can be custom configured
DELAY = 10
job_start_time = now()

def status_view(request):
    elapsed_time = (now() - job_start_time).total_seconds()

    # Return 'pending' until a configurable time has passed
    if elapsed_time < DELAY:
        return JsonResponse({"result": "pending"})

    # After DELAY seconds, return either 'completed' or 'error'
    return JsonResponse({"result": "completed" if random.choice([True, False]) else "error"})
