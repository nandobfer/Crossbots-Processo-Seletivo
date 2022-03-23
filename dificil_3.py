import random
import math

def doc():
    """teste"""
    pass

# solução baseada em um circulo de raio 1 inscrito em um quadrado
# separando apenas o primeiro quadrante, se inserirmos pontos aleatoriamente dentro desse quadrado
# alguns estarão dentro do 1/4 de circulo e outros fora.
# a area do quadradinho é a quantidade total de pontos.
# a area do 1/4 de circulo é a quantidade de pontos que estão dentro do 1/4 de circulo
# a area do quadradinho também é igual a 1, pois seu lado é 1
# a area do 1/4 de circulo também é pi * r ao quadrado / 4, ou pi / 4, pois r = 1
# então pi = aprox 4 vezes a quantidade de pontos dentro do 1/4 de circulo dividido pela quantidade total de pontos

dotsTotal = 10000 # quantidade total de pontos, quanto maior, mais precisa é a estimação

def getPi(dotsTotal):
    dots = 0  # inicializando variavel que contará quantos pontos estão dentro do 1/4 de circulo
    for i in range(dotsTotal):  # inserindo pontos em posições aleatórias de 0 a 1
        x = random.random()
        y = random.random()

        dist = math.sqrt(x * x + y * y)  # calculando a distancia entre o ponto e a origem
        if dist <= 1:  # caso a distancia seja menor ou igual a 1, ele está no primeiro quadrante e no raio do 1/4 de circulo, caso espelhássemos e movessemos sua ponta para a origem
            dots += 1  # ou seja, faz parte do 1/4 de circulo
    pi = 4 * dots / dotsTotal
    return pi

print(getPi(dotsTotal))
print(doc.__doc__)