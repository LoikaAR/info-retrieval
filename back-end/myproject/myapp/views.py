"""
The json module contains functions related to handling HTTP requests and JSON data.
"""
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token


# def get_data(request):
#     """
#     Fetches data and returns it as a JSON response.

#     Args:
#     - request: HttpRequest object

#     Returns:
#     - JsonResponse: JSON response containing data
#     """
    # # right now, data is hardcoded!
    # if request.method == 'GET':
    #     data = [
    #         {
    #         "name": "Via Panoramica Val Bregaglia",
    #         "region": "Maloja",
    #         "category": "Hike",
    #         "distance": "14 km",
    #         "duration": "4 h 30 min",
    #         "ascent": "n/a m",
    #         "link": "https://www.myswitzerland.com/en-ch/experiences/route/via-panoramica-val-bregaglia/",
    #         "description": [
    #             "A spectacularly scenic high-level trail through the Val Bregaglia. You follow old paths through light mixed forest, over solid granite slabs and always with views of mighty granite spikes touching the sky on the other side of the valley.",
    #             "A clear autumn morning, shortly after the Malojapass, picturesque surroundings: the gold and dark green of the conifers contrasting with the deep-blue of the sky and snow-white of the summits. Before you lies the Sentiero Panoramico Val Bregaglia, a fantastic high-Alpine hike through one of Switzerland's most remote valleys.",
    #             "It soon becomes clear that you are hiking on historic paths. The first sign is the 200-year-old ramp on the Roman \u00abMal\u00f6gin\u00bb trading route. Shortly afterwards you cross the monumental Gothic walls of the S. Gaudenzio church ruins. At the beginning some of the unmistakeable hallmarks of civilization succeed in diverting you: the pass road, the mighty dam on the Albigna reservoir, the power lines suspended through the valley like silver threads. But then you enter the silent world of an extensive mixed forest. The path scales the sunny south slope of the valley to become a high-level trail.",
    #             "At the half-way stage, Alp Durbegia makes an inviting spot to stop, offering tranquil isolation and a spectacular panorama. Opposite, enormous granite spikes soar into the sky: the summit of the Sciora group and the Piz Badile - your constant companions on this high-level trail - exude an air of eternity. Equally solid, the granite slabs that pave the path, cross water courses and lead down skilfully-laid steps towards the valley. The silhouettes of the stone roofs in Soglio reveal themselves in the evening sun. The destination is a museum-like village with the history-steeped Hotel Palazzo and exquisite chestnut specialities, or to quote the artist Segantini: \u00abthe threshold to paradise\u00bb.",
    #             "You\u2019ll find one of Europe\u2019s most beautiful chestnut forests above Castasenga, not far from Soglio. The ",
    #             "\u00a0shares interesting facts about the diversity of chestnuts and their cultivation."
    #         ],
    #         "docno": 0
    #     },
    #     {
    #         "name": "Vier-Seen-Wanderung",
    #         "region": "Engelberg",
    #         "category": "Hike",
    #         "distance": "15 km",
    #         "duration": "4 h 35 min",
    #         "ascent": "n/a m",
    #         "link": "https://www.myswitzerland.com/en-ch/experiences/route/vier-seen-wanderung/",
    #         "description": [
    #             "Fabulous mountain scenery around mighty Mount Titlis, unique flora, the crystal-clear waters of Lakes Melch, Tannen, Engstlen and Tr\u00fcb \u2013 this route linking Melchsee-Frutt and Engelberg is justly rated as one of the classic high-altitude hikes.",
    #             "The Melchsee-Frutt cable car station is the starting point for the so-called \u00abfour-lake hike\u00bb. First you walk to Melchsee - the sparkling natural reservoir - where fishing is becoming quite popular. Take a peek inside the chapel, which is often booked for weddings. Then it's on to Lake Tannen, where you can grill your lunch and have a picnic on a covered patio.",
    #             "It's just a bit farther up to Tannalp, and then it's back down again to the beautiful Engstlensee - which is full of fish. Beforehand, you can sample local cheese at the dairy. This area is a place of power - especially near the tall rock that stands next to a pine tree. The ascent to the Joch pass starts near the lake. You can have a snack at the mountain lodge before heading to the fourth lake - Tr\u00fcbsee - on the other side of the mountain.",
    #             "You can discover Tr\u00fcbsee's beauty by rowboat, before heading on to Engelberg."
    #         ],
    #         "docno": 1
    #     }
    #     ]
    #     request.data = data

    #     return JsonResponse(data, safe=False)
    # else:
    #     return JsonResponse({'error': 'Invalid request method'}, status=400)
    # return JsonResponse({'message': 'Data added to request body successfully'})


def get_data(request):
    """
    Fetches data and returns it as a JSON response.

    Args:
    - request: HttpRequest object

    Returns:
    - JsonResponse: JSON response containing data
    """
    data = [
        {
            "name": "Via Panoramica Val Bregaglia",
            "region": "Maloja",
            "category": "Hike",
            "distance": "14 km",
            "duration": "4 h 30 min",
            "ascent": "n/a m",
            "link": "https://www.myswitzerland.com/en-ch/experiences/route/via-panoramica-val-bregaglia/",
            "description": [
                "A spectacularly scenic high-level trail through the Val Bregaglia. You follow old paths through light mixed forest, over solid granite slabs and always with views of mighty granite spikes touching the sky on the other side of the valley.",
                "A clear autumn morning, shortly after the Malojapass, picturesque surroundings: the gold and dark green of the conifers contrasting with the deep-blue of the sky and snow-white of the summits. Before you lies the Sentiero Panoramico Val Bregaglia, a fantastic high-Alpine hike through one of Switzerland's most remote valleys.",
                "It soon becomes clear that you are hiking on historic paths. The first sign is the 200-year-old ramp on the Roman \u00abMal\u00f6gin\u00bb trading route. Shortly afterwards you cross the monumental Gothic walls of the S. Gaudenzio church ruins. At the beginning some of the unmistakeable hallmarks of civilization succeed in diverting you: the pass road, the mighty dam on the Albigna reservoir, the power lines suspended through the valley like silver threads. But then you enter the silent world of an extensive mixed forest. The path scales the sunny south slope of the valley to become a high-level trail.",
                "At the half-way stage, Alp Durbegia makes an inviting spot to stop, offering tranquil isolation and a spectacular panorama. Opposite, enormous granite spikes soar into the sky: the summit of the Sciora group and the Piz Badile - your constant companions on this high-level trail - exude an air of eternity. Equally solid, the granite slabs that pave the path, cross water courses and lead down skilfully-laid steps towards the valley. The silhouettes of the stone roofs in Soglio reveal themselves in the evening sun. The destination is a museum-like village with the history-steeped Hotel Palazzo and exquisite chestnut specialities, or to quote the artist Segantini: \u00abthe threshold to paradise\u00bb.",
                "You\u2019ll find one of Europe\u2019s most beautiful chestnut forests above Castasenga, not far from Soglio. The ",
                "\u00a0shares interesting facts about the diversity of chestnuts and their cultivation."
            ],
            "docno": 0
        },
        {
            "name": "Vier-Seen-Wanderung",
            "region": "Engelberg",
            "category": "Hike",
            "distance": "15 km",
            "duration": "4 h 35 min",
            "ascent": "n/a m",
            "link": "https://www.myswitzerland.com/en-ch/experiences/route/vier-seen-wanderung/",
            "description": [
                "Fabulous mountain scenery around mighty Mount Titlis, unique flora, the crystal-clear waters of Lakes Melch, Tannen, Engstlen and Tr\u00fcb \u2013 this route linking Melchsee-Frutt and Engelberg is justly rated as one of the classic high-altitude hikes.",
                "The Melchsee-Frutt cable car station is the starting point for the so-called \u00abfour-lake hike\u00bb. First you walk to Melchsee - the sparkling natural reservoir - where fishing is becoming quite popular. Take a peek inside the chapel, which is often booked for weddings. Then it's on to Lake Tannen, where you can grill your lunch and have a picnic on a covered patio.",
                "It's just a bit farther up to Tannalp, and then it's back down again to the beautiful Engstlensee - which is full of fish. Beforehand, you can sample local cheese at the dairy. This area is a place of power - especially near the tall rock that stands next to a pine tree. The ascent to the Joch pass starts near the lake. You can have a snack at the mountain lodge before heading to the fourth lake - Tr\u00fcbsee - on the other side of the mountain.",
                "You can discover Tr\u00fcbsee's beauty by rowboat, before heading on to Engelberg."
            ],
            "docno": 1
        }
    ]
    request.data = data
    
    return JsonResponse(data, safe=False)


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

                # Access the specific fields (query, category, region, ascent)
                query = json_data.get('query')
                category = json_data.get('category')
                region = json_data.get('region')
                ascent = json_data.get('ascent')
                print("Received query: " + query + " " +
                      category + " " + region + " " + ascent)

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
