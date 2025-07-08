import streamlit as st

# Define the BankAccount class
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance
        self.__pin = "5678"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        elif amount > self._balance:
            return f"Insufficient funds. Cannot withdraw ${amount}. Balance is ${self._balance}"
        else:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"

    def get_balance(self):
        return f"Current balance for {self.owner}: ${self._balance} (PIN: {self.__pin})"

    def get_pin(self):
        return self._BankAccount__pin

    def change_pin(self, new_pin):
        if new_pin:
            self._BankAccount__pin = new_pin
            return f"PIN changed successfully to {new_pin}"
        return "Invalid PIN entry."

# Session state initialization
if 'account' not in st.session_state:
    st.session_state.account = None

st.title("🏦Bank Account Management System")

# Account creation
if st.session_state.account is None:
    st.subheader("🔐 Create Account")
    owner = st.text_input("Enter your name")
    initial_balance = st.number_input("Initial Balance", min_value=0, step=100)

    if st.button("Create Account"):
        st.session_state.account = BankAccount(owner, initial_balance)
        st.success(f"Account created for {owner} with balance ${initial_balance}")
else:
    acc = st.session_state.account
    st.success(f"Welcome, {acc.owner}!")

    menu = st.sidebar.radio("Select Action", [
        "💰 Deposit", "💸 Withdraw", "📊 Check Balance", "🔑 Show/Change PIN"
    ])

    if menu == "💰 Deposit":
        st.subheader("Deposit Money")
        deposit_amt = st.number_input("Amount to deposit", min_value=1)
        if st.button("Deposit"):
            msg = acc.deposit(deposit_amt)
            st.success(msg)

    elif menu == "💸 Withdraw":
        st.subheader("Withdraw Money")
        withdraw_amt = st.number_input("Amount to withdraw", min_value=1)
        if st.button("Withdraw"):
            msg = acc.withdraw(withdraw_amt)
            st.success(msg) if "Withdrew" in msg else st.error(msg)

    elif menu == "📊 Check Balance":
        st.subheader("Account Balance")
        st.info(acc.get_balance())

    elif menu == "🔑 Show/Change PIN":
        st.subheader("PIN Management")
        if st.checkbox("Show PIN"):
            st.code(acc.get_pin())
        new_pin = st.text_input("Enter new PIN to change it")
        if st.button("Change PIN"):
            result = acc.change_pin(new_pin)
            st.success(result)

    if st.button("❌ Close Account"):
        st.session_state.account = None
        st.warning("Account closed. Refresh to start over.")
