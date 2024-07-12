import numpy as np


def gauss_elimination(A, b):
    """
    Resolve um sistema de equações lineares Ax = b usando eliminação de Gauss.

    Parâmetros:
    A : Matriz dos coeficientes.
    b : Vetor dos termos independentes.

    Retorna:
    x: Vetor solução x.
    Ab: Matriz aumentada concatenando A e b
    """

    n = len(b)

    # Cria a matriz aumentada concatenando A e b
    Ab = np.hstack([A, b.reshape(-1, 1)])

    # Eliminação Progressiva
    for i in range(n):
        # Seleciona o pivô
        pivot = Ab[i, i]

        # Elimina os elementos abaixo do pivô
        for j in range(i + 1, n):
            factor = Ab[j, i] / pivot  # Calcula o fator multiplicador
            # Atualiza a linha j subtraindo o fator multiplicador vezes a linha i
            Ab[j, i:] -= factor * Ab[i, i:]

    # Substituição Regressiva
    x = np.zeros(n)  # Vetor solução inicializado com zeros
    for i in range(n-1, -1, -1):
        # Calcula a solução para a variável x[i]
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]

    return x, Ab


# Exemplo prático
A = np.array([
    [2, 3, -1],
    [4, 4, -3],
    [2, -3, 2]
], dtype=float)

b = np.array([1, 3, 4], dtype=float)

# Resolve o sistema de equações Ax = b
x, Ab = gauss_elimination(A, b)
print(Ab)
print(f"\nSolução do sistema: {x}")
