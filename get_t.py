from speed_auto import speed
    
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
    

b = input('Введите бренд авто')
print(auto(b))
print(f(b))