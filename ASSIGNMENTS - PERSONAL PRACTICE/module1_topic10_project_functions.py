# Create an empty list
library_list = []

# Define a function named add_book(library, title, author, available=True)
# adds a book (as a dict) to the library list

def add_book(library, title, author, available = True):
    book = {"Library": library, "Book Title": title,"Author": author, "Available" : available}
    library_list.append(book)
    return (library_list)

# Mr. Ayub solution
# def add_book(library, title, author, available = True):
#    library_list = []
#    library_list.append({"Library": library, "Book Title": title,"Author": author, "Available" : available})
#    return library_list

# Define a function named search_book(library, title)
# Searches by title and returns the book dict or None
# Request user to search for a book 
# Function definition

def search_book(library, title):
    for dictionary in library:
        if title == dictionary.get("Book Title"):
            return(f"Found: {title}")
    else:
        return(f"{title}, Not found")


# Define a function named borrow_book(library, title)
# That marks the book as unavailable if found and available; returns a status message

def borrow_book(library, title):
    for dictionary in library_list:
        if title == dictionary.get("Book Title"):
            if dictionary.get("Available") == True:
# To update the book availablity status and mark the book as unavailable if found and available, we use
                dictionary["Available"] = False
                return(title, "is available to borrow")
            else:
                return (title, "has been borrowed")
    else:
        return(title, "is not a book in the library")


# Define a function named return_book(library, title) 
# marks the book as available again; returns a status message

def return_book(library, title):
    for dictionary in library:
        if title == dictionary.get("Book Title"):
            if dictionary.get("Available") == False:
# To update the returned book availablity status and mark the book as available, we use
                dictionary["Available"] = True
                return(f"{title} has been returned and is available to be borrowed.")
            elif dictionary.get("Available") == True:
                return(title, "was not the book borrowed")
    else:
        return (title, "does not exist in the library")


# Define a function named display_catalogue(library)
# That iterates and prints all books with their availability status

def display_catalogue(library):
    library_catalogue = []
    for dictionary in library:
        book_name = dictionary.get("Book Title")
        author = dictionary.get("Author")
        book_avail = dictionary.get("Available")
        library_catalogue.append(f"Books: {book_name} | Author: {author} | Availability: {book_avail}")
    return(library_catalogue)

# Rule: Do not put return inside a loop when you want the loop to process every item in a list.
# Return implies that I am through with this function

