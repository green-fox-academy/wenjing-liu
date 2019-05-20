from book import Book, BOOK_TYPE
from bookshelf import Bookshelf


def test():
  book_1 = Book('The Back Page: 40 Years of Crime Fiction', 'Bill Ott', 1997, 250, BOOK_TYPE['HARDCOVER'])
  book_2 = Book('The Year’s Best Crime Novels: 2019', 'Bill Ott', 2019, 200, BOOK_TYPE['PAPERBACK'])
  book_3 = Book('Top 10 Crime Fiction for Youth: 2019', 'Maggie Reagan', 2020, 300, BOOK_TYPE['PAPERBACK'])

  bookshelf = Bookshelf()
  bookshelf.add_book(book_1)
  bookshelf.add_book(book_2)
  bookshelf.add_book(book_3)
 
  print('Who is the author of the lightest book?')
  print(bookshelf.the_lightest_book_author())

  print('Which author wrote the most pages?')
  print(bookshelf.the_most_pages_book_author())


test()
