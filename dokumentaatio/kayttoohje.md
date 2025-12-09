# Käyttöohje

Lataa projektin uusin [release](https://github.com/sandraole/ot-harjoitustyo/releases/tag/v1.0.1) 

## Asennus

### Riippuvuuksien asentaminen

Asenna riipuvuudet komennolla:

```bash
poetry install
```

### Vaadittavat alustustoimenpiteet

Suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```


## Komentorivitoiminnot

### Ohjelman käynnistäminen

Ohjelman voi käynnistää komennolla:

```bash
poetry run invoke start
```

### Ohjelman testaaminen

Ohjelman testit voidaan suorittaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuuden selvittäminen

Testikatavuusraportin voi suorittaa komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Projektin .pylintrc-tiedostossa määritellyt tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
