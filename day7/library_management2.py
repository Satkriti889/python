print("----Welcome to Library Management System---- ")

class Library:
    def __init__(self):
        self.books = {}         
        self.borrow_books = {}   

    def add_books(self, book, quantity):
        if book in self.books:
            self.books[book] += quantity
        else:
            self.books[book] = quantity
        print(f"{quantity} copy/copies of '{book}' added successfully.")

    def remove_books(self, book, quantity):
        if book in self.books:
            if self.books[book] >= quantity:
                self.books[book] -= quantity
                print(f"{quantity} copy/copies of '{book}' removed.")
                if self.books[book] == 0:
                    del self.books[book]
            else:
                print(f"Cannot remove {quantity} copy/copies. Only {self.books[book]} available.")
        else:
            print("The book is not found.")

    def borrow_book(self, book, quantity):
        if book in self.books and self.books[book] >= quantity:
            self.books[book] -= quantity
            self.borrow_books[book] = self.borrow_books.get(book, 0) + quantity
            print(f"{quantity} copy/copies of '{book}' borrowed.")
            if self.books[book] == 0:
                del self.books[book]
        else:
            print(f"'{book}' is not available in sufficient quantity to borrow.")

    def return_books(self, book, quantity):
        if book in self.borrow_books and self.borrow_books[book] >= quantity:
            self.borrow_books[book] -= quantity
            if self.borrow_books[book] == 0:
                del self.borrow_books[book]
            self.books[book] = self.books.get(book, 0) + quantity
            print(f"{quantity} copy/copies of '{book}' returned.")
        else:
            print(f"You did not borrow {quantity} copy/copies of '{book}' from this library.")

    def check_books(self):
        if self.books:
            print("Available books in library:")
            for book, qty in self.books.items():
                print(f"{book} - {qty} copy/copies")
        else:
            print("Library is empty.")

library = Library()

while True:
    print("\nMenu:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Check Library")
    print("6. Exit")

    try:
        choice = int(input("Enter the number according to your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 6.")
        continue

    if choice == 1:
        try:
            num = int(input("How many different books do you want to add? "))
        except ValueError:
            print("Invalid Number")
            num = 0
        for i in range(num):
            book = input(f"Enter the name of book {i+1}: ")
            try:
                qty = int(input(f"Enter the quantity for '{book}': "))
            except ValueError:
                print("Invalid quantity, defaulting to 1.")
                qty = 1
            library.add_books(book, qty)

    elif choice == 2:
        book = input("Enter the book you want to remove: ")
        try:
            qty = int(input(f"Enter the quantity to remove for '{book}': "))
        except ValueError:
            print("Invalid quantity, defaulting to 1.")
            qty = 1
        library.remove_books(book, qty)

    elif choice == 3:
        book = input("Enter the book you want to borrow: ")
        try:
            qty = int(input(f"Enter the quantity to borrow for '{book}': "))
        except ValueError:
            print("Invalid quantity, defaulting to 1.")
            qty = 1
        library.borrow_book(book, qty)

    elif choice == 4:
        book = input("Enter the book you want to return: ")
        try:
            qty = int(input(f"Enter the quantity to return for '{book}': "))
        except ValueError:
            print("Invalid quantity, defaulting to 1.")
            qty = 1
        library.return_books(book, qty)

    elif choice == 5:
        library.check_books()

    elif choice == 6:
        print("...Thank You...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
