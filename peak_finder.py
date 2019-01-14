import json
import requests
import overpass

# Set-up API
api = overpass.API()

# Get Current Location
current_location = "" #Turn location into bounding box
bbox = "5.53, 47.23, 15.38, 54.96" #

# Query for nearest Mountain Ranges
overpass_query = api.get("node({})[natural=peak];".format(bbox))

# Format and Display Results
for feature in overpass_query['features']:
  try:
    coordinates = feature["geometry"]["coordinates"]
    peak_name = feature['properties']['name']
    print(peak_name)
    print(coordinates)
  except KeyError:
    pass
