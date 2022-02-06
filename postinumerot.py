# Kopioi aikaisempi ratkaisusi tänne. Lisää tarvittaessa myös muut ratkaisusi tiedostot.
# Esimerkkisuoritus:
#
# Kirjoita postitoimipaikka: Porvoo
# Postinumerot: 06100, 06101, 06150, 06151, 06200, 06400, 06401, 06450, 06500

import math
import requests
import json
from typing import Optional


data1=[]
def get_numbers(postitoimipaikka: str)-> Optional[str]:
    
    response_API = requests.get('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json')
    #print(response_API.status_code)
    data = response_API.text
    realdata = json.loads(data)
   

    for postinumero, kaupunki in realdata.items():
                if postitoimipaikka.upper().replace(" ", "")==kaupunki.replace(" ", ""):
                    data1.append(postinumero)
    return data1

if __name__ == "__main__":
        etsi = input("Kirjoita postitoimipaikka: ").upper()
        name = get_numbers(etsi)
        if data1: 
            data1.sort()   
            print("Postinumerot: "), print(*data1, sep=", ")
        else:
            print("Tuntematon postitoimipaikka")
            
           
    
         
def get_one(postitoimipaikka):
    response_API = requests.get('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json')
    data = response_API.text
    realdata = json.loads(data)
    data1=[]
    
    if postitoimipaikka not in realdata.values(): 
        return ("Tuntematon postitoimipaikka")
    else:
        for postinumero, kaupunki in realdata.items():
            if postitoimipaikka==kaupunki:
                data1.append(postinumero)
                return data1

