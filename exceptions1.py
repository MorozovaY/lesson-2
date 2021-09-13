#Перепишите функцию discounted(price, discount, max_discount=20) из урока про функции так,
#чтобы она перехватывала исключения, когда переданы некорректные аргументы.
#Первые два нужно приводить к вещественному числу при помощи float(), а третий -
#к целому при помощи int() и перехватывать исключения ValueError и TypeError,
#если приведение типов не сработало.

def discounted(price, discount, max_discount):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
        print(price + discount + max_discount)
    except (ValueError, TypeError):
        print("Некорректные аргументы")
    
discounted(1, 1, 1)
discounted('привет', 1, 1)