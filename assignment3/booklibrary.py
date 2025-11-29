# book_library.py

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN  : {self.isbn}")
        print(f"Status: {self.status}")

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            print("Book issued.")
        else:
            print("Book is already issued.")

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            print("Book returned.")
        else:
            print("Book is already available.")

    def to_record(self):
        # convert details to one line to save in text file
        return f"{self.title}|{self.author}|{self.isbn}|{self.status}\n"


def save_book_to_file(book, filename="library.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(book.to_record())
        print("Book saved to file.")
    except OSError:
        print("Error while writing to file.")


def load_books_from_file(filename="library.txt"):
    books = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    title, author, isbn, status = parts
                    books.append(Book(title, author, isbn, status))
    except FileNotFoundError:
        # file not created yet – just return empty list
        pass
    except OSError:
        print("Error while reading file.")
    return books


def find_book_by_isbn(isbn, books):
    for b in books:
        if b.isbn == isbn:
            return b
    return None


def main():
    books = load_books_from_file()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add new book")
        print("2. View all books")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")

            new_book = Book(title, author, isbn)
            books.append(new_book)
            save_book_to_file(new_book)

        elif choice == 2:
            if not books:
                print("No books in library.")
            else:
                for b in books:
                    print("-" * 20)
                    b.display()

        elif choice == 3:
            isbn = input("Enter ISBN of book to issue: ")
            book = find_book_by_isbn(isbn, books)
            if book:
                book.issue()
                # rewrite whole file with updated statuses
                try:
                    with open("library.txt", "w", encoding="utf-8") as f:
                        for b in books:
                            f.write(b.to_record())
                except OSError:
                    print("Error updating file.")
            else:
                print("Book not found.")

        elif choice == 4:
            isbn = input("Enter ISBN of book to return: ")
            book = find_book_by_isbn(isbn, books)
            if book:
                book.return_book()
                try:
                    with open("library.txt", "w", encoding="utf-8") as f:
                        for b in books:
                            f.write(b.to_record())
                except OSError:
                    print("Error updating file.")
            else:
                print("Book not found.")

        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
