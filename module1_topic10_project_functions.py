# Enter a name for the library using the input() function
library_ = input("Enter the name of the library: ").title()

# Create an empty library list 
library_list = []

# Enter a name for the book title and author using the input() function
# title_ = input("What is the title of the book?").title()
# author_ = input("Who is the author of the book?").title()

# Define a function named add_book(library, title, author, available=True)
# adds a book (as a dict) to the library list
# Set available to True
# available_ = True

def add_book(library, title, author, available = True):
        book = {"Library": library, "Book Title": title,"Author": author, "Available" : available}
        library_list.append(book)
        return(library_list)

for i in range(4):
  title_ = input("What is the title of the book?").title()
  author_ = input("Who is the author of the book?").title()
  add_book(library_, title_, author_, available = True)

# Define a function named search_book(library, title)
# Searches by title and returns the book dict or None
# Request user to search for a book 
book_search_ = input("What book are you looking for?").title()

# Function definition
def search_book(library, title):
    for dictionary in library_list:
        if book_search_ == dictionary.get("Book Title"):
        #dictionary.get("Book Title") == book_search_:
            return(f"Found: {book_search_}")
    else:
        return(f"{book_search_}, Not found")


# Define a function named borrow_book(library, title)
# That marks the book as unavailable if found and available; returns a status message

book_borrow_ = input("What book do you want to borrow?").title()

def borrow_book(library, title):
    for dictionary in library_list:
        if book_borrow_ == dictionary.get("Book Title"):
            if dictionary.get("Available") == True:
# To update the book availablity status and mark the book as unavailable if found and available, we use
                dictionary["Available"] = False
                return(book_borrow_, "is available to borrow")
            else:
                return (book_borrow_, "has been borrowed")
    else:
        return(book_borrow_, "is not found")
    

# Define a function named return_book(library, title) 
# marks the book as available again; returns a status message

book_return_ = input("What book are you returning?").title()

def return_book(library, title, available = True):
    for dictionary in library_list:
        if book_return_ == dictionary.get("Book Title"):
            if dictionary.get("Available") == False:
# To update the returned book availablity status and mark the book as available, we use
                dictionary["Available"] = True
                return(f"{book_return_} has been returned and is available to be borrowed.")
            else:
                if book_return_ == dictionary.get("Book Title"):
                    if dictionary.get("Available") == True:
                        return(book_return_, "was not the book borrowed")
    else:
        return (book_return_, "does not exist in the library")


# Define a function named display_catalogue(library)
# That iterates and prints all books with their availability status
library_ = "Miva"

def display_catalogue(library):
    for dictionary in library_list:
        book_name = dictionary.get("Book Title")
        book_avail = dictionary.get("Available")
        return(f"Books: {book_name} | Availability: {book_avail}")
        print(f"Books: {book_name} | Availability: {book_avail}")

display_catalogue(library_)

