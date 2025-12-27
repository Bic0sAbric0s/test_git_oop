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
    def __init__(self, mark, balance):
        self.mark = mark
        self.balance = balance
        self.auto_df = {np.random.randint(1000,9999): [np.random.choice(auto_m), np.random.randint(1_500_000, 7_000_000)] for _ in range(30)}
        self.id = list(self.auto_df.keys())
        
    def all_auto(self):
        print('ID   brand  price')
        for key, columns in self.auto_df.items():
            print(f'{key}: {columns[0]}, {columns[1]}')
            
    def choice_brand(self):
        for i in self.id:
            if self.mark in self.auto_df[i][0]:
                pass
            

                
                
# brand_user = input('Напишите марку автомобиля, который хотите арендовать ')
# balance = input('Напишите сумму, в пределах который вы хотите арендовать автомобиль ')              
    
# car = CarDealerShip(brand_user, balance)
car = CarDealerShip('2', 2)
print(car.all_auto())
# print(car.choice_brand())



