import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

key = "Enter your API key"  #Geocoder API key need to paste here
num = input('Enter a number with country code:')
new_num = phonenumbers.parse(num)
location = geocoder.description_for_number(new_num,"en")
print(location)

service_name = carrier.name_for_number(new_num,"en")
print(service_name)

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

my_map = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(my_map)

my_map.save('lcn.html')

print('location tracking complete')
print('Thank you')