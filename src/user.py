
from book import Book
from pydantic import BaseModel
from catalog import *

class User(BaseModel):
    username: str
    email: str | None = None
    name: str | None = None

    def __init__(self, username, password, libraryCardNumber, permissions):
      self.username = username
      self.password = password
      self.libraryCardNumber = libraryCardNumber
      self.checkedOut = []
      self.holds = []
      self.history = [] 
      self.permissions = permissions 


    def addHold(self, bookToPutOnHold:Book):
       if (bookToPutOnHold not in set(self.holds)):   
         self.holds.append(bookToPutOnHold)

         try:
           print("Attempting to add hold...")
           #TODO: connect to database and add hold record
           print("the book " + bookToPutOnHold.title + " has been put on hold")
      

         except Exception as e:
            print("An error occurred while adding hold to the database: ", e)
       else:
         print("the book " + bookToPutOnHold.title + " is already on hold")
          

    def checkout(self, bookToCheckout:Book):
       
       self.checkedOut.append(bookToCheckout)