"""
The json module contains functions related to handling HTTP requests and JSON data.
"""
import json
import sys
import os
from .terrier_utils.indexer import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .terrier_utils.get_filters import get_top_5_regions, get_top_categories,apply_category_filter

br = generate_factory()

def get_data(request):
    # path to ordered json file
    # json_file_path = './myapp/terrier_utils/ordered_json_file.json'

    json_file_path = '../../front-end/public/ordered_json_file.json'

    # Check if the file exists
    if os.path.exists(json_file_path):
        print("FILE FOUND")
        # Open and read the contents of the JSON file
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)

        # Return the JSON data as a JSON response
        return JsonResponse(json_data,safe=False)
    else:
        print("FILE NOT FOUND")
        
        # Return a response indicating the file was not found
        return JsonResponse({"error": "File not found"}, status=404)


def get_regions(request):
    regions = get_top_5_regions()
    return JsonResponse({'regions': regions})

def get_categories(request):
    categories = get_top_categories()
    return JsonResponse({'categories': categories})


def get_csrf_token(request):
    """
    Retrieves the CSRF token and returns it in a JSON response.

    Args:
    - request: HttpRequest object

    Returns:
    - JsonResponse: JSON response containing CSRF token
    """
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


# @csrf_exempt needed for POST!
@csrf_exempt
def submit_form(request):
    """
    Processes JSON data from a POST request and returns a JSON response.

    Args:
    - request: HttpRequest object

    Returns:
    - JsonResponse: JSON response confirming successful data processing or error
    """
    if request.method == 'POST':
        # Check if the request has JSON data
        if request.body:
            try:
                # Load the JSON data from the request body
                json_data = json.loads(request.body)

                # Access the specific fields (query, category, region)
                query = json_data.get('query')
                category = json_data.get('category')
                region = json_data.get('region')
                distance = json_data.get('distance', {})
                min_distance = distance.get('min', '')
                max_distance = distance.get('max', '')
                print("Received query: " + query + " " +
                      category + " " + region + " min distance" + str(min_distance) + " max distance:" + str(max_distance))

                transorm_query(br, query)
                apply_category_filter(category,region, min_distance, max_distance)

                # Return a success message or any other response if needed

                return JsonResponse({'message': 'JSON data processed successfully'})
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        else:
            return JsonResponse({'error': 'No JSON data received'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



@csrf_exempt
def submit_recommendation(request):
    """
    Processes JSON data from a POST request and returns a JSON response.

    Args:
    - request: HttpRequest object

    Returns:
    - JsonResponse: JSON response confirming successful data processing or error
    """
    if request.method == 'POST':
        # Check if the request has JSON data
        if request.body:
            try:
                # Load the JSON data from the request body
                json_data = json.loads(request.body)

                # Access the specific fields (query, category, region)
                query = json_data.get('query')
                name = json_data.get('name')
                set_helpful = json_data.get('setHelpful')
                print("Received query: " + query + "| name: " + name
                      + "| setHelpful: " + set_helpful)
                # Return a success message or any other response if needed

                return JsonResponse({'message': 'JSON data processed successfully'})
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        else:
            return JsonResponse({'error': 'No JSON data received'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
