import json
from collections import Counter

# path will be weird
with open('./myapp/terrier_utils/parsed.json', 'r', encoding='utf-8') as file:
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


def obj_distance_parser(obj_distance):
    res = obj_distance.split(' ')
    numeric_value = res[0].replace(',', '.')

    if numeric_value != 'n/a':
        return float(numeric_value)
    return 0.0


def apply_category_filter(category, region, min_dist, max_dist):
    res = []
    with open('../../front-end/public/ordered_json_file.json', 'r', encoding='utf-8') as file:
        df = json.load(file)
    chosen_cat = chosen_categories(category)

    for obj in df:
        is_category = len(category) == 0 or obj["category"] in chosen_cat
        is_region = len(region) == 0 or obj["region"] == region
        is_distance = False

        distance_value = obj_distance_parser(obj["distance"])
        if min_dist == 0:
            if max_dist == 0:
                is_distance = True
            else:
                is_distance = distance_value <= max_dist
        if min_dist > 0:
            if max_dist == 0:
                is_distance = distance_value >=  min_dist
            else:
                is_distance = max_dist >= distance_value >=  min_dist


        if is_category and is_region and is_distance:
            res.append(obj)

    with open('../../front-end/public/ordered_json_file.json', 'w', encoding='utf-8') as file:
        json.dump(res, file, indent=4, default=str)
