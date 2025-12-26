import numpy as np
import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
brand TEXT NOT NULL,
count_parking INT)
''')

def insert(id, username, brand, count_parking):
    cursor.execute("INSERT INTO Users (id, username, brand, count_parking) VALUES (?,?,?,?)", (id, username, brand, count_parking))

def select():
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    
    for i in users:
        print(i)

def check_user(id_user):
    cursor.execute('select 1 from Users where id = ? LIMIT 1', (id_user, ))
    return cursor.fetchone()

def brand_f(id_user):
    cursor.execute('select brand from Users where id = ? limit 1', (id_user, ))
    return cursor.fetchone()

def count_parking_plus(id_user):
    cursor.execute('Update Users set count_parking = count_parking + 1 where id = ?', (id_user, ))

def delete_table():
    cursor.execute('delete from Users')
# np.random.seed(1)

class Parking:
    def __init__(self, id, brand):
        self._id = id
        self.brand = brand
        self.f = 1
        self.price = 100
        self.price_end = 150
        self._wastes = 0
        
    def id(self):
        return self._id
    
    def register():
        return np.random.randint(1000, 10000)
    
    def parking_price(self, amount):
        time_parking = np.random.randint(amount, amount+10)
        count_parking_plus(self._id)
        return (self.price * amount) + (self.price_end * (time_parking-amount))


# id_user = Parking.register()
id_user = int(input('Введите ID '))
if check_user(id_user) is None:
    name = input('Введите имя ')  
    brand_auto = input('Введите бренд вашего автомобиля ')
    insert(id_user, name, brand_auto, 0)
else:
    print('Вы зарегистрированы')

brand_auto = brand_f(id_user)
car = Parking(id_user, brand_auto)
amount = int(input('На сколько часов вы хотите арендовать парковочное место? '))
print(f'Итого: {car.parking_price(amount)} рублей')

print(select())
    
connection.commit()
connection.close()
