import math


def square(t, tamanho):
    for i in range(4):
        t.fd(tamanho)
        t.lt(90)


def poligonoParaArco(t, n, tamanho, angulo):
    for i in range(n):
        t.fd(tamanho)
        t.lt(angulo)


def poligono(t, n, tamanho):
    angulo = 360.0 / n
    poligonoParaArco(t, n, tamanho, angulo)


def arco(t, raio, angulo):
    arcoTamanho = 2 * math.pi * raio * abs(angulo) / 360
    n = int(arcoTamanho / 4) + 3
    medidaTamanho = arcoTamanho / n
    medidaAngulo = float(angulo) / n
    
    t.lt(medidaAngulo / 2)
    poligonoParaArco(t, n, medidaTamanho, medidaAngulo)
    t.rt(medidaAngulo / 2) 


def circulo(t, raio):
    arco(t, raio, 360)
