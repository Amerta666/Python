# 3. Даны два файла в каждом из которых находится запись многочлена. 
#   Сформировать файл содержащий сумму многочленов.
#

def parse(expr):
    left, right = expr.split(' = ')
    terms = left.split(' + ')
    def parse_term(term):
        mlt_pw = term.split('x')
        if len(mlt_pw) == 1:
            return [int(mlt_pw[0]), 0]
        else:
            mlt = mlt_pw[0]
            pw = mlt_pw[1]
        if mlt == '':
            mlt = 1
        else:
            mlt = int(mlt.replace('*', ''))
        if pw == '':
            pw = 1
        else:
            pw = int(pw.replace('^', ''))
        return [mlt, pw]
    return list(map(parse_term, terms))

with open('Practic/Practic_5/Practice_5_3_1.txt', 'r') as file: # '3*x^6 + 3*x^4 + 8*x^3 + 9*x^2 + 4*x1 + 10 = 0'
    data = file.read().rstrip()

with open('Practic/Practic_5/Practice_5_3_2.txt', 'r') as file: # '10*x^6 + 7*x^5 + 3*x^4 + 1*x^3 + 1*x^2 + 3*x^1 = 0'
    data2 = file.read().rstrip()

expr1 = parse(data)
expr2 = parse(data2)

expression = {}
for term in expr1:
    expression[term[1]] = term[0]

for term in expr2:
    if term[1] in expression:
        expression[term[1]] += term[0]
    else:
        expression[term[1]] = term[0]

pows = sorted(list(expression.keys()), reverse=True)
def to_term(pw):
    mlt = expression[pw]
    if not(mlt) or mlt == 0:
        return ''
    if pw == 0:
        return str(mlt)
    if pw == 1:
        return f'{mlt}*x'
    return f'{mlt}*x^{pw}'

terms = list(map(to_term, pows))
terms = filter(lambda x: x, terms)
result = ' + '.join(terms) + ' = 0'

output_file = open("Practic/Practic_5/output_5_3.txt", "w") # 23*x^6 + 7*x^5 + 6*x^4 + 9*x^3 + 10*x^2 + 7*x + 10 = 0
output_file.write(result)
output_file.close()