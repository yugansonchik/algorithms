def in_short(mystring):
    count = 1
    res = ''

    for i, char in enumerate(mystring):
        try:
            if char == mystring[i + 1]:
                count += 1
            else:
                if count == 1:
                    res += str(char)
                else:
                    res += str(count)
                    res += str(char)
                count = 1

        except IndexError:
            if count == 1:
                res += str(char)
            else:
                res += str(count)
                res += str(char)
    return res

string = input()
print(in_short(string))


'''
enumerate - функция для перебора элементов последовательности - списка, кортежа или строки одновременно с их индексами!
______________________________________________
1 sample
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)


0 apple
1 banana
2 cherry
______________________________________________
2 sample
languages = ['Python', 'java', 'c++']
lang_dict = dict(enumerate(languages))
print(lang_dict) #словарь, где ключи - индексы, значения - элементы

{0: 'Python', 1: 'Java', 2: 'JavaScript', 3: 'C++'}

'''