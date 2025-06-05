print("----Welcome to Library Management System---- ")
class Library:

    def __init__(self):
        self.books=[]
        self.borrow_books=[]


    def add_books(self,book):
        self.books.append(book)
        print("The book is added successfully.")

    def remove_books(self,book):
        if book in self.books:
            self.books.remove(book)
            print("Book has been deleted")
        else:
            print("The book is not fouund")

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.borrow_books.append(book)
            print(f"'{book}' has been borrowed.")
        else:
            print(f"'{book}' is not available or already borrowed.")

    def return_books(self, book):
        if book in self.borrow_books:
            self.borrow_books.remove(book)
            self.books.append(book)
            print(f"'{book}' has been returned and is now available.")
        else:
            print(f"'{book}' was not borrowed from this library.")


    def check_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("Library is empty.")

library=Library()

while True:
    print("\nMenu:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Check Library")
    print("6. Exit")

    choice=int(input("Enter the number according to your choice:"))

    if choice==1:
        try:
            num=int(input("How many book do you want to add initially?  "))
        except ValueError:
            print("Invalid Number")
            num=0
        for i in range(num):
            book=input(f"Enter the book{i+1}: ")
            library.add_books(book)

    elif choice==2:
        book =input("Enter the book which you want to remove : ")
        library.remove_books(book)

    elif choice==3:
        borrowed_book=input("Enter the book you want to borrow : ")
        library.borrow_book(borrowed_book)
    elif choice==4:
            return_book=input("Enter the book you want to return : ")
            library.return_books(return_book)

    elif choice==5:
       library.check_books()

    elif choice==6:
        print("...Thank You...")
        break
    else:
        print("Invalid choice please enter the number from 1 to 4 : ")

