import json
from urllib.request import urlopen

#url = "tähänurl"
#response = urlopen(url)
#data = json.loads(response.read())
#ylläoleva on toimiva reaaliaikaisen haun lämpötilan suhteen, mutta testiä varten käytetään alempaa jottei kysytä liian usein säätä

saa = json.dumps({"coord":{"lon":25.75,"lat":62.25},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":269.15,"pressure":1014,"humidity":100,"temp_min":269.15,"temp_max":269.15},"visibility":10000,"wind":{"speed":2.82,"deg":238.003},"clouds":{"all":0},"dt":1490482200,"sys":{"type":1,"id":5025,"message":0.0095,"country":"FI","sunrise":1490414304,"sunset":1490460506},"id":655195,"name":"Jyväskylä","cod":200})
data = json.loads(saa)
lampo = data['main']['temp'] - 273.15

print("Jyväskylän lämpötila on nyt %s C"%(lampo))


