import math
import pandas as pd


def bisseccao(f, a, b, i):
    table_data = []
    for i in range(1, i + 1):
        c = (a + b) / 2
        table_data.append([i, a, b, c, f(a), f(b), f(c)])

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    table = pd.DataFrame(table_data, columns=[
                         'Iteração', 'x1', 'x2', 'xr', 'f(x1)', 'f(x2)', 'f(xr)'])
    return table


def funcao(x):
    return (((9.81*68.1)/x)*(1-math.exp(-(x/68.1)*10)))-40


raiz = bisseccao(funcao, 12, 16, 3)
print(raiz)
