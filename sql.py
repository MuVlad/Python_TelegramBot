import re
import sqlite3


def add(item):
  connect = sqlite3.connect('db.db')
  cursor = connect.cursor()
  m = []
  m.append(item.split(' '))
  name_possition = m[0][0]
  link_possition = m[0][1]
  price_possition = int(m[0][2])
  cursor.execute('INSERT INTO sup (name,link,price) VALUES(?,?,?);',
                 (name_possition, link_possition, price_possition))
  connect.commit()
  connect.close()


def get_names():
  connect = sqlite3.connect('db.db')
  cursor = connect.cursor()
  query = 'SELECT name FROM sup'
  cursor.execute(query)
  data = cursor.fetchall()
  m = []

  for i in data:
    m.append(i)

  l = len(data)
  g = []

  for i in range(l):
    a = re.sub('|\(|\'|\,|\)', '', str(m[i]))
    g.append(a)
  return g

def get_links():
  connect = sqlite3.connect('db.db')
  cursor = connect.cursor()
  query = 'SELECT link FROM sup'
  cursor.execute(query)
  data = cursor.fetchall()
  m = []

  for i in data:
    m.append(i)

  l = len(data)
  g = []

  for i in range(l):
    a = re.sub('|\(|\'|\,|\)', '', str(m[i]))
    g.append(a)
  return g

def get_prices():
  connect = sqlite3.connect('db.db')
  cursor = connect.cursor()
  query = 'SELECT price FROM sup'
  cursor.execute(query)
  data = cursor.fetchall()
  m = []

  for i in data:
    m.append(i)

  l = len(data)
  g = []

  for i in range(l):
    a = re.sub('|\(|\'|\,|\)', '', str(m[i]))
    g.append(a)
  return g


def delete(name):
  connect = sqlite3.connect('db.db')
  cursor = connect.cursor()
  query = f'DELETE FROM sup WHERE name = \'{name}\''
  cursor.execute(query)
  connect.commit()
  connect.close()
