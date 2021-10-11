import feedparser
from pprint import pprint
from operator import itemgetter

def create_url(product, suburb, region, brand, surrounding, stateregion, day):
    url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?'
    if product:  #Expected 1 ULP, 2 Premium, 3 Diesel, 4 LPG
        url += 'Product=' + str(product) + '&'
    if suburb:  #Expected BALCATTA, BEDFORD, ROCKINGHAM
        url += 'Suburb=' + str(suburb) + '&'
    if region:  #Expected 25 Metro North, 26 Metro South
        url += 'Region=' + str(region) + '&'
    if brand:  #Expected 7 Gull, 2 Ampol, 5 bp, 6 Caltex
        url += 'Brand=' + str(brand) + '&'
    if surrounding:  #Expected yes, no - to include surrounding suburbs
        url += 'Surrounding=' + str(surrounding) + '&'
    if stateregion:  #Expected 7 Pilbara, 98 Metro, 1 Gascoyne
        url += 'Stateregion=' + str(stateregion) + '&'
    if day:  #Expected today, tomorrow - only after 2.30pm, yesterday
        url += 'Day=' + str(day) + '&'

    return url

def get_data(url):
    data = feedparser.parse(url)
#    pprint(data)
    return data['entries']

url = create_url(1, "BALCATTA", 0, 0, 0, 0, "today")
today_prices = get_data(url)
#print(today_prices)
url = url.replace("today","tomorrow")
tomorrow_prices = get_data(url)
#print(tomorrow_prices)
fuel_list=[]

for i in today_prices:  #Loop through the entries
    price = float(i['price'])
    suburb = i['location']
    address = i['address']
    date = i['date']
    temp_dict={'price':price, 'suburb':suburb,'address':address,'date':date}
    fuel_list.append(temp_dict)

for i in tomorrow_prices:  #Loop through the entries
    price = float(i['price'])
    suburb = i['location']
    address = i['address']
    date = i['date']
    temp_dict={'price':price, 'suburb':suburb,'address':address,'date':date}
    fuel_list.append(temp_dict)

#new_list = sorted(fuel_list, key=lambda k: k['price'], reverse=False)
new_list = sorted(fuel_list, key=itemgetter('price'), reverse=False)

if(not(new_list)):
    print("Error")  # Realised we had no error handling - maybe put something here later?
else:
#    print(new_list)
    pprint(new_list)
# We now have a sorted list, with all entries being dictionaries composed of price, suburb etc
# What else can we do? Can compare to the cheapest fuel in Australia..