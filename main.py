import csv
import json

# Predefined Categories
CATEGORIES = {
    "Travel": ["flight", "vacation", "hotel", "trip", "tour"],
    "Finance": ["loan", "insurance", "investment", "credit", "bank"],
    "Retail": ["sale", "discount", "shop", "store", "product"],
    "Food": ["restaurant", "delivery", "menu", "cuisine", "dish"],
}


# Categorization Logic
def categorize_ad(ad, categories):
    matched_categories = set()
    text = (ad['title'] + " " + ad['description'] + " " + " ".join(ad['keywords'])).lower()

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in text:
                matched_categories.add(category)
                break

    return list(matched_categories)


# Load Ads from CSV
def load_ads_from_csv(filename):
    ads = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ads.append({
                "title": row['title'],
                "description": row['description'],
                "keywords": [kw.strip() for kw in row['keywords'].split(',')]
            })
    return ads


# Save Results to JSON
def save_to_json(data, filename):
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


# Main
if __name__ == "__main__":
    ads = load_ads_from_csv("ads.csv")

    for ad in ads:
        ad['categories'] = categorize_ad(ad, CATEGORIES)

    save_to_json(ads, "categorized_ads.json")
    print("✅ Ads have been categorized and saved to 'categorized_ads.json'")
