# Book Tracker - Vaatimusmäärittely

## Sovelluksen tarkoitus

Book Tracker on henkilökohtainen lukupäiväkirja, jonka avulla käyttäjä voi seurata lukemiaan kirjoja ja omaa lukemisen edistymistään. Käyttäjä voi lisätä kirjoja listalle, merkitä ne luetuiksi sekä tarkastella tilastoja luetuista kirjoista ja sivuista.

### Käyttäjät

Sovelluksessa on yksi käyttäjärooli: normaali käyttäjä.
Useita käyttäjätunnuksia voidaan luoda, ja jokaisella käyttäjällä on oma, erillinen kirjalistansa.

### Käyttöliittymä

Sovellus koostuu kolmesta näkymästä:̈́
- Login - kirjautuminen sovellukseen tai siirtyminen rekisteröitymiseen
- Register - uuden käyttäjätunnuksne luominen
- Main - kirjautuneen käyttäjän oma kirjalista ja tilastot

Sovellus käynnistyy "Login" näkymään ja onnistuneen kirjautumisen jälkeen käyttäjä siirtyy omaan kirjalista näkymään.

## Perusversion toiminnallisuudet

### Ennen kirjautumista

- Käyttäjä voi luoda uuden käyttäjätunnuksen
  - Käyttäjätunnuksen on oltava uusi
  - Käyttäjän täytyy antaa käyttäjätunnus ja salasana, tyhjiä kenttiä ei hyväksytä
- Käyttäjä voi kirjautua sisään jo olemassa olevilla tunnuksilla
  - Jos käyttäjätunnusta ei ole tai se on väärä, sovellus näyttää virheilmoituksen

### Kirjautumisen jälkeen

Käyttäjä näkee oman kirjalistansa. Toiminnot:
- **Kirjan lisääminen**
  - Käyttäjä voi lisätä uuden kirjan antamalla:
    - nimen (title)
    - kirjailijan (author)
    - sivumäärän (pages)
  - Sivumäärän tulee olla positiivinen kokonaisluku, muuten tulee virheilmoitus
- **Kirjojen listaus ja luettu-tila**
  - Käyttäjä näkee omat kirjat kahdessa listassa:
    - Unread books
    - Read books
  - Käyttäjä voi kaksoisklikkaamalla kirjaa merkitä kirjan luetuksi ja päinvastoin
- **Kirjan poistaminen**
  - Käyttäjä voi poistaa valitun kirjan "Delete selected book" napilla
  - Poistamista edeltää varmistkysymys
- **Haku**
  - Käyttäjä voi hakea kirjoja hakukentällä
  - Kirjaa haetan kirjan tai kirjailijan nimellä
  - Jos kirjaa ei löydy, tulee virheilmoitus
- **Tilastot**
  - Käyttäjä näkee oikeasta alakulmasta tilastot:
    - luettujen kirjojen määrä
    - kaikkien kirjojen määrä
    - luettujen sivujen määrä ja prosenttiosuus kaikista sivuista
  - "Read pages" linkkiä painamalla käyttäjä voi vaihtaa näkymää:
    - prosenttiosuus
    - sivumäärä
- **Pylväsdiagrammi (matplotlib)**
  - Käyttäjä voi painamalla nappia "Show reading chart" avata pylväsdiagrammin, jossa näkyy:
    - luettujen sivujen määrä
    - lukemattomien sivujen määrä
- **Uloskirjautuminen**
  - Käyttäjä voi kirjautua ulos, jolloin sovellus palaa "Login" näkymään
  - Eri käyttäjien kirjalistat ovat erillisiä ja tallentuvat käyttäjäkohtaisiin tiedostoihin
 
## Tiedon tallennus

- Käyttäjien kirjautumistiedot tallennetaan JSON-tiedostoon
- Jokaisen käyttäjän kirjalista tallennetaan erilliseen JSON-tiedostoon ja tiedot säilyvät ohjelman sulkemisen jälkeen
- Tiedostot luodaan automaattisesti, jos niitä ei vielä ole

## Jatkokehitysideat

Seuraavia toiminnallisuuksia ei ole vielä toteutettu, mutta ne olisi mahdollista lisätä myöhemmin:
- Kirjojen lajittelu kirjailijan, nimen tai sivumäärän mukaan
- Mahdollisuus arvostella luettu kirja
- Lukemistavoitteen asettaminen
- Useampi käyttäjärooli, joilla erilaiset oikeudet
- Kirjojen tietojen muokkaaminen jälkikäteen



