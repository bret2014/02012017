import turtle
from tkinter import *
t = turtle.Pen()
t.reset()
a=int(input("Ingrese numero de lados: "))
b = 360/a 
c = 360 - b
t = turtle.Pen()
t.reset()
if a <=3:
    print("No se puede dibujar la estrella")
elif a %2!=0:
    print("No se puede dibujar la estrella")
else:
    t.right(45)
    for i in range(a):
        t.forward(100)
        t.right(b)
        for i in range(3):
            t.forward(100)
            t.right(120)
        for i in range(4):
            t.forward(100)
            t.right(90)
                      
                
        
        
   
        


    
