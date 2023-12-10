import json
from collections import Counter

with open('./parsed.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def get_categories():
    categories = []
    for obj in data:
        if obj["category"] not in categories:
            categories.append(obj["category"])
    return categories


# print(get_categories())


def get_top_10_regions():
    regions = [item['region'] for item in data]

    # Count occurrences of each region
    region_counts = Counter(regions)

    regions = region_counts.most_common(10)

    res = [region[0] for region in regions]
    return res


print(get_top_10_regions())


def get_top_10_categories():
    categories = [obj['category'] for obj in data]

    # Count occurrences of each region
    cat_counts = Counter(categories)

    # return cat_counts.most_common(28)
    categories = cat_counts.most_common(5)

    res = [cat[0] for cat in categories]
    return res

# print(get_top_10_categories())
