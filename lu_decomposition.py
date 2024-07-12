import numpy as np


def lu_decomposition(A):
    """
    Realiza a decomposição LU da matriz A usando o método de eliminação de Gauss.

    Parâmetros:
    A : Matriz dos coeficientes.

    Retorna:
    L : Matriz triangular inferior.
    U : Matriz triangular superior.
    """
    n = A.shape[0]
    L = np.eye(n)  # Matriz identidade de tamanho n
    U = A.copy()

    for i in range(n):
        # Seleciona o pivô
        pivot = U[i, i]

        # Elimina os elementos abaixo do pivô
        for j in range(i + 1, n):
            factor = U[j, i] / pivot
            U[j, i:] -= factor * U[i, i:]
            L[j, i] = factor

    return L, U


def lu_solve(L, U, b):
    """
    Resolve o sistema Ax = b utilizando a decomposição LU.

    Parâmetros:
    L : Matriz triangular inferior.
    U : Matriz triangular superior.
    b : Vetor de termos independentes.

    Retorna:
    d : Vetor solução d.
    x : Vetor solução x.
    """
    n = L.shape[0]
    d = np.zeros(n)

    # Substituição Progressiva
    for i in range(n):
        sum_ld = 0
        for j in range(i):
            sum_ld += L[i, j] * d[j]
        d[i] = b[i] - sum_ld

    x = np.zeros(n)

    # Substituição Regressiva
    for i in range(n-1, -1, -1):
        sum_ux = 0
        for j in range(i+1, n):
            sum_ux += U[i, j] * x[j]
        x[i] = (d[i] - sum_ux) / U[i, i]

    return d, x


# Exemplo prático
A = np.array([
    [2, 3, 1],
    [4, 7, 1],
    [2, 5, 3]
], dtype=float)

# Vetor de termos independentes
b = np.array([1, 3, 7], dtype=float)

# Realiza a decomposição LU
L, U = lu_decomposition(A)

# Resolve o sistema utilizando a decomposição LU
d, x = lu_solve(L, U, b)

print("Matriz L:")
print(L)
print("\nMatriz U:")
print(U)
print("\nMatriz d:")
print(d)
print("\nMatriz x:")
print(x)
