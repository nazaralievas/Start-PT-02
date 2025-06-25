# если бы мы делали программу типа Яндекс Такси, мы в первую очередь определились с классами
# что можно представить в виде класса?
# таксиста, клиента и саму поездку
# создадим класс Taxist с нужными атрибутами: айди, имя, марка автомобиля, номер авто и номер телефона
class Taxist:
    def __init__(self, id, name, car_model, car_number, phone_number):
        self.id = id
        self.name = name
        self.car_model = car_model
        self.car_number = car_number
        self.phone_number = phone_number

# и пропишем магический метод __str__, который позволит нам выводить данные о таксисте в виде удобной строки:
    def __str__(self):
        return f'Водитель: {self.name} на машине {self.car_model} с номерами {self.car_number}'

# создадим экземпляр класса Taxist:
taxist_1 = Taxist(1, 'Mike', 'Toyota Camry', 'X007AN', '+99670089')
# чтобы вывести имя этого таксиста, нужно:
print(taxist_1.name) # Mike
# а вот так можно вывести строку с данными таксиста, благодаря ранее написанной функции __str__
print(taxist_1) # Водитель: Mike на машине Toyota Camry с номерами X007AN


# давайте создадим класс Poezdka с нужными атрибутами:
# айди, маршрут, время начала поездки, стоимость поездки, имя пассажира и имя таксиста
class Poezdka:
    def __init__(self, id, marshrut, time_start, stoimost, passenger, taxist):
        self.id = id
        self.imarshrutd = marshrut
        self.time_start = time_start
        self.stoimost = stoimost
        self.passenger = passenger
        self.taxist = taxist

# и создадим экземпляр класса Poezdka. Мы бы могли создать его так:
poezdka_1 = Poezdka(1, 'BishkekPark - AP Manas', '14:09', 900, 'Saadat', 'Mike')
# но ведь у нас есть объект taxist_1, в котором есть вся информация о таксисте
# с помощью аггрегации, мы можем передать taxist_1 в качестве аргумента при создании экземпляра класса Poezdka. Вот так:
poezdka_1 = Poezdka(1, 'BishkekPark - AP Manas', '14:09', 900, 'Saadat', taxist_1)
# теперь мы можем узнать все данные о водителе этой поездки:
print(poezdka_1.taxist) # Водитель: Mike на машине Toyota Camry с номерами X007AN


# теперь напишем класс Client с аттрибутами айди, имя и номер телефона:
class Client:
    def __init__(self, id, name, phone_number):
        self.id = id
        self.name = name
        self.phone_number = phone_number

# создадим начего первого клиента:
client_1 = Client(1, 'Saadat', '07544657')
# и теперь в poezdka_1 вместо простого 'Saadat' можно передать client_1
poezdka_1 = Poezdka(1, 'BishkekPark - AP Manas', '14:09', 900, client_1, taxist_1)
# узнать имя клиента можно так:
print(poezdka_1.passenger.name) # Saadat



# заметили, что классы Taxist и Client имеют много общего: атрибуты айди, имя и номер телефона
# в программировании есть правило DRY - don't repeat yourself
# согласно которому не стоит писать повторяющийся код
# чтобы убрать повторение познакомимся с одним из основных принципов ООП - НАСЛЕДОВАНИЕМ
# НАСЛЕДОВАНИЕ позволяет создать родительский класс с атрибутами, общими для дочерних классов
# класс Person и будет таким родительским классом, содержащим основные повторяющиеся атрибуты:
class Person:
    def __init__(self, id, name, phone_number):
        self.id = id
        self.name = name
        self.phone_number = phone_number

# класс Taxist будет наследоваться от Person, что мы и укажем в скобках:
class Taxist(Person):
    def __init__(self, id, name, car_model, car_number, phone_number):
        super().__init__(id, name, phone_number) # указываем какие атрибуты мы наследуем у родителя
        self.car_model = car_model
        self.car_number = car_number
        
        # этот метод остается без изменений
        def __str__(self):
            return f'Водитель: {self.name} на машине {self.car_model} с номерами {self.car_number}'

# класс Client тоже наследуется от класса Person и наследует все свои атрибуты:
class Client(Person):
    def __init__(self, id, name, phone_number):
        super().__init__(id, name, phone_number)

    # напишем метод __str__ для отображения инфы о клиенте в виде красивой строки
    def __str__(self):
        return f'Имя пассажира: {self.name}; номер телефона: {self.phone_number}'


# в создании таксиста, клиента и поездки ничего не изменилось, так как мы не меняли логику кода, мы его сокращали и улучшали
taxist_1 = Taxist(1, 'Mike', 'Toyota Camry', 'X007AN', '+99670089')
client_1 = Client(1, 'Saadat', '07544657')
poezdka_1 = Poezdka(1, 'BishkekPark - AP Manas', '14:09', 900, client_1, taxist_1)
print(poezdka_1.passenger) # Имя пассажира: Saadat; номер телефона: 07544657


# рассмотрим ещё один магический метод __new__, который вызывается при создании экземпляра класса
# но мы этого не видим, так как это происходит "под капотом" - это скрыто от наших глаз
# давайте в существующий метод __new__ внесём одно действие: каждый раз при создании экземпляра класса у нас счётчик count будет увеличиваться на 1
# но счётчик count тоже не простой, это АТРИБУТ КЛАССА
# то есть принадлежит классу, а не экземплярам (это видно и по записи):
class Poezdka:
    count = 0

    def __new__(cls, *args, **kwargs): # при создании экземпляра класса Poezdka будет запускаться этот магический метод
        instance = super().__new__(cls)
        cls.count += 1 # и значение переменной count будет увеличиваться на 1
        return instance

    def __init__(self, id, marshrut, time_start, stoimost, passenger, taxist):
        self.id = id
        self.marshrut = marshrut
        self.time_start = time_start
        self.stoimost = stoimost
        self.passenger = passenger
        self.taxist = taxist


# создадим 3 поездки
poezdka_1 = Poezdka(1, 'BishkekPark - AP Manas', '14:09', 900, client_1, taxist_1)
poezdka_2 = Poezdka(2, 'Codify - Park Panfilova', '17:54', 290, client_1, taxist_1)
poezdka_3 = Poezdka(3, 'TSUM - Ala-Too', '14:09', 150, client_1, taxist_1)

# посмотрим, работает ли наш счётчик:
print(Poezdka.count) # 3
# Успех!