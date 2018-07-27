from tinydb import TinyDB

db = TinyDB('database.json')
db.purge_table('locations')

locations = db.table('locations')

locations.insert(
  {
    'name': 'Bar', 
    'directions': ['list of directions']
  }
)

locations.insert(
  {
    'name': 'McDonalds', 
    'directions': ['list of directions']
  }
)

locations.insert(
  {
    'name': 'Cafe', 
    'directions': ['list of directions']
  }
)

locations.insert(
  {
    'name': 'Car Park', 
    'directions': ['list of directions']
  }
)

locations.insert(
  {
    'name': 'Taxi Rank', 
    'directions': ['list of directions']
  }
)

locations.insert(
  {
    'name': 'Toilets', 
    'directions': ['list of directions']
  }
)

locations.insert(
  {
    'name': 'ATM', 
    'directions': ['list of directions']
  }
)

locations.insert(
  {
    'name': 'Bar', 
    'directions': ['list of directions']
  }
)

locations.insert(
  {
    'name': 'Gate x', 
    'directions': ['list of directions']
  }
)