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

# def apply_category_filter(category, region):
#     res = []
#     with open('ordered_json_file.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     filter = chosen_categories(category)
#     for obj in data:
#         if obj["category"] in filter:
#             res.append(obj)
#     with open('ordered_json_file.json', 'w', encoding='utf-8') as file:
#         json.dump(res, file, indent=4, default=str)


# def apply_region_filter(region):
#     res = []
#     with open('ordered_json_file.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     for obj in data:
#         if obj["region"] == region:
#             res.append(obj)
#     with open('ordered_json_file.json', 'w', encoding='utf-8') as file:
#         json.dump(res, file, indent=4, default=str)

def apply_category_filter(category, region, min_dist, max_dist):
    res = []
    with open('ordered_json_file.json', 'r', encoding='utf-8') as file:
        df = json.load(file)
    chosen_cat = chosen_categories(category)

    for obj in df:
        is_category = False
        is_region = False
        is_distance = False
        if obj["category"] in chosen_cat or len(category) == 0:
            is_category = True
        if len(region) == 0 or obj["region"] == region:
            is_region = True
        # if len(min_dist) == 0 and len(max_dist) == 0:
        #     is_distance = True
        # if len(min_dist) == 0 and
        if is_region and is_category:
            res.append(obj)

    with open('ordered_json_file.json', 'w', encoding='utf-8') as file:
        json.dump(res, file, indent=4, default=str)
