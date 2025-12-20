# Testausdokumentti

Sovellusta on testattu automaattisesti yksikkö- ja integraatiotesteillä (unittest ja pytest), sekä manuaalisesti käyttöliittymän kautta.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

UserService- ja BookSevice luokkia testataan omilla testiluokilla [src/tests](https://github.com/sandraole/ot-harjoitustyo/tree/master/src/tests) hakemistossa.

Testeissä tarkistetaan:
- Uuden käyttäjän luominen ja jo olemassa olevien käyttäjien estäminen
- Kirjautuminen oikeilla ja väärillä tunnuksilla
- Kirjojen lisääminen oikeilla ja virheellisillä syötteillä
- Kirjojen luettu-tilan vaihtaminen
- Tilastojen laskeminen: kirjojen lukumäärä, luetut sivut ja luettujen sivujen prosentti

### Repositorio luokat

BookRepository luokkaa testataan käyttäen erillistä testitiedostoa.

setUp- ja tearDown metodit huolehtivat, että:
- Testitiedosto luodaan uutena jokaiselle kerralle
- Testin lopuksi tiedosto poistetaan, jotta vanha tieto ei vaikuta uusiin testeihin

Testit kattavat:
- Kirjojen lisäämisen ja poistamisen indeksin perusteella
- Kirjojen lataamisen tyhjästä/puuttuvasta tai virheellisestä JSON-tiedstosta
- Luettu-tilan vaihtamisen luetuksi ja takaisin lukemattomaksi


### Testauskattavuus

Rivikattavuus 88% ja haarautumakattavuus 71%.

![](https://github.com/sandraole/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Screenshot%20from%202025-12-20%2021-24-06.png)

Kattavuus koskee sovelluslogiikkaa (services), pysyväistallennusta (repositories) ja data/file_utils.py. Graafista käyttöliittymää ei testata automaattisesti.


## Järjestelmätestaus

Sovellusta on testattu vain Linux-ympäristössä seuraavasti:
- Projekti asennettu ohjeiden mukaan
- Riippuvuudet asennettu komennolla "poetry install"
- Sovellus käynnistetty komennolla "poetry run invoke start"


### Manuaalisesti testatus toiminnot:

- Käyttäjän luominen ja kirjautuminen
- Virheelliset syötteet kirjautuimisessa / rekisteröinnissä
- Kirjojen lisääminen ja poistaminen
- Kirjojen merkitseminen luetuksi / lukemattomaksi kaksoisklikkauksella
- Hakukenttä
- Tilastojen päivittyminen
- "Read pages" tekstin klikkaaminen
- Pylväsdiagrammin avaaminen
- Uloskirjautuminen
- Eri käyttäjillä eri listat


## Sovellukseen jääneet laatuongelmat

- Tkinteriä ei testata automaattisesti. UI-muutokset voivat rikkoa asioita, joita yksikkötestit wivät havaitse.
- matplotlib-kaavion toimivuus on testattu vain manuaalisesti.
- Ei ole testattu tilannetta, jossa matplotlib ei ole saatavilla
- Ei olla testattu virhetilanteita tiedostokäsittelyssä (puuttuvat oikeudet data-hakemsitoon)
