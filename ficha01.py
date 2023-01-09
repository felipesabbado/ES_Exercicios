import random


# Criar uma lista de valores aleatórios
def lista_aleatoria():
    qtd = int(input("Digite a quantidade de elementos: "))
    lista = []
    for i in range(qtd):
        lista.append(random.random())
    return lista


# Determinar o maior, o menor, o somatório e a média de uma lista
def maior_menor_soma_media(lista):
    maior = lista[0]
    menor = lista[0]
    soma = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
        soma += lista[i]
    media = soma / len(lista)

    txt = "Maior: {}\tMenor: {}\tSoma: {}\tMedia: {}"

    return print(txt.format(maior, menor, soma, media))


# Calcular fatorial de um número (iterativo)
def fatorial_iterativo(n):
    fatorial = 1
    for i in range(n):
        fatorial *= i + 1
    return fatorial


# Calcular fatorial de um número (recursivo)
def fatorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)


# Criar uma lista de caracteres aleatórios
def lista_caracteres_aleatorios():
    qtd = int(input("Digite a quantidade de elementos: "))
    lista = []
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(qtd):
        lista.append(alfabeto[random.randrange(len(alfabeto))])
    return lista


# Criar uma matriz de números inteiros gerados aleatoriamente
def matriz_aleatoria():
    linhas = int(input("Digite o numero de linhas: "))
    colunas = int(input("Digite o numero de colunas: "))
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(random.randint(0, 99))
    return matriz


# Criar uma matriz quadrada de caracteres arbitrários (A-Z) aleatórios
def matriz_caracteres_aleatorios():
    qtd = int(input("Digite a quantidade de elementos: "))
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    matriz = []
    for i in range(qtd):
        matriz.append([])
        for j in range(qtd):
            matriz[i].append(alfabeto[random.randrange(len(alfabeto))])
    return matriz


# Imprimir matriz
def print_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], "\t", end="")
        print()


if __name__ == '__main__':
    # print(lista_aleatoria())

    # print(lista_aleatoria_intervalo())

    # maior_menor_soma_media(lista_aleatoria_intervalo())

    # fatorial = int(input("Digite um número: "))
    # print("Seu fatorial (iterativo) é: ", fatorial_iterativo(fatorial))
    # print("Seu fatorial (recursivo) é: ", fatorial_recursivo(fatorial))

    print(lista_caracteres_aleatorios())

    # print_matriz(matriz_aleatoria())

    # print_matriz(matriz_caracteres_aleatorios())
