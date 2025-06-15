import turtle

import math

from utilidades import *

bob = turtle.Turtle()

raio = 100
bob.pu()
bob.fd(raio)
bob.lt(90)
bob.pd()
circulo(bob, raio)

turtle.mainloop()