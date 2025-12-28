import numpy as np
import random

#.items исп в словарях для разделения код значение
# dict {a = b,c} намного эффективнее

np.random.seed(2)
auto_m = ["Toyota", "Volkswagen", "Ford", "Honda", "Nissan", "Hyundai", "Kia", "Mercedes-Benz", "BMW", "Chevrolet"]

# Плохой вариант
# for i in range(30):
#     auto_df[np.random.randint(1000,9999)] = [np.random.choice(auto_m), np.random.randint(1_500_000, 7_000_000)]

class CarDealerShip:
    auto_df = {
        np.random.randint(1000,9999): 
        [np.random.choice(auto_m),
         np.random.randint(1_500_000, 7_000_000),
         np.random.randint(2012, 2025), np.random.randint(75_000, 500_000)]
        for _ in range(30)
    }
    id = list(auto_df.keys())
    
    def __init__(self, mark, balance, year, km):
        self.mark = mark
        self.balance = balance
        self.year = year  # должно быть: мин_год-макс_год
        self.km = km
   
        
    @classmethod
    def krit(cls):
        brand_user = input('Напишите марку автомобиля, который хотите арендовать ')
        balance = int(input('Напишите сумму, в пределах которой вы хотите арендовать автомобиль '))
        year = input('Введите год машины ').split('-')              
        km = int(input('Какой пробег долен быть у машины '))
        
        car = cls(brand_user, balance, year, km) 
        return car.choice_brand()
    
    @classmethod  
    def all_auto(cls):
        print('ID   brand  price   year  distancekm')
        for key, columns in cls.auto_df.items():
            print(f'{key}: {columns[0]}, {columns[1]}, {columns[2]}, {columns[3]}')
        return len(cls.auto_df) 
            
    def choice_brand(self):
        auto_pay = {}
        for i in CarDealerShip.id:
            if self.mark in CarDealerShip.auto_df[i][0] and \
                CarDealerShip.auto_df[i][1] <= self.balance + 50_000 and\
                (int(self.year[0]) <= CarDealerShip.auto_df[i][2] <= int(self.year[1])) and \
                CarDealerShip.auto_df[i][3] <= self.km + 50_000:
                    auto_pay[i] = CarDealerShip.auto_df[i]
                    print(f'ID: {i}, Характеристики: ', *CarDealerShip.auto_df[i])
        if auto_pay is None:
            print('Ничего не найдено')
            
        if auto_pay:
            prom = int(input('Вы хотите рассмотреть данные варианты для покупки: 1-Да 2-Нет '))
            if prom == 1:
                CarDealerShip.pay_car(auto_pay)
            else:
                print('Хорошего дня! Приходите к нам еще')
        
    @staticmethod            
    def pay_car(auto_pay):
        for key, col in auto_pay.items():
            print(f'ID: {key} Характеристики: {col[0]} {col[1]} {col[2]} {col[3]}')
        id_pay = int(input('Введите ID понравившегося авто '))
        for i in list(auto_pay.keys()):
            if id_pay == int(i):
                print(f'Поздравляю! Вы купили {auto_pay[i][0]} {auto_pay[i][2]} года с пробегом {auto_pay[i][3]}км')
            
            del CarDealerShip.auto_df[id_pay]
            break
        else:
            print('Увы, автомобиля с таки ID нет')
            

if __name__ == "__main__":
    while True:
        print("\n" + "=" * 40)
        print("АВТОСАЛОН")
        print("=" * 40)
        print("1. Показать все автомобили")
        print("2. Подобрать автомобиль по критериям")
        print("3. Выход")
        
        try:
            choice_user = int(input('Введите число 1-3 '))
        
            if choice_user == 1:
                CarDealerShip.all_auto()
            elif choice_user == 2:
                CarDealerShip.krit()
            elif choice_user == 3:
                print('До скорой встречи!')
                break
            else:
                print('Пожалуйста, выберете 1,2 или 3 ')
        except:
            print('Вы ввели не число!')


