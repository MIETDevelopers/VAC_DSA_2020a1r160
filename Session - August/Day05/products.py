products = {
    'electronics': {
        'laptops': {'samsung': 1000, 'HP': 900, 'dell': 1100},
        'fridge': {'samsung': 800, 'LG': 750, 'whirlpool': 900},
        'TV': {'samsung': 1200, 'LG': 1100, 'sony': 1300}
    },
    'Cosmetics': {
        'Skincare': {'cetaphil': 20, 'minimilist': 10, 'ordinary': 15},
        'Makeup': {'loreal': 25, 'revlon': 20, 'covergirl': 18}
    },
    'Groceries': {
        'vegetables': {'carrot': 1, 'tomato': 2, 'potato': 1.5},
        'fruits': {'apple': 2, 'banana': 1.5, 'orange': 1}
    }
}

def login():
    valid_email = "abc@gmail.com"
    valid_password = "password"
    
    entered_email = input("Enter your email: ")
    entered_password = input("Enter your password: ")
    
    if entered_email == valid_email and entered_password == valid_password:
        print("Login successful!")
    else:
        print("Invalid credentials. Please try again.")


def show_products():
    print("Available categories:")
    for category in products:
        print("- " + category)

def show_sub_products(category):
    print(f"Available subcategories under {category}:")
    for subproduct in products[category]:
        print("- " + subproduct)
    
def show_brand(subproduct, category):
    print(f"Available brands for {subproduct} in {category}:")
    for brand in products[category][subproduct]:
        print("- " + brand)
        
def main():
    login()

    show_products()
    
    category = input("Select a category: ")
    if category not in products:
        print("Invalid category.")
        return
    
    show_sub_products(category)
    subproduct = input("Select a subcategory: ")
    if subproduct not in products[category]:
        print("Invalid subcategory.")
        return

    show_brand(subproduct,category)
    brand = input("Select a brand: ")
    if brand not in products[category][subproduct]:
        print("Invalid brand.")
        return

    price = products[category][subproduct][brand]
    print(f"Price for {brand} {subproduct} is ${price}")

    otp = input("Enter your OTP to confirm purchase: ")
    if otp == "1234":
        print("Purchase confirmed. Thank you!")
    else:
        print("Incorrect OTP. Purchase not confirmed.")


if __name__ == "__main__":
    main()

