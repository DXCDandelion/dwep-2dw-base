from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sendgrid
import base64
import os
from sendgrid.helpers.mail import *
from tinydb import TinyDB, Query

import socket
s = socket.gethostname()
print s
print socket.gethostbyname(s)

app = Flask(__name__)
CORS(app)

USER_ID_FILE_MASK = 'user_ids/%(id)d_user_id.png'
TICKET_FILE_MASK = 'tickets/%(id)d_ticket.png'
BOARDING_PASS_FILE_MASK = 'boarding_passes/%(id)d_boarding_pass.png'

sg = sendgrid.SendGridAPIClient(apikey='API KEY HERE')
FROM_EMAIL = Email('no-reply@dxcair.com')

db = TinyDB('db/database.json')
users = db.table('users')
nao_marks = db.table('nao_marks')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods = ['POST'])
def new_user():
  print request.get_json()
  user_data = request.get_json()
  NaoMark = Query()
  unalloc_nao_marks = nao_marks.search((NaoMark.allocated == False) & (NaoMark.type == 'user'))
  # print unalloc_nao_marks
  if unalloc_nao_marks:
    next_nao_mark = unalloc_nao_marks[0]
    next_nao_mark['allocated'] = True
    nao_marks.update(next_nao_mark, NaoMark.id == next_nao_mark['id'])
    user_data['nao_mark_id'] = next_nao_mark['id']
    new_user_id = create_user_id(user_data)
    email_user_id(user_data, new_user_id)
    users.insert(user_data)
    resp = jsonify(user_data)
    resp.status_code = 200
    return resp
  resp = jsonify({'msg': 'No unallocated user nao marks available'})
  resp.status_code = 500
  return resp

@app.route('/user/<id>', methods = ['GET'])
def get_user(id):
  User = Query()
  user_data = users.get(User.nao_mark_id == int(id))
  
  if user_data is None:
    resp = jsonify({'error': 'User not found.'})
    resp.status_code = 400
  else:
    resp = jsonify(user_data)
    resp.status_code = 200
  return resp

def create_user_id(user_data):
  print user_data
  user_hdr_img = Image.open('image/user_hdr.png', 'r').convert('RGBA')

  size = width, height = user_hdr_img.size
  draw = ImageDraw.Draw(user_hdr_img,'RGBA')
  font = ImageFont.truetype('image/FiraSans-Bold.ttf', 36)

  # Passenger
  text = '%s %s' % (user_data['first_name'], user_data['last_name'])
  w, h = draw.textsize(text, font=font)
  draw.text(((width-w)/2,(height-h)/2), text, (255, 255, 255, 255),font=font)
  imgs    = [user_hdr_img, Image.open('nao_mark_files/%d.png' % user_data['nao_mark_id'])]
  # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)

  min_shape = sorted( [(sum(i.size), i.size ) for i in imgs])[0][1]
  print min_shape
  new_im = Image.new('RGB', (min_shape[0], min_shape[1]*2))
  y_offset = 0
  for i in imgs:
      new_im.paste(i.resize(min_shape), (0, y_offset))
      y_offset += min_shape[0]
  new_user_id = USER_ID_FILE_MASK % {'id': user_data['nao_mark_id']}
  new_im.save(new_user_id)
  return new_user_id

@app.route('/create_ticket', methods = ['POST'])
def create_ticket():
    ticket_data =  request.get_json()
    print ticket_data
    ticket_hdr_img = Image.open('image/ticket_hdr.png', 'r').convert('RGBA')

    size = width, height = ticket_hdr_img.size
    draw = ImageDraw.Draw(ticket_hdr_img,'RGBA')
    font = ImageFont.truetype('image/FiraSans-Bold.ttf', 16)

    # Passenger
    draw.text((150,175), ticket_data['name'], (0, 155, 157, 255),font=font)
    # Flight
    draw.text((150,235), ticket_data['destination'], (0, 155, 157, 255),font=font)
    # Amount
    draw.text((150,295), ticket_data['price'], (0, 155, 157, 255),font=font)
    # ticket_hdr_img.save('sample-out.png')

    # list_im = [ticket_hdr_img, '125.png']
    imgs    = [ticket_hdr_img, Image.open('nao_mark_files/%d.png' % ticket_data['nao_mark_id'])]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)

    min_shape = sorted( [(sum(i.size), i.size ) for i in imgs])[0][1]
    new_im = Image.new('RGB', (min_shape[0], min_shape[1]*2))
    y_offset = 0
    for i in imgs:
        new_im.paste(i.resize(min_shape), (0, y_offset))
        y_offset += min_shape[0]
    new_ticket = TICKET_FILE_MASK % {'id': ticket_data['nao_mark_id']}
    new_im.save(new_ticket)
    ticket_data['ticket_file'] = new_ticket
    resp = jsonify(ticket_data)
    resp.status_code = 200
    return resp

@app.route('/create_boarding_pass', methods = ['POST'])
def create_boarding_pass():
    boarding_pass_data =  request.get_json()
    print boarding_pass_data
    boarding_pass_img = Image.open('image/boarding-pass_hdr.png', 'r').convert('RGBA')

    size = width, height = boarding_pass_img.size
    draw = ImageDraw.Draw(boarding_pass_img,'RGBA')
    font = ImageFont.truetype('image/FiraSans-Bold.ttf', 16)

    # Passenger
    draw.text((145,145), boarding_pass_data['name'], (0, 155, 157, 255),font=font)
    # Flight
    draw.text((115,205), boarding_pass_data['destination'], (0, 155, 157, 255),font=font)
    # Departs
    draw.text((250,205), boarding_pass_data['departure'], (0, 155, 157, 255),font=font)
    # Seat
    draw.text((115,265), boarding_pass_data['seat'], (0, 155, 157, 255),font=font)
    # Boarding
    draw.text((250,265), boarding_pass_data['boarding'], (0, 155, 157, 255),font=font)
    # Terminal
    draw.text((130,375), boarding_pass_data['terminal'], (0, 155, 157, 255),font=font)
    # Gate
    draw.text((250,375), boarding_pass_data['gate'], (0, 155, 157, 255),font=font)

    imgs    = [boarding_pass_img, Image.open('nao_mark_files/%d.png' % boarding_pass_data['nao_mark_id'])]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = Image.fromarray( imgs_comb)
    new_boarding_pass = BOARDING_PASS_FILE_MASK % {'id': boarding_pass_data['nao_mark_id']}
    imgs_comb.save(new_boarding_pass)
    boarding_pass_data['boarding_pass_file'] = new_boarding_pass
    resp = jsonify(boarding_pass_data)
    resp.status_code = 200
    return resp

def email_user_id(user_data, new_user_id):
    print user_data
    to_email = Email(user_data['email'])
    subject = 'Your DXC Airlines Identifier'
    content = Content('text/html', '<h1>Thank you for registering!</h1><br>Your unique DXC Airlines identifier is attached.')
    mail = Mail(FROM_EMAIL, subject, to_email, content)
    with open(new_user_id,'rb') as f:
      data = f.read()
      f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.content = encoded
    attachment.type = 'image/png'
    attachment.filename = '%s-%s-%s-ticket.png' % (user_data['first_name'],user_data['last_name'],  user_data['nao_mark_id'])
    mail.add_attachment(attachment)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    resp = jsonify({'body': response.body})
    resp.status_code = response.status_code
    return resp

@app.route('/email_ticket', methods = ['POST'])
def email_ticket():
    ticket_data =  request.get_json()
    print ticket_data
    to_email = Email(ticket_data['email'])
    subject = 'Your DXC Airlines Ticket to %s' % ticket_data['destination']
    content = Content('text/html', '<h1>Thank you for your purchase %s!</h1><br><h3>Your ticket to your flight to %s is attached.</h3>' % (ticket_data['name'], ticket_data['destination']))
    mail = Mail(FROM_EMAIL, subject, to_email, content)
    with open(ticket_data['ticket_file'], 'rb') as f:
      data = f.read()
      f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.content = encoded
    attachment.type = 'image/png'
    attachment.filename = '%s-%s-ticket.png' % (ticket_data['destination'], ticket_data['nao_mark_id'])
    mail.add_attachment(attachment)
    response = sg.client.mail.send.post(request_body=mail.get())
    resp = jsonify({'body': response.body})
    resp.status_code = response.status_code
    return resp

@app.route('/email_boarding_pass', methods = ['POST'])
def email_boarding_pass():
    boarding_pass_data =  request.get_json()
    print boarding_pass_data
    to_email = Email(boarding_pass_data['email'])
    subject = 'Your DXC Airlines Boarding Pass for %s' % boarding_pass_data['destination']
    content_text = '''
    <h1>You are now checked in for your flight to %s!</h1><br>
    <h3>Your boarding pass is attached.</h3><br>
    <h3>You are boarding at gate %s at %s</h3>
    ''' % (boarding_pass_data['destination'], boarding_pass_data['gate'], boarding_pass_data['boarding'])
    content = Content('text/html', content_text)
    mail = Mail(FROM_EMAIL, subject, to_email, content)
    with open(boarding_pass_data['boarding_pass_file'], 'rb') as f:
      data = f.read()
      f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.content = encoded
    attachment.type = 'image/png'
    attachment.filename = '%s-%s-boarding-pass.png' % (boarding_pass_data['destination'], boarding_pass_data['nao_mark_id'])
    mail.add_attachment(attachment)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    resp = jsonify({'body': response.body})
    resp.status_code = response.status_code
    return resp

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
    