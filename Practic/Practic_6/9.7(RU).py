
class Expression:
    def __init__(self, st):
        self.list = []
        self.__parse_st_to_list(st)

    def evaluate(self):
        self.__operate('*', lambda a, b: a * b)
        self.__operate('/', lambda a, b: a / b)
        self.__operate('+', lambda a, b: a + b)
        self.__operate('-', lambda a, b: a - b)
        return self.list[0]


    def __parse_st_to_list(self, st):
        current_number = ''
        for i in st:
            if i.isdigit() == True:
                current_number += i
            else:
                self.list.append(int(current_number))
                current_number = ''
                if i == '+' or i == '-' or i == '*' or i == '/':
                    self.list.append(i)
        if len(current_number) > 0:
            self.list.append(int(current_number))


    def __operate(self, operator, fn):
        size = len(self.list)
        sum = None
        for i in range(size):
            for j in range(size):
                if i >= size:
                    break
                if self.list[i] == operator:
                    a = self.list[i-1]
                    b = self.list[i+1]
                    sum = fn(a, b)
                    self.list[i - 1] = sum
                    self.list.pop(i + 1)
                    self.list.pop(i)
                    size = len(self.list)

st = '1+21-3*4*5'
expr = Expression(st)
print(expr.evaluate())
