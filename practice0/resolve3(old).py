#Задача «Среднее арифметическое».

## через импорт плагина
first=12
second=24
third=36

massive = (first, second, third)

from statistics import mean

print(mean(massive))

## без импорта, чистая логика

print(sum(massive)/len(massive))