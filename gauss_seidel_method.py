import numpy as np
import pandas as pd


def gauss_seidel(A, b, x0, tol, max_iter):
    """
    Executa o método de Gauss-Seidel.

    Parâmetros:
    A        : Matriz dos coeficientes.
    b        : Vetor dos termos constantes.
    x0       : Vetor inicial de aproximações.
    tol      : Tolerância para o critério de parada.
    max_iter : Número máximo de iterações.

    Retorna:
    x       : Vetor solução.
    k       : Número de iterações realizadas.
    history : Histórico das iterações com os valores de x e erros relativos.
    """

    n = len(b)
    x = x0.copy()
    history = []

    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]

        # Calcula os erros relativos
        errors = np.abs((x - x_old) / x)

        # Armazena os valores atuais e erros na história
        history.append(np.concatenate(([k + 1], x, errors)))
        
        # Critério de parada
        if np.allclose(x, x_old, rtol=tol):
            break
    
    columns = ['Iteração', 'x1', 'x2', 'x3', 'Erro x1', 'Erro x2', 'Erro x3']
    history_df = pd.DataFrame(history, columns=columns)
    return x, k + 1, history_df


# Definindo o sistema de equações
A = np.array([[4, 1, 2],
              [1, 3, 1],
              [2, 1, 3]], dtype=float)

b = np.array([4, 5, 6], dtype=float)

# Valores iniciais
x0 = np.zeros(len(b))

# Tolerância e número máximo de iterações
tol = 1e-10
max_iter = 1000

# Executando o método de Gauss-Seidel
sol, iterations, history_df = gauss_seidel(A, b, x0, tol, max_iter)

print(history_df)
print("Número de iterações:", iterations)
print("Solução:", sol)
