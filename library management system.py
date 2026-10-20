class Library:
    def __init__(self, book_list):
        self.books = book_list

    def display_books(self):
        """Displays all available books in the library."""
        print("\n--- Available Books ---")
        if not self.books:
            print("No books currently available in the library.")
        else:
            for index, book in enumerate(self.books, 1):
                print(f"{index}. {book}")

    def borrow_book(self, book_name):
        """Allows a user to borrow a book if it's available."""
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Success! You have borrowed '{book_name}'. Enjoy reading!")
        else:
            print(f"Sorry, '{book_name}' is either not available or does not exist.")

    def add_book(self, book_name):
        """Allows adding a new book to the library collection."""
        self.books.append(book_name)
        print(f"Success! '{book_name}' has been added to the library.")

    def return_book(self, book_name):
        """Allows a user to return a borrowed book."""
        self.books.append(book_name)
        print(f"Thank you for returning '{book_name}'.")


def main():
    # Initial collection of books
    initial_books = ["Python Crash Course","Data Structures and Algorithms","Clean Code","The Pragmatic Programmer"]
    
    my_library = Library(initial_books)

    while True:
        print("="*30)
        print(" LIBRARY MANAGEMENT SYSTEM ")
        print("="*30)
        print("1. Display Available Books")
        print("2. Borrow a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Exit")
        print("-"*30)
        
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            my_library.display_books()
            
        elif choice == '2':
            book = input("Enter the exact name of the book you want to borrow: ").strip()
            my_library.borrow_book(book)
            
        elif choice == '3':
            book = input("Enter the name of the new book you want to add: ").strip()
            my_library.add_book(book)
            
        elif choice == '4':
            book = input("Enter the name of the book you are returning: ").strip()
            my_library.return_book(book)
            
        elif choice == '5':
            print("\nThank you for using the Library Management System. Goodbye!")
            break
            
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
