# Without function
PLACES = {1: "Delhi",
          2: "London",
          3: "Paris",
          4: "New York",
          5: "Doha",}

for pl in PLACES:
  if len(PLACES[pl]) > 5:
    print(PLACES[pl].upper())
  
# With function
def place_names(places):
  for pl in places:
    if len(places[pl]) > 5:
      print(places[pl].upper())

PLACES = {1: "Delhi",
          2: "London",
          3: "Paris",
          4: "New York",
          5: "Doha",}
place_names(PLACES)
