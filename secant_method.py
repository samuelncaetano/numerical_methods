import pandas as pd


def secante(f, x0, x1, i):
    table_data = []

    for i in range(1, i + 1):
        xr = x1 - f(x1) * ((x1 - x0)/(f(x1) - f(x0)))
        table_data.append([i, x0, x1, f(x0), f(x1), xr])
        x0, x1 = x1, xr

    table = pd.DataFrame(table_data, columns=[
                         'Iteração', 'x0', 'x1', 'f(x0)', 'f(x1)', 'xr'])
    return table


def funcao(x):
    return x**2 - 2


raiz = secante(funcao, 1, 2, 3)
print(raiz)
