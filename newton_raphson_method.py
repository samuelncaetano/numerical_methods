import pandas as pd
from sympy import symbols, diff


def newton_raphson(f, df, x0, i):
    table_data = []

    for i in range(1, i + 1):
        xr = x0 - f(x0) / df(x0)
        table_data.append(
            [i, float(x0), float(f(x0)), float(df(x0)), float(xr)])
        x0 = xr

    table = pd.DataFrame(table_data, columns=[
                         'Iteração', 'x0', 'f(x0)', "f'(x0)", 'xr'])
    return table


def funcao(x0):
    return x0**2 - 2


def derivada_funcao(x0):
    x = symbols('x')
    df = diff(funcao(x), x)
    return df.subs(x, x0)


raiz = newton_raphson(funcao, derivada_funcao, 1, 3)
print(raiz)
