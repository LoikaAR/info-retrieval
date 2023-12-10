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
from .terrier_utils.get_filter_categories import get_top_10_regions, get_top_10_categories

br = generate_factory()

# def get_data(request):
#     """
#     Fetches data and returns it as a JSON response.

#     Args:
#     - request: HttpRequest object

#     Returns:
#     - JsonResponse: JSON response containing data
#     """


def get_data(request):
    # Path to your JSON file
    json_file_path = './ordered_json_file.json'  # Replace with the actual path

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
    regions = get_top_10_regions()
    return JsonResponse({'regions': regions})

def get_categories(request):
    categories = get_top_10_categories()
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
                distance = json_data.get('distance')
                print("Received query: " + query + " " +
                      category + " " + region + " " + distance)
                
                transorm_query(br, query)                

                # Return a success message or any other response if needed

                return JsonResponse({'message': 'JSON data processed successfully'})
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        else:
            return JsonResponse({'error': 'No JSON data received'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
