# Käyttöohje

Lataa projektin uusin [release](https://github.com/sandraole/ot-harjoitustyo/releases/tag/v2.0.0).

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

## Kirjautuminen
Sovellus käynnistyy kirjautumisnäkymään. Käyttäjä voi joko kirjautuaolemassa olevalla tunnuksella tai luoda uuden käyttäjän painamalla "Register".

![](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202025-12-20%2020-19-05.png)

## Uuden käyttäjän luominen
Rekisteröintinäkymässä käyttäjä voi luoda uuden tunnuksen tai palata takaisin kirjautumisnäkymään. Onnistuneen rekisteröitymisen jälkeen sovellus palauttaa käyttäjän Login sivulle.

![](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202025-12-20%2020-19-39.png)

## Oma kirjalista
Kirjalistanäkymässä käyttäjä voi:
- Lisätä uusia kirjoja
- Poistaa valitun kirjan
- Etsiä kirjoja hakukentällä kirjan nimen tai kirjailijan mukaan
- Merkitä kirjan luetuksi tai lukemattomaksi kaksoisklikkaamalla sitä listassa
- Tarkastella luettuja ja lukemattomia sivuja pylväsdiagrammina painamalla "Show reading chart"
- Nähdä luettujen ja lukemattomien kirjojen määrän
- Vaihtaa luettujen sivujen esitystapaa klikkaamalla "Read pages" tekstiä (näkyy joko sivumääränä tai prosenttiosuutena)
- Kirjautua ulos painamalla "Logout"

![](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202025-12-20%2020-21-09.png)









