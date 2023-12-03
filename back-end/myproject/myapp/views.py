import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

@csrf_exempt
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

def get_data(request):
    # Dummy data (replace with your actual data retrieval logic)
    data = [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'},
        # Add more items as needed
    ]

    return JsonResponse(data, safe=False)



@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        # Check if the request has JSON data
        if request.body:
            try:
                # Load the JSON data from the request body
                json_data = json.loads(request.body)

                # Access the specific fields (query, category, region, ascent)
                query = json_data.get('query')
                category = json_data.get('category')
                region = json_data.get('region')
                ascent = json_data.get('ascent')
                print("Received query: " + query + " " + category + " " + region + " " + ascent)

                # Process the data (for example, store it in a database)
                # Replace this with your actual data processing logic

                # Return a success message or any other response if needed
                return JsonResponse({'message': 'JSON data processed successfully'})
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        else:
            return JsonResponse({'error': 'No JSON data received'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
