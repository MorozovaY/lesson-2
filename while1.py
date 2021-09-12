def hey_user():

    hello_user = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую!'}

    while True:
        ask_user = input('Введите вопрос или exit')
        if ask_user == 'exit':
                break
        for question, answer in hello_user.items():
            if ask_user == question:
                print(hello_user.get(question))

hey_user()