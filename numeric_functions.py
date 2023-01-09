import random


# Criar uma lista de valores aleatórios em determinado intervalo
def lista_aleatoria_intervalo():
    qtd = int(input("Digite a quantidade de elementos: "))
    n_min = int(input("Digite o valor minimo: "))
    n_max = int(input("Digite o valor maximo: "))
    lista = []
    for i in range(qtd):
        lista.append(random.randint(n_min, n_max))
    return lista


# Criar uma função para determinar o máximo divisor comum entre dois números inteiros
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


# Determinar uma função para determinar se um número é primo
def primo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


# Criar uma função iterativa para gerar a sequência de Fibonacci
def fibonacci_i(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, a + b
        return b


# Criar uma função recursiva para gerar a sequência de Fibonacci
def fibonacci_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_r(n - 1) + fibonacci_r(n - 2)
