print("Welcome to the Inventory Management System")

inventory = []

n = int(input("How many items do you want to add ? "))
for i in range(n):
    item = input(f"Enter item {i + 1}: ").strip()
    inventory.append(item)

while True:
    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Check inventory")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter item to add: ").strip()
        inventory.append(item)
        print("Item added.")

    elif choice == '2':
        item = input("Enter item to remove: ").strip()
        if item in inventory:
            inventory.remove(item)
            print("Item removed.")
        else:
            print("Item not found in inventory.")

    elif choice == '3':
        if inventory:
            print(f"There are {len(inventory)} item(s): {inventory}")
        else:
            print("Inventory is empty.")

    elif choice == '4':
        print("Thanks for using the inventory system!")
    

    else:
        print("Invalid choice. Please enter 1 to 4.")
