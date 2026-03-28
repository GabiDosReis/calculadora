import math
def soma(a,b):
    return a + b
def subtracao(a,b):
    return a - b
def divisao(a,b):
    return a / b
def multiplicacao(a,b):
    return a * b
def raiz(a):
    return math.sqrt(a)
def porcentagem(a, b):
    return (a * b) / 100
def raiz(a):
    if a < 0:
        return "Erro: raiz de número negativo"
    return math.sqrt(a)
def quadrado(a):
    return a ** 2