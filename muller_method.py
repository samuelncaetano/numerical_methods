import math
import pandas as pd


def muller(f, x0, x1, x2, i):
    table_data = []

    for i in range(1, i + 1):
        h0 = x1 - x0
        h1 = x2 - x1

        delta0 = (f(x1) - f(x0)) / h0
        delta1 = (f(x2) - f(x1)) / h1

        a = (delta1 - delta0) / (h1 + h0)
        b = a * h1 + delta1
        c = f(x2)

        discriminant = math.sqrt(b**2 - 4*a*c)
        if abs(b + discriminant) > abs(b - discriminant):
            den = b + discriminant
        else:
            den = b - discriminant

        x3 = x2 + (-2 * c) / den

        table_data.append([i, x0, x1, x2, x3, h0, h1,
                          delta0, delta1, a, b, c, f(x0), f(x1), f(x2), f(x3)])

        x0, x1, x2 = x1, x2, x3

    table = pd.DataFrame(table_data, columns=[
                         'Iteração', 'x0', 'x1', 'x2', 'x3', 'h0', 'h1',
                         'delta0', 'delta1', 'a', 'b', 'c', 'f(x0)', 'f(x1)', 'f(x2)', 'f(x3)'])
    return table


# Exemplo de uso
def funcao_exemplo(x):
    return x**3 - 13*x - 12


raiz = muller(funcao_exemplo, 5, 6, 7, 6)
print(raiz)
