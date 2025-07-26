def func(a, b):
    return a + b

# эта же функция в виде лямбда-функции
f = lambda a, b: a+b

a = 5
b = 4
print(func(a, b))
print(f(a, b))

# map() применяет функцию ко всем элементам, например, списка:
# map(функция, список)

nums = [1, 2, 3, 4]
kvadraty = list(map(lambda x: x**2, nums))
print(kvadraty)  # [1, 4, 9, 16]