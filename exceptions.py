#Перепишите функцию hello_user() из задания про while, чтобы она перехватывала KeyboardInterrupt,
#писала пользователю "Пока!" и завершала работу при помощи оператора break

def exceptions():

    while True:
        try:
            hello_user = input('Как дела?')
            if hello_user == 'Хорошо':
                print('Я очень рад')
            else:
                print('Понятно')
        except KeyboardInterrupt:
            print('Пока!')
            break

exceptions()