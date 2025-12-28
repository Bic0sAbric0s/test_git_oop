import numpy as np
import random

#.items исп в словарях для разделения код значение
# dict {a = b,c} намного эффективнее

np.random.seed(2)
auto_m = ["Toyota", "Volkswagen", "Ford", "Honda", "Nissan", "Hyundai", "Kia", "Mercedes-Benz", "BMW", "Chevrolet"]

auto_df = {}

# Плохой вариант
# for i in range(30):
#     auto_df[np.random.randint(1000,9999)] = [np.random.choice(auto_m), np.random.randint(1_500_000, 7_000_000)]

class CarDealerShip:
    auto_df = {np.random.randint(1000,9999): [np.random.choice(auto_m), np.random.randint(1_500_000, 7_000_000), np.random.randint(2012, 2025), np.random.randint(75_000, 500_000)] for _ in range(30)}
    id = list(auto_df.keys())
    
    def __init__(self, mark, balance, year, km):
        self.mark = mark
        self.balance = balance
        self.year = year
        self.km = km
        
    @staticmethod
    def krit():
        brand_user = input('Напишите марку автомобиля, который хотите арендовать ')
        balance = int(input('Напишите сумму, в пределах которой вы хотите арендовать автомобиль '))
        year = input('Введите год машины ').split('-')              
        km = int(input('Какой пробег долен быть у машины '))
        car = CarDealerShip(brand_user, balance, year, km) 
        car.choice_brand()
        
    def all_auto():
        print('ID   brand  price   year  distancekm')
        for key, columns in CarDealerShip.auto_df.items():
            print(f'{key}: {columns[0]}, {columns[1]}, {columns[2]}, {columns[3]}')
            
    def choice_brand(self):
        for i in CarDealerShip.id:
            if self.mark in CarDealerShip.auto_df[i][0] and \
                CarDealerShip.auto_df[i][1] <= self.balance + 50_000 and\
                (int(self.year[0]) <= CarDealerShip.auto_df[i][2] <= int(self.year[1])) and \
                CarDealerShip.auto_df[i][3] <= self.km + 50_000:
                    print(i, *CarDealerShip.auto_df[i])
            else:
                print('Ничего не найдено')
                
    def pay_car():
        pass
            
choice_user = int(input('Выберете: 1-показ всех авто, 2-выбор авто, 3-покупка авто'))

if choice_user == 1:
    print(CarDealerShip.all_auto())               
elif choice_user == 2:      
    print(CarDealerShip.krit())
elif choice_user == 3:
    print(CarDealerShip.pay_car())



