from speed_auto import speed, country
from distances_auto import distance

print('Hello')

for i in range(5):
    print(i)
    
def hello():
    pass

def her():
    pass

def auto(brand):
    return brand

def f(b):
    try:  
        return speed[b]
    except:
        print('Для такого бренда машины средняя скорость неизвеста')

def country_f(b):
    try:
        return country[b]
    except:
        print('Такой марки машины нет в списке')
        
def distance_f(b):
    try:
        return distance[b]
    except:
        print('Такой марки машины нет в списке')
        
print('-----------------')

b = input('Введите бренд авто')
print(auto(b))
print(f(b))
print(country_f(b))