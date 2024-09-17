# Задача №1
# nested_list = [['Я помню'],['чудное'], ['мгновенье'], ['передо'], ['мной'], ['явилась'], ['ты']]
# new_list = []
# for words in nested_list:
#     new_list.extend(words)
# print(new_list)

# Задача №2
# numbers = [5, 8, 9, 5, 7, 9, 6, 8, 5 , 9]
# value_remove_num = [9, 5]
# for i in value_remove_num:
#     while i in numbers:
#        numbers.remove(i)
# print(numbers)

# Задача №3
set_a = {1, 5 , 6, 9}
set_b = {1, 5}
print(set_a.issuperset(set_b))
# issuperset - возвращает True, если первое множество является подмножеством второго,
# и False в обратном случае.
# issubset - возвращает True, если одно множество является надмножеством другого,
# и False в противном случае.

# Задача №4
list_str = ['Привет, как твои дела?',
            'Оу, сегодня прекрасный денек для прогулок и солнечных ванн.',
            'Ты не против составить мне компанию?',
            'С удовольствием!',
            ]
print(list_str)

max_len = max(len(s) for s in list_str)
for i, s in enumerate(list_str):
        if len(s) < max_len:
            list_str[i] = s.ljust(max_len, '_')
input_str = list_str
for item in input_str:
    print(item)



