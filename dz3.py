# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

print ('Введите количество элементов в списке: ')
n  = int (input ())
list_1 = list(range(1, n))
print ('Наш список:')
print (*list_1, sep = ' ')
print ('Введите искомое число: ')
m  = int (input ())
counter = list_1.count(m)
print (f'Число {m} встречается {counter} раз')

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


print('Введите количество элементов в списке: ')
n = int(input())
list_1 = list(range(1, n+1))

print('Наш список:', *list_1, sep=' ')
print('Введите искомое число: ')
m = int(input())

if m in list_1: print(f'Число {m} входит в список')
elif m > list_1[-1]: print(f' Ближайшее к числу {m} число: {list_1[-1]}')


# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

# Значения для английских букв
letters_values_eng = [('AEIOULNSTR', 1),
                      ('DG', 2),
                      ('BCMP', 3),
                      ('FHVWY', 4),
                      ('K', 5),
                      ('JX', 8),
                      ('QZ', 10)]

# Значения для русских букв
letters_values_rus = [('АВЕИНОРСТ', 1),
                      ('ДКЛМПУ', 2),
                      ('БГЁЬЯ', 3),
                      ('ЙЫ', 4),
                      ('ЖЗХЦЧ', 5),
                      ('ШЭЮ', 8),
                      ('ФЩЪ', 10)]

# Создаем словари для английского и русского алфавитов
my_dict_eng = {letter: value for letters, value in letters_values_eng for letter in letters}
my_dict_rus = {letter: value for letters, value in letters_values_rus for letter in letters}

# Получаем слово от пользователя
word = input("Введите слово: ")
word_upper = word.upper()

# Проверяем, какой алфавит используется в слове
is_english = all(letter in my_dict_eng for letter in word_upper)
is_russian = all(letter in my_dict_rus for letter in word_upper)

if is_english:
    my_dict = my_dict_eng
elif is_russian:
    my_dict = my_dict_rus
else:
    print("Ошибка: в слове использованы буквы из разных алфавитов")
    exit()

# Вычисляем стоимость слова
total_value = sum(my_dict[letter] for letter in word_upper)

print(f"Стоимость слова '{word}' равна {total_value}")
