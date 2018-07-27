from tinydb import TinyDB

db = TinyDB('../database.json')
db.purge_table('users')

users = db.table('users')
users.insert(
  {
    'first_name': 'Bob', 
    'last_name': 'Down',
    'email': 'nothing@nothing.com',
    'password': 'efwefwfwef',
    'cc_number': 1234567809876543,
    'nao_mark_id': 108,
    'security_flag': 'GREEN',
    'tickets': [],
    'boarding_passes': []
  }
)