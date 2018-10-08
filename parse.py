# parse.py

from bs4 import BeautifulSoup
import re

raw_html = open("locations.html").read()
html = BeautifulSoup(raw_html,'html.parser')

class Location():
    def __init__(self, i):
        self.id = i
        self.name = ""
        self.addr = ""
        self.addr2 = ""
        self.city = ""
        self.state = ""
        self.postal = ""
        self.latlong = (0, 0)

locations = []

for entry in html.select('tr'):
    fields = _, i, name, addr, addr2, city, state, postal, blank, lat = [td.text.strip() for td in entry.select('td')]
    loc = Location(i)
    loc.name = name
    loc.addr = addr
    loc.addr2 = addr2
    loc.city = city
    loc.state = state
    loc.postal = postal
    loc.latlong = eval(lat)
    print(loc.latlong)
    locations.append(loc)

output = "["

for e in locations:
    output += "\n  {"
    output += '\n    "id": "'+e.id+'",'
    output += '\n    "name": "'+e.name.title()+'",'
    output += '\n    "lat": "'+str(e.latlong[0])+'",'
    output += '\n    "lng": "'+str(e.latlong[1])+'",'
    output += '\n    "category": "grocery",'
    output += '\n    "address": "'+e.addr+'",'
    output += '\n    "address2": "'+e.addr2+'",'
    output += '\n    "city": "'+e.city+'",'
    output += '\n    "state": "'+e.state+'",'
    output += '\n    "postal": "'+e.postal+'",'
    output += '\n    "phone": "",'
    output += '\n    "web": "",'
    output += '\n    "hours1": "",'
    output += '\n    "hours2": "",'
    output += '\n    "hours3": "",'
    output += '\n    "featured": "",'
    output += '\n    "features": "",'
    output += '\n    "date": "10/7/18"'
    output += "\n  },"
output += "\n]"

with open("locs.json", "w") as write_file:
    write_file.write(output)
