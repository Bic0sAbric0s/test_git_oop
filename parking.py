import random
import numpy as np
import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
brand TEXT NOT NULL,
time DATE,
time_down DATE,
flag INT
)
''')

def insert(id, username, brand):
    cursor.execute("INSERT INTO Users (id, username, brand) VALUES (?,?,?)", (id, username, brand))

def select():
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    
    for i in users:
        print(i)

def check(id_user):
    cursor.execute('select 1 from Users where id = ? LIMIT 1', (id_user, ))
    return cursor.fetchone()

np.random.seed(1)

class Parking:
    def __init__(self, id, brand):
        self._id = id
        self.brand = brand
        self.f = 1
        self.price = 100
        
    def id(self):
        return self._id
    
    def register():
        return np.random.randint(1000, 10000)
    
    def enter(self, time_down, time):
        pass
    
    def otdach(self):
        pass

id_user = Parking.register()
if check(id_user) is False:
    name = input('Введите имя')  
    brand_auto = input('Введите бренд вашего автомобиля ')
else:
    print('Вы зарегистрированы')
# id_user = Parking.register()

# insert(id_user, name, brand_auto)



# request = int(input('Выбере услугу: 1-въезд, 2-выезд'))

# if 



connection.commit()
connection.close()
