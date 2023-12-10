import json
from collections import Counter

with open('./parsed.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def get_all_categories():
    categories = []
    for obj in data:
        if obj["category"] not in categories:
            categories.append(obj["category"])
    return categories


# print(get_all_categories())


def get_top_5_regions():
    regions = [item['region'] for item in data]

    # Count occurrences of each region
    region_counts = Counter(regions)

    regions = region_counts.most_common(5)

    res = [region[0] for region in regions]
    return res


# print(get_top_10_regions())


def get_top_categories():
    categories = ['Hikes', 'Mountain Activities', 'Adventures', 'City Sightseeing']
    return categories

# print(get_top_10_categories())


def chosen_categories(queriedCat):
    res = []
    # Hiking and Trails
    if queriedCat == 'Hikes':
        res = ['Hike', 'Hiking trail', 'Theme trail', 'Trail running',
                'Multi-day hike', 'Via Ferrata', 'Trekking']
    # Mountain Activities
    elif queriedCat == 'Mountain Activities':
        res = ['Mountain biking', 'Winter hiking', 'Sledging', 'Skitouring',
                'Mountain trail', 'Alpine trail', 'Alpine climbing', 'Alpine tour']
    # Other Activities and Adventure
    elif queriedCat == 'Adventures':
        res = ['Cross-country skiing', 'Jogging', 'Cycling', 'Adventure', 'Scenic Views', 'Water']

    # Culture and Sightseeing including Parks
    elif queriedCat == 'City Sightseeing':
        res = ['City walking tour', 'Specialties',
               'Cities & Monuments', 'Museums', 'Villages', 'Parks']

    return res
