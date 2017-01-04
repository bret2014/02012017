import turtle
a=int(input("Ingrese el numero de puntas: "))
if(a%2==0):
    if a >=4:         
        if a ==6:
            b=180/a
            c=b*10
            t= turtle.Pen()
            t.reset()
            for x in range (a):
                t.forward(100)
                t.left(c)
                t.forward(100)
                t.left(120)
        else:
            b=180/a
            c=b*10 
            t= turtle.Pen()
            t.reset()
            for x in range (a):
                t.forward(100)
                t.left(c)
    
else:
    print("Solo funciona para impares")
   

