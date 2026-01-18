
from book import Book

class user():

    def __init__(self, username, password, libraryCardNumber, permissions):
      self.username = username
      self.password = password
      self.libraryCardNumber = libraryCardNumber
      self.checkedOut = []
      self.holds = []
      self.history = [] 
      self.permissions = permissions 


    def addHold(bookToPutOnHold:Book):
