from book import Book

class Bookshelf:
  def __init__(self):
    self.book_list = []

  def add_book(self, book):
    if not isinstance(book, Book):
      raise Exception('You must input book in the shelf')
    for index in range(len(self.book_list)):
      if self.book_list[index].check_book(title = book.title, author = book.author, release_year = book.release_year):
        raise Exception('The book already existing')
    
    book.id = len(self.book_list)
    self.book_list.append(book)
  
  def remove_book_by_title(self, book_title):
    for index in range(len(self.book_list)):
      if self.book_list[index].check_book(title = book_title):
        return self.book_list.pop(index)
    return False
  
  def favourite_author(self): 
    authors = {}
    for index in range(len(self.book_list)):
      book = self.book_list[index]
      authors[book.author] = authors.get(book.author, 0) + 1
    
    return sorted(authors, key = lambda author: author)[-1]
  
  def earliest_published(self):
    if len(self.book_list):
      return sorted(self.book_list, key = lambda book: book.release_year)[0].__str__()
    else:
      return 'The shelf is empty'
  
  def latest_published(self):
    if len(self.book_list):
      return sorted(self.book_list, key = lambda book: book.release_year)[-1].__str__()
    else:
      return 'The shelf is empty'
  
  def the_lightest_book_author(self):
    if len(self.book_list):
      return sorted(self.book_list, key = lambda book: book.weight)[0].author
    else:
      return 'The shelf is empty'
  
  def the_most_pages_book_author(self):
    if len(self.book_list):
      return sorted(self.book_list, key = lambda book: book.page_number, reverse = True)[0].author
    else:
      return 'The shelf is empty'
  
  def __str__(self):
    return f'There are {len(self.book_list)} books in the shelf, the earliest book is {self.earliest_published() } and the latest released book is {self.latest_published()}, and the favourite author is {self.favourite_author()}'