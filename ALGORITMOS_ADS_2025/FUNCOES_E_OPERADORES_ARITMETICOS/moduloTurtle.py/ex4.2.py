import turtle

from utilidades import * 

bob = turtle.Turtle()

def petala(t, raio, angulo):
    for i in range(2):
        arco(t, raio, angulo)
        t.lt(180 - angulo)


def flor(t, n, raio, angulo):
    for i in range(n):
        petala(t, raio, angulo)
        t.lt(360.0 / n) 


def mover(t, tamanho):
    t.pu()
    t.fd(tamanho)
    t.pd()


mover(bob, -90)
flor(bob, 7, 80.0, 60.0)

mover(bob, 120)
flor(bob, 10, 40.0, 50.0)

mover(bob, 90)
flor(bob, 20, 140.0, 20.0)


bob.hideturtle()
turtle.mainloop()      


