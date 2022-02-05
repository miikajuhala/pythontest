# Kirjoita postinumerot-moduulin testit tähän tiedostoon
from postinumerot import get_numbers
from postinumerot import get_one



def test_get_numbers_multiple():
     monta = get_numbers("ESPOO")

     assert len(monta) >= 2 

def test_get_numbers_one():
    monta = get_one("ESPOO")

    assert len(monta) == 1 

def test_get_false_place():
    false = get_one("koirakissa")

    assert false=="Tuntematon postitoimipaikka"