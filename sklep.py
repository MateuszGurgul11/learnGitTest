shoppingList = {
    "piekarnia" : ['Chleb', 'Pączek', 'Bułki'],
    "warzywniak" : ['Marchew', 'Seler', 'Rukola']
}

for shop, item in shoppingList.items():
    shop = shop.capitalize()
    print(f"Ide do {shop} i kupie tam {item}")

    allItems = len(item) + len(item)

print(f"W sumie kupuję {allItems} produktów")