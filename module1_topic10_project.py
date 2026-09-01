from module1_topic10_project_functions import add_book, search_book, borrow_book, return_book, display_catalogue

library_ = input("Enter the name of the library: ").title()
library_list = []

# Enter a name for the book title and author using the input() function
title_ = input("What is the title of the book?").title()
author_ = input("Who is the author of the book?").title()

add_book_ = add_book(library_, title_, author_)
print(library_list)