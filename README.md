# Budjetointisovellus

Tämä on yksinkertainen budjetointisovellus, jonka avulla käyttäjät voivat seurata tuloja ja menoja eri ajanjaksoilta – viikoittain, kuukausittain tai vuositasolla. Sovellus tukee useita käyttäjiä, joista jokaisella on oma henkilökohtainen tili ja budjettiseuranta.

## Dokumentaatio

- [Vaatimusmaarittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)

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
