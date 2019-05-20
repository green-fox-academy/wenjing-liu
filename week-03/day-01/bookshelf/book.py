
BOOK_TYPE = {
  'HARDCOVER': 'HARDCOVER',
  'PAPERBACK': 'PAPERBACK'
}

class Book:
  def __init__(self, title, author, release_year, page_number, book_type = BOOK_TYPE['HARDCOVER']):
    self.id = 0
    self.author = author
    self.title = title
    self.release_year = release_year
    self.page_number = page_number
    self.book_type = book_type
    self._weight = None

  @property
  def book_type(self):
    return self._book_type
  
  @book_type.setter
  def book_type(self, value):
    if value == BOOK_TYPE['PAPERBACK']:
      self._book_type = value
    else:
      self._book_type = BOOK_TYPE['HARDCOVER']

  @property
  def weight(self):
    if self.book_type == BOOK_TYPE['HARDCOVER']:
      self._weight = self.page_number * 10 + 100
    else: 
      self._weight = self.page_number * 10 + 20
    return self._weight


  def __str__(self):
    return f'{self.author}: {self.title} ({self.release_year})'

  def check_book(self, title = None, author = None, release_year = None):
    if title and author and release_year:
      return self.title == title and self.author == author and self.release_year == release_year
    elif title and author:
      return self.title == title and self.author == author
    elif title and release_year:
      return self.title == title and self.release_year == release_year
    elif author and release_year:
      return self.author == author and self.release_year == release_year
    elif title:
      return self.title == title
    elif author:
      return self.author == author
    elif release_year:
      return self.release_year == release_year

    return False