# server/djangoapp/views.py

# ------------------ Imports ------------------
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate

# Get an instance of a logger
logger = logging.getLogger(__name__)

# ------------------ Views ------------------

# Login view for POST request (React frontend)
@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return JsonResponse({"status": "fail", "message": "Only POST allowed"})

    try:
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
    except Exception as e:
        logger.error(f"Error parsing JSON: {e}")
        return JsonResponse({"status": "fail", "message": "Invalid JSON"})

    logger.info(f"Login attempt for username: {username}")
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    else:
        return JsonResponse({"userName": username, "status": "Failed", "message": "Invalid credentials"})


# Logout view
@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"status": "Logged out"})
    return JsonResponse({"status": "fail", "message": "Only POST allowed"})


# Registration view (placeholder)
@csrf_exempt
def registration(request):
    # Implement registration logic here
    return JsonResponse({"status": "success", "message": "Registration endpoint placeholder"})


# Get list of dealerships (placeholder)
def get_dealerships(request):
    # Implement logic to return dealerships here
    return JsonResponse({"dealerships": []})


# Get dealer reviews (placeholder)
def get_dealer_reviews(request, dealer_id):
    # Implement logic to return dealer reviews here
    return JsonResponse({"dealer_id": dealer_id, "reviews": []})


# Get dealer details (placeholder)
def get_dealer_details(request, dealer_id):
    # Implement logic to return dealer details here
    return JsonResponse({"dealer_id": dealer_id, "details": {}})


# Add review view (placeholder)
@csrf_exempt
def add_review(request):
    # Implement logic to add review here
    return JsonResponse({"status": "success", "message": "Add review endpoint placeholder"})
