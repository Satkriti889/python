import csv
transactions=[]

def load_transactions(transactions.csv):
    try:
        with open(transactions.csv, 'r') as file:
            reader = transactions.csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        print("File not found, starting empty.")
        return []
    except Exception as e:
        print("Error reading file:", e)
        return []

def save_transactions(file_path, transactions):
    try:
        with open(file_path, 'w', newline='') as file:
            writer = transactions.writer(file)
            writer.writerow(['Date', 'Type', 'Category', 'Amount', 'Description'])
            writer.writerows(transactions)
    except Exception as a:
        print("Error saving file:", a)
