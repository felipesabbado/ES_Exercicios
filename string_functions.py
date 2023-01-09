import random


# Criar uma lista de palavras aleatórias
def palavras_aleatorias(qtd):
    alfa_num = "abcdefghijklmnopqrstuvwxyz"
    palavras = []
    for i in range(qtd):
        palavra = ""
        n_letras = random.randint(2, 10)
        for j in range(n_letras):
            letra = random.randint(0, len(alfa_num)-1)
            palavra = palavra + alfa_num[letra]
        palavras.append(palavra)
    return palavras


# Verificar se uma frase é um palíndromo
def palindromo(frase):
    frase = frase.replace(" ", "")
    frase = frase.lower()
    return frase == frase[::-1]


# Verificar palíndromos em uma lista de palavras
def palindromo_palavra(lista):
    palindromos = []
    for palavra in lista:
        if palindromo(palavra):
            palindromos.append(palavra)
    return palindromos


# Verificar palíndromos de um texto
def palindromo_texto(texto):
    texto = texto.lower()
    palavras = texto.split(" ")
    palindromos = []
    for palavra in palavras:
        if palindromo(palavra):
            palindromos.append(palavra)
    return palavras, palindromos


# Definir uma função para determinar a frequência absoluta das letras de um texto
def frequencia_absoluta(texto):
    texto = texto.lower()
    letras = "abcdefghijklmnopqrstuvwxyz0123456789"
    frequencia = {}
    for letra in letras:
        frequencia[letra] = texto.count(letra)
    return frequencia


# Definir uma função aprimorada para determinar a frequência absoluta das letras e números de um texto
def freq_abs_aprimorada(texto):
    texto = texto.lower
    digitos = "abcdefghijklmnopqrstuvwxyz0123456789"
    frequencia = {}
    for digito in digitos:
        frequencia[digito] = texto.count(digito)
    return frequencia
