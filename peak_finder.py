import overpy 

# Set-up API
api = overpy.Overpass()

# Get Current Location
location = "California"

# Query for nearest Mountain Ranges
result = api.query("""
area
  [place=state]
  //["region:type"="mountain_area"]
  ["name:en"="{}"];
out body;

// get all peaks in the area
node
  [natural=peak]
  (area);
out body qt;
""".format(location))

# Format Results

# Display Results
print(result)
print(len(result.nodes))
print(result.nodes)
