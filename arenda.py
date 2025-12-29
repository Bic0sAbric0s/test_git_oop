import pandas as pd
import numpy as np

np.random.seed(3)
auto_m = ["Toyota", "Volkswagen", "Ford", "Honda", "Nissan", "Hyundai", "Kia", "Mercedes-Benz", "BMW", "Chevrolet"]

customer_df = ({
    'id': None,
    'name': None,
})

class Car:
    df = pd.DataFrame({
        'id': np.random.randint(1000, 9999, 30),
        'brand': np.random.choice(auto_m, 30),
        'year': np.random.randint(2015, 2025, 30),
        'flag': 'Freely'
    })
    id = df['id'].to_numpy()
    
    @classmethod
    def auto_all(cls):
        print(cls.df)
       
class RentalCar(Car):
    price_auto = pd.DataFrame({
        'brand': ["Toyota", "Volkswagen", "Ford", "Honda", "Nissan", "Hyundai", "Kia", "Mercedes-Benz", "BMW", "Chevrolet"],
        'price': [10,11,12,8,11,8,8,15,15,11] 
    })
    
    @classmethod
    def price_auto_k(cls):
        cls.df['price_minutes'] = cls.df['brand'].map(
            dict(zip(cls.price_auto['brand'], cls.price_auto['price']))
        )
        print(cls.df)
        
class Customer:
    def __init__(self, name):
        self.name = name
        
    def append_customer(self):
        customer_df.loc = [np.random.randint(1000,9999), self.name]
        return f'Вы внесены в базу данных'
        
class Rent(Customer, RentalCar):
    def __init__(self, name, brand, year):
        super().__init__(name)
        self.brand = brand
        self.year = year
        
    def pay_auto(self):
        my_car = RentalCar.df[RentalCar.df['brand'] == self.brand]
        print(my_car)
        
rent_user = Rent('Борис', 'BMW', '2021')
rent_user.pay_auto()

