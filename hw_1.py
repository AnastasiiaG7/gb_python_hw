# Задание_1
x = 10
y = 5
w = 2
print (x - y)
print (x/w)
if x>y:
    print ('x больше y')
else:
    print('x меньше y')
age = 18
mess_1 = int(input('Напишите свой возраст'))
if age>mess_1:
    print('Вы несовершеннолетний')
else:
    print('Вы совершеннолетний')

# Задание_2
time_ = int(input('Напишите время в секундах'))

time_hours = round((time_ / 3600),0)
time_mins = round(((time_ - time_hours*3600)/60),0)
time_sec = round((time_ - time_hours*3600 - time_mins*60),2)
print(f'Время сейчас: {time_hours} часов, {time_mins} минут, {time_sec} секунд')

# Задание_3
n = int(input('Задайте число n'))
print (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))

# Задание_4
task_4 = abs(int(input('Введите целое положительное число ')))
max_num = task_4 % 10
while task_4 >= 1:
    task_4 = task_4 // 10
    if task_4 % 10 > max_num:
        max_num = task_4 % 10
    if task_4 > 9:
        continue
    else:
        print(f'Самая большая цифра в числе, {max_num}')
        break
# Задание_5
income = int(input('Введите значение выручки предприятия за рассматриваемый период в рублях '))
expences = int(input('Введите значение расходов предприятия за рассматриваемый период в рублях '))
result = income  - expences
if result>0:
    print (f'За рассматриваемый период доход предприятия составил {result} рублей')
elif result<0:
    print('За рассматриваемый период предприятие работало в убыток и потеряло', abs(result), 'рублей')
else:
    print(f'За рассматриваемый период предприятие ушло в ноль')

# Задание_6
ret = round((result/income),2)
if result>0:
    print(f'Рентабельность предприятия составила {ret}')
pers_num = int(input('Введите численность предприятия'))
res_per_pers = round(result/pers_num)
print(f'Прибыль фирмы в расчете на одного сотрудника составляет: {res_per_pers} рублей')

# Задание 7
a = int(input('Введите сколько км пробежали в первый день'))
b = int(input('Введите сколько км желаете бегать'))
days = 1
while a < b:
        a = a + 0.1 * a
        days += 1
print(f'Вы достигнете требуемых показателей на {days} день')