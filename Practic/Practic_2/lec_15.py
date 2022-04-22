# 15. Дано количество секунд. Вывести результат в виде: дни:часы:минуты:секунды

sec = int(input('Введите секунды: '))
min = 0
hour = 0
day = 0

day = sec // 86400
sec = sec % 86400
hour = sec // 3600
sec = sec % 3600
min = sec // 60
sec = sec % 60
print(f'{day}:{hour}:{min}:{sec}')
# print(f'{day} day {hour} hour {min} min {sec} sec')