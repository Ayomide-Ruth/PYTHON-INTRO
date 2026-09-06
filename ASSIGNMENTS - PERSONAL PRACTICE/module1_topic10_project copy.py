from module1_topic10_project_functions import add_book, borrow_book, return_book, display_catalogue

library_list = []

# Enter a name for the library using the input() function
library_ = input("Enter the name of the library: ").title()
available_ = True

def add_book(library, title, author, available = True):
    book = {"Library": library_, "Book Title": title_,"Author": author_, "Available" : available_}
    library_list.append(book)
    return (library_list)

# Ask for 4 books
for i in range(4):
    title_ = input("What is the title of the book? ").title()
    author_ = input("Who is the author of the book? ").title()
    library_list = add_book(library_, title_, author_, available = True)

print(library_list)

book_borrow_ = input("What book do you want to borrow?").title()
book_borrow = borrow_book(library_, book_borrow_)
book_borrow_count = 0
while book_borrow_count < 3:
    print (book_borrow)
    book_borrow_count += 1

# print(book_borrow)