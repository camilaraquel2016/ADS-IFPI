from utilidades import *

import math

import turtle

bob = turtle.Turtle()


def isosceles(t, raio, angulo):
    y = raio * math.sin(angulo * math.pi / 180)

    t.rt(angulo)
    t.fd(raio)
    t.lt(90 + angulo)
    t.fd(2 * y)
    t.lt(90 + angulo)
    t.fd(raio)
    t.lt(180 - angulo)


def polypie(t, n, raio):
    angulo = 360.0 / n
    for i in range(n):
        isosceles(t, raio, angulo / 2)
        t.lt(angulo)

def draw_pie(t, n, raio):
    polypie(t, n, raio)
    t.pu()
    t.fd(raio * 2 + 10)
    t.pd()

bob.pu()
bob.bk(130)
bob.pd()

size = 40

draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, 8, size)

bob.hideturtle()
turtle.mainloop()