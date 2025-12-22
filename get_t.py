from speed_auto import speed

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
    return speed[b]
    

b = input('Введите бренд авто')
print(auto(b))
print(f(b))