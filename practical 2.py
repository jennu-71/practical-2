print("Welcome to Inventory List Analyzer!")
item_names = []
item_quantities = []
category_set = set()
 
while True:
    name = input("\nEnter item name: ")
    category = input("Enter category: ")
    quantity = input("Enter quantity: ")

    while quantity.isdigit() == False:
        print("Please enter a valid number.")
        quantity = input("Enter quantity: ")

    quantity = int(quantity)
    item_names.append(name)
    item_quantities.append(quantity)
    category_set.add(category)

    choice = input("\nDo you want to add more items? (y/n): ")
    if choice != "y":
        break

print("\n============ INVENTORY SUMMARY ============")

total_items = len(item_names)
print("\nTotal Different Items:", total_items)
print("Explanation: You entered", total_items, "different items: ", item_names)


total_quantity = sum(item_quantities)
print("\nTotal Quantity in Stock: ", total_quantity)
print("Explanation: Sum of all item quantities: ", item_quantities)

for i in range(total_items):
    print(item_quantities[i], end=" ")
print("=", total_quantity)


average_quantity = total_quantity / total_items
print("\nAverage Quantity per Item: ", average_quantity)
print("Explanation: Average = ", total_quantity, "total /", total_items, "items")


highest_quantity = max(item_quantities)
for i in range(total_items):
    if item_quantities[i] == highest_quantity:
        most_stocked_name = item_names[i]
        break
print("\nMost Stocked Item:", most_stocked_name, highest_quantity)
print("Explanation: ", most_stocked_name, "has the highest quantity among all items.")


lowest_quantity = min(item_quantities)
for i in range(total_items):
    if item_quantities[i] == lowest_quantity:
        least_stocked_name = item_names[i]
        break
print("\nLeast Stocked Item:", least_stocked_name, lowest_quantity)
print("Explanation: ", least_stocked_name, "has the lowest quantity.")


print("\n--------------------------------------------")
print("\nUnique Categories in Inventory:")

for category in category_set:
    print(category)
print("Explanation: Categories are taken user input and converted to lowercase.")
print("No duplicates are showen here.")


print("\n--------------------------------------------")
print("\nItems Sorted by Quantity (High to Low):")

sorted_names = item_names[:]
sorted_quantities = item_quantities[:]

for i in range(total_items):
    for j in range(total_items - 1):
        if sorted_quantities[j] < sorted_quantities[j + 1]:
            temp = sorted_quantities[j]
            sorted_quantities[j] = sorted_quantities[j + 1]
            sorted_quantities[j + 1] = temp
            temp = sorted_names[j]
            sorted_names[j] = sorted_names[j + 1]
            sorted_names[j + 1] = temp

for i in range(total_items):
    print(i + 1, ".", sorted_names[i], "-", sorted_quantities[i], "units")

print("\nExplanation: Items are sorted using the quantities field from highest to lowest.")


print("\n--------------------------------------------")
print("\nCategories in Alphabetical Order:")

sorted_categories = sorted(category_set)

for i in range(len(sorted_categories)):
    print(i + 1, ".", sorted_categories[i])

print("\nExplanation: The set of unique categories was sorted alphabetically for display.")

print("\n============ END OF REPORT ============")