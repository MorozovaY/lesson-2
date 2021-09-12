age = input('Введите ваш возраст:')
true_age = int(age)

def user_age(age):
    if age < 7:
        return 'в детском саду'
    elif 7 <= age <= 18:
        return 'в школе'
    elif 18 < age <= 22:
        return 'в вузе'
    else:
        return 'работает'

print(user_age(true_age))