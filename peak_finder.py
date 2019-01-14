from geopy import distance
import overpass
import operator
import geocoder


def get_current_location():
  g = geocoder.ip('me')
  return tuple(g.latlng)


def format_results(results, current_location):
  formatted_results = {}

  for feature in results['features']:
    try:
      node_id = feature["id"]
      coordinates = tuple(reversed(feature["geometry"]["coordinates"]))
      peak_name = feature['properties']['name']
      dist = distance.geodesic(current_location, coordinates).miles
      formatted_results[dist] = {"name": peak_name, "coordinates": coordinates, "id": node_id}
    except KeyError:
      pass

  return formatted_results

def display_results(results, num_results = 5):
  # Format and Display Results
  print('\nMountain Peaks Near You:\n')
  for i, peak in enumerate(sorted(results.items(), key=operator.itemgetter(0)), 1):
    print('{}. {} ({} mi)'.format(i, peak[1]['name'], round(peak[0], 1)))
    if i == num_results:
      print('\nNote: Only displaying top {} results.\n'.format(num_results))
      return

  print('\nNote: Only displaying top {} results.\n'.format(num_results))

def find_nearest_peak(min_range = 5, max_range = 100, range_inc = 5):
  # Set-up API
  api = overpass.API()

  # Location
  current_location = get_current_location()

  # Query for nearest Mountain Ranges
  for radius in range(min_range, max_range, range_inc):

    overpass_query = api.get("node(around:{}, {})[natural=peak];".format(radius*1609.344, ', '.join(str(v) for v in current_location)))
    if len(overpass_query['features']) > 1:
      display_results(format_results(overpass_query, current_location))
      return
    elif radius == max_range:
      print("No Peaks found within {} mile radius".format(max_range))


find_nearest_peak()