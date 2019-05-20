from book import Book
from bookshelf import Bookshelf


def test():
  book_1 = Book('The Back Page: 40 Years of Crime Fiction', 'Bill Ott', 1997)
  book_2 = Book('The Year’s Best Crime Novels: 2019', 'Bill Ott', 2019)
  book_3 = Book('Top 10 Crime Fiction for Youth: 2019', 'Maggie Reagan', 2020)

  bookshelf = Bookshelf()
  bookshelf.add_book(book_1)
  bookshelf.add_book(book_2)
  bookshelf.add_book(book_3)
  print(bookshelf)
  bookshelf.remove_book_by_title('The Year’s Best Crime Novels: 2019')
  print(bookshelf)


test()
