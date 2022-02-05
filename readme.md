# Yksikkötestaus Pytest-työkalulla

Näissä tehtävissä harjoittelemme koodin refaktorointia ja yksikkötestausta kirjoittamalla testejä aikaisemmin koodatulle `postinumerot.py`-skriptille (edellisen viikon tehtävän 2. osa).

Mikäli aikaisempi tehtävä jäi sinulta palauttamatta tai et halua käyttää vanhaa koodiasi, voit käyttää myös tehtävän malliratkaisun tiedostoja, jotka löydät Teams-kanavalta tehtävän umpeutumisen jälkeen.


## Pytest-asennus

Tässä tehtävässä tarvittavan Pytest-työkalun asennus onnistuu esimerkiksi seuraavasti:

```
$ pip3 install pytest
```

GitHub classroomissa on valmiiksi käytettävissä sekä Pytest että [pytest-mock](https://pypi.org/project/pytest-mock/). Voit halutessasi käyttää myös muita Python-paketteja, mutta lisää ne `requirements.txt`-tiedostoon, jotta ne asennetaan myös classroom-ympäristöön.


## GitHub classroom

Tehtävät arvostellaan käyttäen [GitHub classroom](https://classroom.github.com/) -palvelua, joka suorittaa komentosi, ja tarkastaa ja pisteyttää niiden tulokset automaattisesti. Taustalla GitHub classroom hyödyntää [GitHub actions](https://github.com/features/actions) -nimistä jatkuvan integroinnin palvelua.

Voit tarvittaessa yrittää tehtäviä monta kertaa. Tee tällöin uusi commit, ja vie muutokset uudelleen GitHubiin.


## Harjoitusten kloonaaminen

Kun olet hyväksynyt tehtävän GitHub classroomissa ja saanut repositoriosta henkilökohtaisen kopion, kloonaa se itsellesi `git clone` -komennolla.

Kloonatessasi repositoriota varmista, että Git-osoitteen lopussa on oma GitHub-käyttäjänimesi. Jos käyttäjänimesi puuttuu osoitteesta, kyseessä ei ole henkilökohtainen kopiosi tehtävästä. Luo tässä tapauksessa oma repositorio tämän linkin kautta: https://classroom.github.com/a/OSFhaNxa.


## Osa 1: postinumerot_test.py (3 pistettä)

Kopioi tähän `postinumerot.py`-tiedostoon edellisen viikon Python-tehtävän osan 2 ratkaisusi. Mikäli kyseinen tehtävä jäi sinulta toteuttamatta, voit käyttää testattavana koodina tehtävän malliratkaisua.

Kirjoita seuraavaksi `postinumerot_test.py`-tiedostoon Pytest-yksikkötestit ohjelmallesi. Sinun ei tarvitse testata koko ohjelmalogiikkaa, vaan riittää, että testaat esimerkiksi yksittäisen funktion. Lisäksi joudut todennäköisesti refaktoroimaan aikaisempaa ratkaisuasi siten, että sen testaaminen on ylipäänsä mahdollista.

Testeissä varmista ainakin seuraavien tapausten toiminta:

1. postitoimipaikan nimellä löytyy vain yksi postinumero
1. postitoimipaikan nimellä löytyy useita postinumeroita
1. postitoimipaikan nimellä ei löydy lainkaan postinumeroita.

Testien suorittaminen onnistuu seuraavalla komennolla:

```
$ python3 -m pytest
```

Muista lisätä mahdolliset uudet tiedostot versionhallintaan `git add`- ja `git commit`-komennoilla.

Saadaksesi täydet pisteet tästä osasta **sinun ei tarvitse** testata syötteitä pyytäviä tai tulosteita tekeviä kohtia koodista. Voit oman harkintasi mukaan käyttää testeissä joko kovakoodattua testidataa tai antaa testattavan koodin lukea postinumeroaineiston verkosta tai levyltä. Testiaineiston käyttämisessä `pytest-mock` voi olla avuksi, mutta sitä **ei ole välttämätöntä käyttää**.



## Osa 2: Bugin korjaus ja testaus (2 pistettä)

Postin aineistossa smart post -automaatit esiintyvät sekä nimellä "smart post" että "smartpost". Ohjelmasi toimintaa tulee muuttaa siten, että se löytää kaikki smart post -automaatit riippumatta siitä, esiintyykö niiden nimessä välilyöntiä. Lisää testeihisi myös testitapaukset, jotka osoittavat tekemäsi muutoksen toimivan.

Ohjelman käyttöliittymän tulee toimia samalla tavoin, kuin [edellisessä tehtävässä](https://github.com/harjoitukset/python-postalcodes).

Bugin korjauksessa voi olla avuksi, jos poistat kaikki välilyönnit [Pythonin replace-funktiolla](https://stackoverflow.com/questions/9452108/how-to-use-string-replace-in-python-3-x).

Esimerkkisuoritus:

```
$ python3 postinumerot.py 
Kirjoita postitoimipaikka: smart post
Postinumerot: 00104, 00124, 00134, 00144, ..., 40934, ... 99304, 99604, 99804, 99834, 99874, 99944, 99954, 99994
```
