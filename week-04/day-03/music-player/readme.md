### Music Player

Create a CLI application to manage a music library. The application should be
capable to store/remove/list and play songs. Each song has an artist and title
as well as a status (whether it is currently played or not)

#### Add a song

When the application is running you can add a song by the `a` command with any
of the following syntaxes

```
>>> a Ed Sheeran: I Don't care
>>> a Ed Sheeran, I Don't care
>>> a --artist "Ed Sheeran" --title "I Don't care"
```

#### Listing available songs

You should list the songs with the following command.

```
l                // it will list all the songs
l  --artist "Ed" // it should list all the songs which belongs to an artist who's name contains "Ed"
l  "Ed"          // it should list all the songs who's has the title or artist contains "Ed"
```

The listing should print the song's `id` as well

#### Delete a song

Songs should be deleted with the `d` command

```
d 2 // should remove the song with the id of 2
```

#### Play a song

Playing a song requires the `p` command and a song can be played by it's id
or by the same syntax as it was added to the database. Do not forget that only
one song can be played in the same time. So you have to stop the previous one
before you would start a new one.

[CRUD-tutorial]: https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/
[SELECT-tutorial]: https://pynative.com/python-postgresql-select-data-from-table/
[tips-and-tricks]: https://pynative.com/useful-python-tips-and-tricks-every-programmer-should-know/