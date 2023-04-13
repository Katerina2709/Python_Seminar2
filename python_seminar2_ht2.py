# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input('Введите сумму двух чисел, где каждое из чисел <= 1000: '))
p = int(input('Введите их произведение: '))
if s > 2000 or s < 0: 
    print ('Неверно введены данные')
else:
    # Вариант 2
    # d = (s**2 - 4*p)**0.5
    # n1 = int(s + d) // 2
    # n2 = int(s - d) // 2
    # print (f'Загаданы числа {n1} и {n2}' if n1*n2 == p else 'Неверно введены данные')
    # Вариант 1:
    ind = 0
    for n1 in range(s+1):
        for n2 in range(s - n1 + 1):
            if n1*n2 == p and n1 + n2 == s:
                ind = 1
                break
        if ind == 1: break
    print (f'Загаданы числа {n1} и {n2}' if ind == 1 else 'Неверно введены данные')