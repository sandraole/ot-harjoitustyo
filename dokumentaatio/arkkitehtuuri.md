# Sovelluslogiikka

Sovelluksen alustava logiikka --> tarkentuu toiminnallisuuden lisääntyessä

```mermaid
 classDiagram
      UserService "*" --> "1" User
      class User{
          username
          password
      }
      class UserService{
          file_path
          users
      }
```

# Sekvenssikaavio

```mermaid
sequenceDiagram
    actor User
    participant MV as MainView
    participant BS as BookService
    participant BR as BookRepository

    User->>MV: click "Add book"\n(syöttää title, author, pages)
    MV->>BS: add_book(title, author, pages_str)

    BS->>BS: strip + validointi\n(tyhjät, integer, > 0)

    alt syöte virheellinen
        BS-->>MV: ValueError (virheviesti)
        MV->>User: messagebox.showerror(...)
    else syöte ok
        BS->>BR: add_book(title, author, pages)
        BR->>BR: lisää kirja listaan\nja tallentaa JSON-tiedostoon
        BR-->>BS: ok
        BS-->>MV: ok

        MV->>BS: get_books()
        BS->>BR: get_all()
        BR-->>BS: lista kirjoista
        BS-->>MV: lista kirjoista
        MV->>MV: _refresh_book_list()
    end
```


