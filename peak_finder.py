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
    coordinates = feature["geometry"]["coordinates"]
    peak_name = feature['properties']['name']
    print(peak_name)
    print(coordinates)
  except KeyError:
    pass
