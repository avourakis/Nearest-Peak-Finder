import json
import requests
import overpass

# Set-up API
api = overpass.API()

# Get Current Location
location = "California"

# Query for nearest Mountain Ranges
overpass_query = api.get("""
 area
  [place=state]
  //["region:type"="mountain_area"]
  ["name:en"="{}"];
out meta;

// get all peaks in the area
node
  [natural=peak]
  (area);
out meta;
 
 """.format(location))

# Format and Display Results
for feature in overpass_query['features']:
  try:
    print(feature['properties']['name'])
  except KeyError:
    print('No Peak name')
