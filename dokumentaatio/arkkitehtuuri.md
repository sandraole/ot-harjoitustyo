# Sovelluslogiikka

Sovelluksessa on kolmitasoinen kerrosarkkitehtuuri:
- UI-kerros näyttää Tkninter käyttöliittymän
- Sevices-kerros sisältää käyttäjiin ja kirjoihin liittyvän sovelluslogiikan
- Repositories-kerros tallentaa kirjat JSON-tiedostoihin

Käyttöliittymä kutsuu vain service-luokkia ja service-luokat hoitavat tiedostonkäsittelyn repository-luokkien kautta.

```mermaid
classDiagram
    class UserService{
        _file_path
        _users
        create_user(username, password)
        login(username, password)
        authenticate(username, password)
    }

    class BookService{
        add_book(title, author, pages_str)
        get_books()
        delete_book(index)
        toggle_book_read(index)
    }

    class BookRepository{
        _file_path
        _books
        add_book(...)
        delete_by_index(index)
        toggle_read_status(index)
        get_all()
    }

    BookService --> BookRepository
```

# Sekvenssikaavio
Kirjan lisääminen:

```mermaid
sequenceDiagram
    actor User
    participant MV as MainView
    participant BS as BookService
    participant BR as BookRepository

    User->>MV: click "Add book" (syöttää title, author, pages)
    MV->>BS: add_book(title, author, pages)

    BS->>BS: strip + validointi (tyhjät, integer, > 0)

    alt syöte virheellinen
        BS-->>MV: ValueError (virheviesti)
        MV->>User: messagebox.showerror(...)
    else syöte ok
        BS->>BR: add_book(title, author, pages)
        BR->>BR: lisää kirja listaan ja tallentaa JSON-tiedostoon
        BR-->>BS: ok
        BS-->>MV: ok

        MV->>BS: get_books()
        BS->>BR: get_all()
        BR-->>BS: lista kirjoista
        BS-->>MV: lista kirjoista
        MV->>MV: _refresh_book_list()
    end
```





