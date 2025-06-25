# Разбор домашки:
# У класса Client напишите метод __str__, который будет выводить информацию о клиенте
# в виде строки (посмотрите как мы сделали это у таксиста)
class Client:
    def __init__(self, id, name, phone_number):
        self.id = id
        self.name = name
        self.phone_number = phone_number
    
    def __str__(self):
        return f'Имя: {self.name}; номер телефона: {self.phone_number}'

# на прошлом уроке мы разобрали с вами наследование
# и для удобства наследовали классы Client и Taxist от класса Person:
class Person:
    def __init__(self, id, name, phone_number):
        self.id = id
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f'Имя: {self.name}; номер телефона: {self.phone_number}'

# класс Client может наследовать всё от Person таким образом:
class Client(Person):
    pass

# и при расширении нашего бизнеса, если нам нужен новый класс Курьер,
# мы можем наследовать его от Person
class Courier(Person):
    pass

# и создавать объекты:
client_1 = Client(1, 'Doni', '+8896756')
client_1.name = 'Daniel'
# и пользоваться методом __str__ родительского класса:
print(client_1) # Имя: Daniel; номер телефона: +8896756

courier_1 = Courier(1, 'Robert', '+7776002')
print(courier_1) # Имя: Robert; номер телефона: +7776002
