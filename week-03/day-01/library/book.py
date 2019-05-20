class Book:
  def __init__(self, title, author, release_year):
    self.id = 0
    self.author = author
    self.title = title
    self.release_year = release_year

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


'''
## Book

- Book has an author, a title and a release year
- Book should have an `toString` method that returns a string in this format:
  - Douglas Adams : The Hitchhiker's Guide to the Galaxy (1979)
'''