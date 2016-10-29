__author__ = 'Alex'

import random
import math
import copy


class Elem:
    def __init__(self, x, y, val):
        self.row = x
        self.col = y
        self.val = val

    def __repr__(self):
        return "Elem(%s, %s, %s)" % (self.row, self.col, self.val)


def gen_matrix(cords, n, m, max_val):
    matrix = []
    allowed_vals = set(x for x in range(1, max_val+1))

    for i in range(0, n):
        field = []
        for j in range(0, m):
            x = 0
            field.append(x)
        matrix.append(field)

    for cord in cords:
        matrix[cord.row][cord.col] = cord.val

    got_result = False
    while not got_result:
        try:
            matrix = try_to_fill_matrix(matrix, n, m, allowed_vals)
            got_result = True
        except Exception:
            got_result = False

    return matrix


def try_to_fill_matrix(matrix, n, m, allowed_vals):
    cp_matrix = copy.deepcopy(matrix)

    for i in range(n):
        for j in range(m):
            if cp_matrix[i][j] == 0:
                row_set = set(cp_matrix[i])
                col_set = matrix_column(cp_matrix, j, max_val_count=math.ceil(n/m))
                val = random.sample(allowed_vals.difference(row_set).difference(col_set), 1)[0]
                cp_matrix[i][j] = val

    return cp_matrix


def matrix_column(matrix, n, max_val_count: object=1):
    col = {}
    for row in matrix:
        old_val = col.get(row[n], 0)
        col.update({row[n]: old_val + 1})

    result_set = set()
    for val, freq in col.items():
        if freq >= max_val_count:
            result_set.add(val)

    return result_set


def print_csharp_list_body(matrix):
    print("new List<List<string>>()\n{")
    for row in matrix:
        format_row = list(map((lambda x: '"E'+repr(x)+'", '), row))
        print("    new List<string>(){{{0}}},".format("".join(format_row)))
    print("};")


print_csharp_list_body(gen_matrix([Elem(0, 1, 5), Elem(1, 2, 3)], 10, 4, 5))
