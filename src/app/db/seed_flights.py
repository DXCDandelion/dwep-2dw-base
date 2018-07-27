from tinydb import TinyDB

db = TinyDB('database.json')
db.purge_table('flights')

flights = db.table('flights')
flights.insert(
  {
    'destination': 'Sydney', 
    'departure': '08:55',
    'gate': '11',
    'checkin_cutoff': '08:25',
    'ticket_price': 123.76,
    'capacity': 66,
    'passengers': []
  }
)

flights.insert(
  {
    'destination': 'Brisbane', 
    'departure': '09:45',
    'gate': '9',
    'checkin_cutoff': '09:15',
    'ticket_price': 321.87,
    'capacity': 44,
    'passengers': []
  }
)

flights.insert(
  {
    'destination': 'Melbourne', 
    'departure': '07:30',
    'gate': '12',
    'checkin_cutoff': '07:00',
    'ticket_price': 244.98,
    'capacity': 55,
    'passengers': []
  }
)

flights.insert(
  {
    'destination': 'Darwin', 
    'departure': '11:15',
    'gate': '9',
    'checkin_cutoff': '10:45',
    'ticket_price': 452.66,
    'capacity': 22,
    'passengers': []
  }
)

flights.insert(
  {
    'destination': 'Adelaide', 
    'departure': '13:35',
    'gate': '10',
    'checkin_cutoff': '13:05',
    'ticket_price': 231.96,
    'capacity': 33,
    'passengers': []
  }
)

flights.insert(
  {
    'destination': 'Perth', 
    'departure': '06:20',
    'gate': '8',
    'checkin_cutoff': '05:50',
    'ticket_price': 367.54,
    'capacity': 33,
    'passengers': []
  }
)

flights.insert(
  {
    'destination': 'Hobart', 
    'departure': '14:50',
    'gate': '7',
    'checkin_cutoff': '14:20',
    'ticket_price': 345.77,
    'capacity': 22,
    'passengers': []
  }
)

flights.insert(
  {
    'destination': 'Canberra', 
    'departure': '16:10',
    'gate': '8',
    'checkin_cutoff': '15:40',
    'ticket_price': 367.43,
    'capacity': 22,
    'passengers': []
  }
)