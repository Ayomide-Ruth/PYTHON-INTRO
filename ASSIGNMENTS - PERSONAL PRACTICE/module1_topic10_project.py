from module1_topic10_project_functions import add_book, borrow_book, return_book, display_catalogue

# Create an empty library list 
library_list = []

# Enter a name for the library using the input() function
library_ = input("Enter the name of the library: ").title()

# Ask for 4 books
for i in range(4):
    title_ = input("What is the title of the book? ").title()
    author_ = input("Who is the author of the book? ").title()
    library_list = add_book(library_, title_, author_, available = True)
    
# Create a library with 4 books by calling the add_book function
print(library_list)

# Borrow 2 books
borrowed_books = []
for i in range (2):
    book_borrow_ = input("What book do you want to borrow? ").title()
    book_borrowed = borrow_book(library_list, book_borrow_)
    print(book_borrowed)
    # To add the 2nd book that is borrowed
    # We use .append() method to add to the borrowed_books list
    borrowed_books.append(book_borrow_)


# Return 1
book_returned_ = input("What book do you want to return? ").title()
book_returned = return_book(library_list, book_returned_ )
print(book_returned)
   
# Create an empty catalogue list to store the catalogue
# library_catalogue = []
# Display the full catalogue

print("=" * 40)
print("LIBRARY CATALOGUE")
print("=" * 40)
library_catalogue = display_catalogue(library_list)
print(library_catalogue)


























# library_list = []

# # Enter a name for the library using the input() function
# library_ = input("Enter the name of the library: ").title()
# available_ = True

# def add_book(library, title, author, available = True):
#     book = {"Library": library_, "Book Title": title_,"Author": author_, "Available" : available_}
#     library_list.append(book)
#     return (library_list)

# # Ask for 4 books
# for i in range(4):
#     title_ = input("What is the title of the book? ").title()
#     author_ = input("Who is the author of the book? ").title()
#     library_list = add_book(library_, title_, author_, available = True)

# print(library_list)

# book_borrow_ = input("What book do you want to borrow?").title()
# book_borrow = borrow_book(library_, book_borrow_)
# book_borrow_count = 0
# while book_borrow_count < 3:
#     print (book_borrow)
#     book_borrow_count += 1

# # print(boo)