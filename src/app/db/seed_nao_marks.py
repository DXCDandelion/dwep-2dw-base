from tinydb import TinyDB

db = TinyDB('database.json')
db.purge_table('nao_marks')

nao_marks_folder = '/home/nao/airport/nao_mark_files'

nao_marks = db.table('nao_marks')

nao_mark_ids = [64,68,80,84,85,107,108,109,112,114,117,119,124,125,127,128,130,131,136,138,141,143,146,147,148,170,171,175,187]

user_nao_mark_ids = nao_mark_ids[:7]
ticket_nao_mark_ids = nao_mark_ids[7:18]
boarding_pass_nao_mark_ids = nao_mark_ids[18:]

for nao_mark_id in user_nao_mark_ids:
  nao_marks.insert(
    {
      'id': nao_mark_id, 
      'type': 'user', 
      'allocated': False,
      'image_file': '%s/%d.jpg' % (nao_marks_folder, nao_mark_id)
    }
  )

for nao_mark_id in ticket_nao_mark_ids:
  nao_marks.insert(
    {
      'id': nao_mark_id, 
      'type': 'ticket', 
      'allocated': False,
      'image_file': '%s/%d.jpg' % (nao_marks_folder, nao_mark_id)
    }
  )

for nao_mark_id in boarding_pass_nao_mark_ids:
  nao_marks.insert(
    {
      'id': nao_mark_id, 
      'type': 'boarding_pass', 
      'allocated': False,
      'image_file': '%s/%d.jpg' % (nao_marks_folder, nao_mark_id)
    }
  )