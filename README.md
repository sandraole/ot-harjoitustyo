# Book Tracker

Book Tracker on sovellus, jonka avulla käyttäjä voi seurata lukemiaan kirjoja ja omia lukutavoitteitaan. Käyttäjä voi lisätä kirjoja lukulistalle, merkitä kirjoja luetuiksi sekä seurata luettujen kirjojen ja sivujen määrää. 

Sovelluksen tarkoituksena on motivoida käyttäjää lukemaan enemmän ja toimia muistilistana jo luetuista kirjoista.

### Koodikatselmointi
Toivoisin erityisesti palautetta ja parannusehdotuksia koodin laatuun ja rakenteeseen. Tiedostan, että tällä hetkellä tieotojen tallentaminen synnyttää kaksi data kansiota. Src kansion ulkopuolinen data kansio on se ei toivottu. Tämä on työn alla.

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Release](https://github.com/sandraole/ot-harjoitustyo/releases/tag/v1.0.0)

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
