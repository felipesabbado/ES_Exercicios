from numeric_functions import *
from string_functions import *


# Interface para mostrar o maximo divisor comum entre dois números inteiros
def mdc_interface():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print("O máximo divisor comum entre {} e {} é {}.".format(a, b, mdc(a, b)))


# Interface para mostrar se um número é primo
def primo_interface():
    n = int(input("Digite um número para verificar se é primo: "))
    if primo(n):
        print("{} é primo.".format(n))
    else:
        print("{} não é primo.".format(n))


# Interface para mostrar a sequência de Fibonacci recursiva
def fibonacci_r_interface():
    n = int(input("Digite um número para mostrar a sequência de Fibonacci: "))
    print("A sequência de Fibonacci até {} é:".format(n))
    for i in range(n):
        print(i+1, "=>", fibonacci_r(i))
    print()


# Interface para mostrar a sequência de Fibonacci iterativa
def fibonacci_i_interface():
    n = int(input("Digite um número para mostrar a sequência de Fibonacci: "))
    print("A sequência de Fibonacci até {} é:".format(n))
    for i in range(n):
        print(i+1, "=>", fibonacci_i(i))
    print()


# Interface para mostrar o palíndromo
def palindromo_interface():
    frase = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
    if palindromo(frase):
        print("{} é um palíndromo.".format(frase))
    else:
        print("{} não é um palíndromo.".format(frase))


# Interface para mostrar os palindromos de um texto
def palindromo_texto_interface():
    pergunta = int(input("Você quer digitar um texto[1] ou gerar palavras aleatórias[2] "
                         "para verificar os palíndromos? "))
    if pergunta == 1:
        texto = input("Digite um texto para verificar se as palavras são palíndromas: ")
        palavras, palindromos = palindromo_texto(texto)
        print("Palavras do texto: ", palavras)
        print("Palavras palíndromas: ", palindromos)
    elif pergunta == 2:
        n_palavras = int(input("Quantas palavras você quer gerar? "))
        palavras = palavras_aleatorias(n_palavras)
        palindromos = palindromo_palavra(palavras)
        print("Palavras geradas: ", palavras)
        print("Palíndromos: ", palindromos)


# Interface para mostrar a frequência absoluta das letras de um texto
def frequencia_absoluta_interface():
    texto = input("Digite um texto para verificar a frequência absoluta das letras: ")
    frequencia = frequencia_absoluta(texto)
    print("Texto: {}".format(texto))
    for letra in frequencia:
        print(letra + ":", frequencia[letra], end=" | ")


# Interface para mostrar a frequência absoluta aprimorada
def frequencia_absoluta_aprimorada_interface():
    texto = input("Digite um texto para verificar a frequência absoluta das letras e números: ")
    frequencia = freq_abs_aprimorada(texto)
    print("Texto: {}".format(texto))
    for digito in frequencia:
        print(digito + ":", frequencia[digito], end=" | ")
