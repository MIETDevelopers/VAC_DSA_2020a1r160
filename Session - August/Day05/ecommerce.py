# Sample product data
products = {
    'electronics': {
        'laptop': {'samsung': 1000, 'hp': 900, 'dell': 1100},
        'fridge': {'samsung': 800, 'lg': 750, 'whirlpool': 900},
        'tv': {'samsung': 1200, 'lg': 1100, 'sony': 1300}
    },
    'cosmetics': {
        'lipstick': {'mac': 20, 'maybelline': 10, 'nyx': 15},
        'foundation': {'loreal': 25, 'revlon': 20, 'covergirl': 18}
    },
    'grocery': {
        'vegetables': {'carrot': 1, 'tomato': 2, 'potato': 1.5},
        'fruits': {'apple': 2, 'banana': 1.5, 'orange': 1}
    }
}

DEFAULT_USERNAME = "user"
DEFAULT_PASSWORD = "password"

def display_categories():
    print("Available categories:")
    for category in products:
        print("- " + category)

def display_subcategories(category):
    print(f"Available subcategories under {category}:")
    for subcategory in products[category]:
        print("- " + subcategory)

def display_brands(category, subcategory):
    print(f"Available brands for {subcategory} in {category}:")
    for brand in products[category][subcategory]:
        print("- " + brand)

def main():
    print("Desi Amazon")

    username = input("Username: ")
    password = input("Password: ")

    if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
        print("Login successful.")
    else:
        print("Login failed. Exiting...")
        return

    display_categories()

    category = input("Select a category: ")
    if category not in products:
        print("Invalid category.")
        return

    display_subcategories(category)
    subcategory = input("Select a subcategory: ")
    if subcategory not in products[category]:
        print("Invalid subcategory.")
        return

    display_brands(category, subcategory)
    brand = input("Select a brand: ")
    if brand not in products[category][subcategory]:
        print("Invalid brand.")
        return

    price = products[category][subcategory][brand]
    print(f"Price for {brand} {subcategory} is ${price}")

    pin = input("Enter your PIN to confirm purchase: ")
    if pin == "1234":
        print("Purchase confirmed. Thank you!")
    else:
        print("Incorrect PIN. Purchase not confirmed.")

if __name__ == "__main__":
    main()
