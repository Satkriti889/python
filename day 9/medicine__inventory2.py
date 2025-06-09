import datetime
import streamlit as st

class Medicine:
    def __init__(self, name, batch, quantity, expiry, supplier, purchase, price):
        self.name = name
        self.batch = batch
        self.quantity = quantity
        self.expiry = expiry  
        self.supplier = supplier
        self.purchase = purchase  
        self.price = price

    def __str__(self):
        return (f"{self.name} | Batch: {self.batch} | Qty: {self.quantity} | "
                f"Expiry: {self.expiry} | Supplier: {self.supplier} | "
                f"Purchased: {self.purchase} | Price: ${self.price:.2f}")

class Inventory:
    def __init__(self):
        if 'medicines' not in st.session_state:
            st.session_state.medicines = []

    def add_medicine(self, med):
        st.session_state.medicines.append(med)

    def find_medicine(self, name, batch):
        for med in st.session_state.medicines:
            if med.name.lower() == name.lower() and med.batch == batch:
                return med
        return None

    def dispense_medicine(self, name, batch, qty):
        med = self.find_medicine(name, batch)
        if med and qty <= med.quantity:
            med.quantity -= qty
            return True, f"Dispensed {qty} units of {med.name}. Remaining: {med.quantity}"
        elif med:
            return False, f"Not enough stock. Available: {med.quantity}"
        else:
            return False, "Medicine not found."

    def get_inventory(self):
        return st.session_state.medicines

    def check_low_stock(self, threshold=10):
        return [m for m in st.session_state.medicines if m.quantity <= threshold]

    def check_near_expiry(self, days=30):
        today = datetime.date.today()
        return [m for m in st.session_state.medicines if 0 <= (m.expiry - today).days <= days]

    def search_medicine(self, keyword):
        keyword = keyword.lower()
        return [m for m in st.session_state.medicines if keyword in m.name.lower()]

inventory = Inventory()

st.title("Medicine Inventory Management")

menu = st.sidebar.selectbox("Menu", ["Add Medicine", "Dispense Medicine", "View Inventory", 
                                     "Check Low Stock", "Check Near Expiry", "Search Medicine"])

if menu == "Add Medicine":
    st.header("Add New Medicine")
    with st.form("add_form"):
        name = st.text_input("Medicine name")
        batch = st.text_input("Batch number")
        quantity = st.number_input("Quantity", min_value=0, step=1)
        expiry = st.date_input("Expiry date")
        purchase = st.date_input("Purchase date")
        supplier = st.text_input("Supplier name")
        price = st.number_input("Price", min_value=0.0, format="%.2f")

        submitted = st.form_submit_button("Add Medicine")
        if submitted:
            if not name or not batch:
                st.error("Please enter medicine name and batch number.")
            else:
                med = Medicine(name, batch, quantity, expiry, supplier, purchase, price)
                inventory.add_medicine(med)
                st.success(f"Medicine '{name}' added successfully!")

elif menu == "Dispense Medicine":
    st.header("Dispense Medicine")
    name = st.text_input("Medicine name")
    batch = st.text_input("Batch number")
    qty = st.number_input("Quantity to dispense", min_value=1, step=1)
    if st.button("Dispense"):
        success, msg = inventory.dispense_medicine(name, batch, qty)
        if success:
            st.success(msg)
        else:
            st.error(msg)

elif menu == "View Inventory":
    st.header("Current Inventory")
    meds = inventory.get_inventory()
    if meds:
        for med in meds:
            st.write(med)
    else:
        st.info("Inventory is empty.")

elif menu == "Check Low Stock":
    st.header("Medicines Low in Stock")
    threshold = st.number_input("Stock threshold", min_value=0, value=10, step=1)
    low_stock = inventory.check_low_stock(threshold)
    if low_stock:
        for med in low_stock:
            st.write(med)
    else:
        st.info(f"No medicines with stock ≤ {threshold}.")

elif menu == "Check Near Expiry":
    st.header("Medicines Near Expiry")
    days = st.number_input("Days until expiry", min_value=1, value=30, step=1)
    near_expiry = inventory.check_near_expiry(days)
    if near_expiry:
        for med in near_expiry:
            st.write(med)
    else:
        st.info(f"No medicines expiring within {days} days.")

elif menu == "Search Medicine":
    st.header("Search Medicines")
    keyword = st.text_input("Enter medicine name keyword")
    if keyword:
        results = inventory.search_medicine(keyword)
        if results:
            for med in results:
                st.write(med)
        else:
            st.info("No medicines found.")

