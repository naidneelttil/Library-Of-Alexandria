from enum import Enum
class Book:

    def __init__(self, title, author, isbn):
      self.title = title
      self.author = author
      self.isbn = isbn
      self.copies = 1



class BookStatus(Enum):
    CheckedOut = 1
    Availible = 2
    OnHold = 3
