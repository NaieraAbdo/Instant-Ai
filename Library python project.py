
import tkinter as tk
from tkinter import messagebox

# Define the Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Borrowed' if self.is_borrowed else 'Available'}"

# Define the Member class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {', '.join(book.title for book in self.borrowed_books)}"

# Define the Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def get_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

    def __str__(self):
        return f"Library has {len(self.books)} books and {len(self.members)} members."

# Define the LibraryGUI class
class LibraryGUI:
    def __init__(self, library):
        self.library = library

        self.root = tk.Tk()
        self.root.title("Library Management System")

        # Add Book Frame
        self.add_book_frame = tk.Frame(self.root)
        self.add_book_frame.pack(pady=10)
        tk.Label(self.add_book_frame, text="Title").grid(row=0, column=0)
        tk.Label(self.add_book_frame, text="Author").grid(row=0, column=1)
        tk.Label(self.add_book_frame, text="ISBN").grid(row=0, column=2)
        self.title_entry = tk.Entry(self.add_book_frame)
        self.title_entry.grid(row=1, column=0)
        self.author_entry = tk.Entry(self.add_book_frame)
        self.author_entry.grid(row=1, column=1)
        self.isbn_entry = tk.Entry(self.add_book_frame)
        self.isbn_entry.grid(row=1, column=2)
        self.add_book_button = tk.Button(self.add_book_frame, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=1, column=3)

        # List Books Frame
        self.list_books_frame = tk.Frame(self.root)
        self.list_books_frame.pack(pady=10)
        self.books_listbox = tk.Listbox(self.list_books_frame, width=50)
        self.books_listbox.pack(side=tk.LEFT)
        self.view_books_button = tk.Button(self.list_books_frame, text="View Available Books", command=self.view_books)
        self.view_books_button.pack(side=tk.RIGHT)

        self.root.mainloop()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        if title and author and isbn:
            book = Book(title, author, isbn)
            self.library.add_book(book)
            messagebox.showinfo("Success", f"Book '{title}' added to the library!")
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def view_books(self):
        self.books_listbox.delete(0, tk.END)
        available_books = self.library.get_available_books()
        for book in available_books:
            self.books_listbox.insert(tk.END, str(book))

# Main script
if __name__ == "__main__":
    library = Library()
    library.add_member(Member("John Doe"))
    library.add_member(Member("Jane Smith"))
    LibraryGUI(library)
