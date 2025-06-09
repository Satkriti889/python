import os
import datetime

class MedicineInventory:
    def __init__(self):
        self.medicines = []
        self.log_file = "medicine_log"
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write("Medicine Inventory Log Started\n")

    def log(self, action, name, qty=None):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if qty is not None:
            entry = f"[{time}] {action} - {name} Qty: {qty}\n"
        else:
            entry = f"[{time}] {action} - {name}\n"
        with open(self.log_file, 'a') as f:
            f.write(entry)
        print(f"Log saved: {entry.strip()}")

    def add_medicine(self):
        name = input("Medicine name: ").strip()
        expiry_str = input("Expiry date (YYYY-MM-DD): ").strip()
        quantity = input("Quantity: ").strip()
        price = input("Price: ").strip()

        try:
            expiry = datetime.datetime.strptime(expiry_str, "%Y-%m-%d").date()
            quantity = int(quantity)
            price = float(price)
        except:
            print("Invalid input. Try again.")
            return

        self.medicines.append({
            'name': name,
            'expiry': expiry,
            'quantity': quantity,
            'price': price
        })
        print(f"Added medicine: {name}")
        self.log("ADD", name, quantity)

    def dispense_medicine(self):
        name = input("Medicine name: ").strip()
        for med in self.medicines:
            if med['name'].lower() == name.lower() and med['quantity'] > 0:
                qty = input("Quantity: ").strip()
                if qty.isdigit():
                    qty = int(qty)
                    if qty <= med['quantity']:
                        med['quantity'] -= qty
                        print(f"Dispensed {qty} of {med['name']}. Left: {med['quantity']}")
                        self.log("DISPENSE", med['name'], qty)
                    else:
                        print("Not enough stock.")
                else:
                    print("Invalid quantity.")
                return
        print("Medicine not found or out of stock.")

    def check_near_expiry(self):
        today = datetime.date.today()
        found = False
        for med in self.medicines:
            days_left = (med['expiry'] - today).days
            if med['quantity'] > 0 and 0 <= days_left <= 30:
                if not found:
                    print("Medicines expiring soon:")
                    found = True
                print(med['name'], "Expiry:", med['expiry'], "Qty:", med['quantity'])
        if not found:
            print("No medicines expiring soon.")

    def check_low_stock(self):
        threshold = 10
        low_stock = [m for m in self.medicines if 0 < m['quantity'] <= threshold]

        if low_stock:
            print("Low stock medicines:")
            for med in low_stock:
                print(med['name'], "-", med['quantity'])
        else:
            print("No medicines with low stock.")

    def view_logs(self):
        if os.path.exists(self.log_file):
            print("\nMedicine Inventory Logs:")
            with open(self.log_file, 'r') as f:
                print(f.read())
        else:
            print("No logs found.")

def main():
    inventory = MedicineInventory()

    while True:
        print("\nMenu:")
        print("1. Add Medicine")
        print("2. Dispense Medicine")
        print("3. Check Near Expiry")
        print("4. Check Low Stock")
        print("5. View Logs")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            inventory.add_medicine()
        elif choice == '2':
            inventory.dispense_medicine()
        elif choice == '3':
            inventory.check_near_expiry()
        elif choice == '4':
            inventory.check_low_stock()
        elif choice == '5':
            inventory.view_logs()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
