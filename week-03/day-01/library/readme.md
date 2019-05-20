# Library

You are going to create a simple library where you can store books in a
bookshelf.

## Book

- Book has an author, a title and a release year
- Book should have an `toString` method that returns a string in this format:
  - Douglas Adams : The Hitchhiker's Guide to the Galaxy (1979)

## Bookshelf

- Bookshelf has a list of books in it
- It must be able to add books to the bookshelf
- It must be able to remove books from the bookshelf
- It must have a `favouriteAuthor` method which must be able to return who has
  written the most books in the shelf
- It must have a `earliestPublished` method which must be able to return the
  earliest published book.
- It must have a `latestPublished` method which must be able to return the
  latest published book.
- It must have a `toString` method which give us information about the number of
  books, the earliest and the latest released books, and the favourite author.