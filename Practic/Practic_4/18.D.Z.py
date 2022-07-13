# 18. Вычислить число Пи c заданной точностью d
#	  Пример: при d = 0.001, Пи = 3.141.10 в степени -1 <= d <= 10 в степени -10#

def get_dot_count(number):
    return (len(str(float(number))[str(float(number)).index('.')+1:]) 
            if str(float(number))[str(float(number)).index('.')+1:]!='0' 
            else 0)

d = float(input('Введите D: '))
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480

print(get_dot_count(d))
print(round(pi, get_dot_count(d)))