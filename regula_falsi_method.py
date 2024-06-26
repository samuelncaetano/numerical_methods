import math
import pandas as pd


def regula_falsi(f, a, b, i):
    table_data = []
    for i in range(1, i + 1):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        table_data.append([i, a, b, c, f(a), f(c)])

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    table = pd.DataFrame(table_data, columns=[
                         'Iteração', 'x1', 'x2', 'xr', 'f(x1)', 'f(xr)'])
    return table


def funcao(x):
    return (((9.81*68.1)/x)*(1-math.exp(-(x/68.1)*10)))-40


raiz = regula_falsi(funcao, 12, 16, 3)
print(raiz)
