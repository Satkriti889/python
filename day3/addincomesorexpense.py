import csv
import os
from datetime import datetime

filename = "transactions.csv"

if os.path.isfile(filename)!=True:
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Type", "Amount", "Category"])

def is_valid_name(name):
    return name.isalpha()

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_string(category):
    return category.isalpha()


def add_expense():
    while True:
        name = input("Enter your name: ")
        if is_valid_name(name)!= True:
            print("Invalid name. Please enter letters only.\n")
            continue

        date = input("Enter date (YYYY-MM-DD): ")
        if is_valid_date(date)!= True:
            print("Invalid date format. Please use YYYY-MM-DD.\n")
            continue

        amount_str = input("Enter expense amount: ")
        try:
            amount = float(amount_str)
            if amount < 0:
                print("Amount cannot be negative.\n")
                continue
        except ValueError:
            print("Invalid amount. Please enter a number.\n")
    
            continue

        category = input("Enter expense category: ")
        if is_valid_string(category)!=True:
            print("Invalid category. Please enter letters only.\n")
            continue

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, date, "Expense", amount, category])
        print("Expense recorded successfully!\n")
        break

def show_total_expense():
    person_name = input("Enter the name to calculate total expense: ")
    if is_valid_name(person_name)!= True:
        print("Invalid name. Please enter letters only.\n")
        return

    total_expense = 0.0

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name, _, trans_type, amount, _ = row
            if trans_type == "Expense" and name.lower() == person_name.lower():
                total_expense += float(amount)

    print(f"\n Your total expense is {total_expense}\n")

def main():
    while True:
        print("Choose an option:")
        print("1. Add Expense")
        print("2. Show Total Expense")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_total_expense()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
