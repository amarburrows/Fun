class Book:
    """Represent a titled book written by a single author"""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author



def selection_sort_books(books: list[Book]) -> list[Book]:
    for i in range(len(books)):
        books_min = i
        for j in range(i, len(books)):
            if books[j].title < books[books_min].title:
                books_min = j

        temp = books[i]
        books[i] = books[books_min]
        books[books_min] = temp

    return books



# Input: A string
# Output: Returns a string
# Data Representation: String

def swap_case(phrase: str) -> str:
    swapped = ""
    for letter in phrase:
        if letter.isalpha():
            if letter.isupper():
             swapped += letter.lower()
            else:
                swapped += letter.upper()
    return swapped


# Input: A string
# Output: Returns a modified string
# Data Representation: String

def str_translate(phrase: str, letter_1: str, letter_2: str) -> str:
    modified = ''
    for letter in phrase:
        if letter == letter_1:
            modified += letter_2
        else:
            modified += letter
    return modified
