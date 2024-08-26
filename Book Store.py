class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

def create_books():
    books = []  # List to store book objects
    
    num_books = int(input("How many books do you want to enter? "))
    
    for _ in range(num_books):
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        book = Book(title, author)  # Create a Book object
        books.append(book)  # Add the book to the list
    
    return books

def display_all_books(books):
    for book in books:
        book.display_info()

def remove_book(books, title):
    for book in books:
        if book.title == title:
            books.remove(book)
            print(f"Book titled '{title}' has been removed.")
            return
    print(f"Book titled '{title}' not found.")

def update_book_info(books, old_title, new_title, new_author):
    for book in books:
        if book.title == old_title:
            book.title = new_title
            book.author = new_author
            print(f"Book information updated to Title: '{new_title}', Author: '{new_author}'.")
            return
    print(f"Book titled '{old_title}' not found.")

# Main program
if __name__ == "__main__":
    books = create_books()
    display_all_books(books)
    
    # Remove a book
    title_to_remove = input("\nEnter the title of the book to remove: ")
    remove_book(books, title_to_remove)
    display_all_books(books)
    
    # Update book information
    old_title = input("\nEnter the title of the book to update: ")
    new_title = input("Enter the new title: ")
    new_author = input("Enter the new author: ")
    update_book_info(books, old_title, new_title, new_author)
    display_all_books(books)
