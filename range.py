#Создать список из десяти целых чисел.
#Вывести на экран каждое число, увеличенное на 1.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for final_number in numbers:    
    print(final_number + 1)


#Ввести с клавиатуры строку.
#Вывести эту же строку вертикально: по одному символу на строку консоли.

example_string = "Я учусь"

for word in example_string:
	print(word)


#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.

students_scores = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [5,5,4,5,3]},
    {'school_class': '4c', 'scores': [2,2,2,5,2]}
]

school_sum = 0
len_sum = 0

for score in students_scores:
    marks_sum = 0
    for class_sum in score['scores']:
        marks_sum += class_sum
    class_avg = marks_sum / len(score['scores'])
    print(score['school_class'],class_avg)
    school_sum += marks_sum
    len_sum += len(score['scores'])
school_avg = school_sum / len_sum
print(school_avg)