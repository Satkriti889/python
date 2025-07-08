import streamlit as st

st.title("📚 Library Management System")

# Initialize session state
if 'books' not in st.session_state:
    st.session_state.books = {}

if 'borrow_books' not in st.session_state:
    st.session_state.borrow_books = {}

# Functions
def add_books(book, quantity):
    if book in st.session_state.books:
        st.session_state.books[book] += quantity
    else:
        st.session_state.books[book] = quantity
    st.success(f"{quantity} copy/copies of '{book}' added successfully.")

def remove_books(book, quantity):
    if book in st.session_state.books:
        if st.session_state.books[book] >= quantity:
            st.session_state.books[book] -= quantity
            st.success(f"{quantity} copy/copies of '{book}' removed.")
            if st.session_state.books[book] == 0:
                del st.session_state.books[book]
        else:
            st.error(f"Cannot remove {quantity}. Only {st.session_state.books[book]} available.")
    else:
        st.error("Book not found.")

def borrow_book(book, quantity):
    if book in st.session_state.books and st.session_state.books[book] >= quantity:
        st.session_state.books[book] -= quantity
        st.session_state.borrow_books[book] = st.session_state.borrow_books.get(book, 0) + quantity
        st.success(f"{quantity} copy/copies of '{book}' borrowed.")
        if st.session_state.books[book] == 0:
            del st.session_state.books[book]
    else:
        st.warning(f"'{book}' not available in sufficient quantity.")

def return_books(book, quantity):
    if book in st.session_state.borrow_books and st.session_state.borrow_books[book] >= quantity:
        st.session_state.borrow_books[book] -= quantity
        if st.session_state.borrow_books[book] == 0:
            del st.session_state.borrow_books[book]
        st.session_state.books[book] = st.session_state.books.get(book, 0) + quantity
        st.success(f"{quantity} copy/copies of '{book}' returned.")
    else:
        st.error(f"You didn't borrow {quantity} copy/copies of '{book}'.")

def check_books():
    if st.session_state.books:
        st.subheader("Available Books:")
        for book, qty in st.session_state.books.items():
            st.write(f"📘 {book} — {qty} copy/copies")
    else:
        st.info("Library is empty.")

# Sidebar menu
menu = st.sidebar.radio("Choose Action", [
    "Add Book", "Remove Book", "Borrow Book", "Return Book", "Check Library", "Exit"
])

if menu == "Add Book":
    book = st.text_input("Enter book name")
    qty = st.number_input("Enter quantity", min_value=1, step=1)
    if st.button("Add Book"):
        if book.strip():
            add_books(book.strip(), qty)

elif menu == "Remove Book":
    book = st.text_input("Enter book name to remove")
    qty = st.number_input("Enter quantity to remove", min_value=1, step=1)
    if st.button("Remove Book"):
        if book.strip():
            remove_books(book.strip(), qty)

elif menu == "Borrow Book":
    book = st.text_input("Enter book name to borrow")
    qty = st.number_input("Enter quantity to borrow", min_value=1, step=1)
    if st.button("Borrow Book"):
        if book.strip():
            borrow_book(book.strip(), qty)

elif menu == "Return Book":
    book = st.text_input("Enter book name to return")
    qty = st.number_input("Enter quantity to return", min_value=1, step=1)
    if st.button("Return Book"):
        if book.strip():
            return_books(book.strip(), qty)

elif menu == "Check Library":
    check_books()

elif menu == "Exit":
    st.balloons()
    st.success("Thank you for using the Library Management System!")
