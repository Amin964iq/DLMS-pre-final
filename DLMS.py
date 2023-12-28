import json


# Class representing a Book
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def to_dict(self):
        return {"book_id": self.book_id, "title": self.title, "author": self.author}

# Class representing a Digital Library Management System
class DLMS:
    def __init__(self):
        self.books = []

    def load_books(self, filename):
        # Load books from a JSON file
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.books = [Book(**book_data) for book_data in data]
        except FileNotFoundError:
            print("File not found. Starting with an empty library.")

    def save_books(self, filename):
        # Save books to a JSON file
        data = [book.to_dict() for book in self.books]
        with open(filename, 'w') as file:
            json.dump(data, file, inde6nt=2)

    def add_book(self, book_id, title, author):
        # Add a new book to the library and sort the books by ID
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        self.books = sorted(self.books, key=lambda x: x.book_id)

    def find_book_by_id(self, book_id):
        # Find a book by its ID using linear search
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_books_by_name(self, name):
        # Find books by name using case-insensitive search
        result = [book for book in self.books if name.lower() in book.title.lower()]
        return result

    def update_book_info(self, book_id, title, author):
        # Update book information (title and author)
        for book in self.books:
            if book.book_id == book_id:
                book.title = title
                book.author = author
                break

def print_book(book):
    # Print book information
    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

def main():
    dlms = DLMS()
    dlms.load_books('books.json')  # Load existing data if any

    while True:
        print("\nDigital Library Management System\n")
        print("1. Add a new book")
        print("2. Find a book by ID")
        print("3. Find books by name")
        print("4. Update book information")
        print("5. Display all books")
        print("6. Save and exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Add a new book
            book_id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            dlms.add_book(book_id, title, author)
            print("Book added successfully!")

        elif choice == '2':
            # Find a book by ID
            book_id = int(input("Enter book ID to search: "))
            book = dlms.find_book_by_id(book_id)
            if book:
                print_book(book)
            else:
                print("Book not found.")

        elif choice == '3':
            # Find books by name
            name = input("Enter book name to search: ")
            books = dlms.find_books_by_name(name)
            if books:
                for book in books:
                    print_book(book)
            else:
                print("No books found with that name.")

        elif choice == '4':
            # Update book information
            book_id = int(input("Enter book ID to update: "))
            book = dlms.find_book_by_id(book_id)
            if book:
                title = input("Enter new title (press Enter to keep the existing title): ")
                author = input("Enter new author (press Enter to keep the existing author): ")
                dlms.update_book_info(book_id, title, author)
                print("Book information updated successfully!")
            else:
                print("Book not found.")

        elif choice == '5':
            # Display all books
            if dlms.books:
                for book in dlms.books:
                    print_book(book)
            else:
                print("No books in the library.")

        elif choice == '6':
            # Save and exit
            dlms.save_books('books.json')  # Save data before exiting
            print("Library data saved. Exiting.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
