import pandas as pd


def secante_modificado(f, x0, d, i):
    table_data = []
    for i in range(1, i + 1):
        fx0 = f(x0)
        fd = f(x0 + d)
        xr = x0 - ((d * fx0) / (fd - fx0))
        table_data.append([i, x0, d, fx0, fd, xr])
        x0 = xr

    table = pd.DataFrame(table_data, columns=[
                         'Iteração', 'x', 'delta', 'fx', 'fd', 'xr'])
    return table


# Exemplo de uso
def funcao_exemplo(x):
    return x**3 - 2*x**2 - 4


raiz = secante_modificado(funcao_exemplo, 3, 0.01, 4)
print(raiz)
