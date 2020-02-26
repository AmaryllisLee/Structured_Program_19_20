from pymongo import MongoClient
import pprint

client = MongoClient()
db = client.huwebshop
products = db.products

#pprint.pprint((products.find_one())) # find_one : Print een doc van collection products

# Wat is de naam en prijs van het eerste product in de database
eerst_products = products.find_one()
pprint.pprint(eerst_products['name'])
pprint.pprint(eerst_products['price']['selling_price'])

# Geef de naam van het eerste product waarvan de naambegin met een 'R'
product_met_r = products.distinct('name',{'name':{'$regex':'^R'}})
pprint.pprint(product_met_r)
# Wat is de gemiddelde prijs van de producten in de database?
gemmiddelde_prijs = products.aggregate(
    [
        {'$group':
             {'_id':'$_id','avgprice':
                 {'$avg':'$price.selling_price'}
              }
         }
    ]
)
for i in gemmiddelde_prijs:
     pprint.pprint(i)

