import streamlit as st

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance
        self.__pin = "5678"
        st.success(f"Account created for {self.owner}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            st.info(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            st.warning("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            st.warning("Withdrawal amount must be positive.")
        elif amount > self._balance:
            st.error(f"Insufficient funds. Cannot withdraw ${amount}. Balance is ${self._balance}")
        else:
            self._balance -= amount
            st.info(f"Withdrew ${amount}. New balance: ${self._balance}")

    def get_balance(self):
        st.success(f"Current balance for {self.owner}: ${self._balance}")
        st.code(f"(Internal Pin: {self.__pin})")
        return self._balance

    def get_pin(self):
        return self._BankAccount__pin


# --- Streamlit App UI ---

st.title("🏦 Simple Bank Account App")

# Account creation
owner = st.text_input("Enter account holder name:", value="")
initial_balance = st.number_input("Enter initial balance:", min_value=0, value=300)

if st.button("Create Account"):
    if 'account' not in st.session_state:
        st.session_state.account = BankAccount(owner, initial_balance)
    else:
        st.warning("Account already created. Restart app to create a new one.")

# If account exists
if 'account' in st.session_state:
    acc = st.session_state.account

    st.subheader("🔁 Actions")

    deposit_amount = st.number_input("Deposit amount", min_value=0)
    if st.button("Deposit"):
        acc.deposit(deposit_amount)

    withdraw_amount = st.number_input("Withdraw amount", min_value=0)
    if st.button("Withdraw"):
        acc.withdraw(withdraw_amount)

    if st.button("Show Balance"):
        acc.get_balance()

    if st.button("Show Internal Pin (for demo)"):
        pin = acc.get_pin()
        st.code(f"Accessed internal pin: {pin}")

    if st.button("Change Public __pin"):
        acc.__pin = "3456"
        st.warning("Public __pin changed (not the real one).")

    if st.button("Change True Private Pin"):
        acc._BankAccount__pin = "1234"
        st.info("Changed real private pin (not recommended).")
        st.code(f"New Internal Pin: {acc.get_pin()}")

    # Show direct balance access
    st.write("### Debug Info")
    st.code(f"Direct access to _balance: {acc._balance}")
