# Book Tracker

Book Tracker on henkilökohtainen lukupäiväkirja, jonka avulla käyttäjä voi seurata lukemiaan kirjoja ja omaa lukemisen edistymistään. Käyttäjä voi lisätä kirjoja listalle, merkitä ne luetuiksi sekä tarkastella tilastoja luetuista kirjoista ja sivuista.

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Release](https://github.com/sandraole/ot-harjoitustyo/releases/tag/v2.0.0)

[Käyttöohje](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Asennus

### Riippuvuuksien asentaminen

Asenna riipuvuudet komennolla:

```bash
poetry install
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
