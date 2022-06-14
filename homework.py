#1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
#Пример: 2+2 => 4;  => 7; 1-2*3 => -5;
#Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
#Пример: 1+2*3 => 7; (1+2)*3 => 9;

'''def find(nums):
    if '^' in nums:
        abs = nums.index("^")
        nums[abs] = int(nums[abs-1]) ** int(nums[abs+1])
        del nums[abs+1]
        del nums[abs-1]
        find(nums)
    return nums

def create_array(sp, stroka):
    arr = [i for i in stroka]
    nums = []
    s = ''
    for i in arr:
        if i in sp:
            s += i
        else:
            nums.append(s)
            nums.append(i)
            s = ''
    nums.append(s)
    return nums

def znach(nums):
    i = 0
    while i < len(nums):
        if nums[i] == '*':
            nums[i] = int(nums[i-1]) * int(nums[i+1])
            del nums[i+1]
            del nums[i-1]
            i -= 1
        elif nums[i] == '/':
            nums[i] = int(nums[i-1]) / int(nums[i+1])
            del nums[i+1]
            del nums[i-1]
            i -= 1
        i += 1
    print(nums)
    znach = int(nums[0])
    for i in range(len(nums)):
        if nums[i] == '+':
            znach += int(nums[i+1])
        elif nums[i] == '-':
            znach -= int(nums[i+1])
    print(znach)

n = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
exp = '1+2*3'

array = create_array(n, exp)
print(array)
array = find(array)
print(array)
znach(array)'''

#2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 

'''def slovar(stroka):
    sl = {}
    g = 0
    for i in stroka:
        if i not in sl.values():
            sl[g] = i
            g += 1
    return sl
        
def get_key(i, sl):
    for k, j in sl.items():
        if j == i:
            return k

def create_array(text):
    stroka = str(text.readlines()).replace('[', '').replace(']', '').replace("'", '')
    array = list(stroka.split())
    return array

def convert_file_min(gk, sl, ca):
    with open('text_do.txt','r', encoding='utf8') as fdo, open('text_posle.txt', 'w') as fpo:
        file_format = ca(fdo)
        ff = sl(file_format)
        for i in file_format:
            key = gk(i, ff)
            if ff[key] == '\\n,':
                fpo.write('\n')
            else:
                fpo.write(f'{key}' + ' ')

def convert_file_max(ca, sl):
    with open('text_posle.txt', 'r+', encoding='utf8') as tp, open('text_do.txt','r', encoding='utf8') as td:
        ff = sl(create_array(td))
        file_format = create_array(tp)
    with open('text_posle.txt', 'w+', encoding='utf8') as tp:
        for i in file_format:
            if i == '\\n,':
                tp.write('\n')
            else:
                key = int(i)
                tp.write(f'{ff[key]} ')б
user = input('Вы хотите сжать файл или восстановить?: ')
if user.lower() == 'сжать':
    convert_file_min(get_key, slovar, create_array)
elif user.lower() == 'восстановить':
    convert_file_max(create_array, slovar)'''

#3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
#Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . 
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть. 
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
#Не использовать функцию encode.

slovar = {
    'а': 'м', 'б': 'н', 'в': 'о', 'г': 'п', 'д': 'р', 'е': 'с', 'ё': 'т', 'ж': 'у', 'з': 'ф', 'и': 'х',
    'й': 'ц', 'к': 'ч', 'л': 'ш', 'м': 'щ', 'н': 'ь', 'о': 'ы', 'п': 'ъ', 'р': 'э', 'с': 'ю', 'т': 'я',
    'у': 'а', 'ф': 'б', 'х': 'в', 'ц': 'г', 'ч': 'д', 'ш': '', 'щ': '', 'ъ': '', 'ы': '', 'ь': '',
    'э': '', 'ю': '', 'я': ''
}