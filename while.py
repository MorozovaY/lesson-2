#Напишите функцию hello_user(), которая с помощью функции input()
#спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”

def good():
    while True:
        hello_user = input('Как дела?')
        if hello_user == 'Хорошо':
            break

good()