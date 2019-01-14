import json
import requests
import overpass

def get_current_location():
  current_location = "33.671039, -117.910602"
  return current_location

def display_results(results):
  # Format and Display Results
  for feature in results['features']:
    try:
      coordinates = feature["geometry"]["coordinates"]
      peak_name = feature['properties']['name']
      print(peak_name)
      print(coordinates)
    except KeyError:
      pass

def find_nearest_peak(min_range = 5, max_range = 100, range_inc = 5):
  # Set-up API
  api = overpass.API()

  # Location
  current_location = get_current_location()

  # Query for nearest Mountain Ranges
  for radius in range(min_range, max_range, range_inc):
    print(radius)

    overpass_query = api.get("node(around:{}, {})[natural=peak];".format(radius*1609.344, current_location))
    if len(overpass_query['features']) > 1:
      display_results(overpass_query)
      return

    elif radius == max_range:
      print("No Peaks found within {} mile radius".format(max_range))


find_nearest_peak()