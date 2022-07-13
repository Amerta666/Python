# 5. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую 
#   последовательность и содержащие максимальное количество элементов. 
#   Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#              [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]


def best_list(list, current_list = [], i = 0):
    if i >= len(list):
        return current_list
    can_take = len(current_list) == 0 or list[i] > current_list[-1]
    if can_take:
        if_take = best_list(list, current_list + [list[i]], i + 1)
        if_not_take = best_list(list, current_list, i + 1)
        if len(if_take) > len(if_not_take):
            return if_take
        else:
            return if_not_take
    else:
        return best_list(list, current_list, i + 1)

print(best_list([1, 5, 2, 3, 4, 6, 1, 7]))     # [1, 2, 3, 4, 6, 7]
print(best_list([5, 2, 3, 4, 6, 1, 7]))        # [2, 3, 4, 6, 7]