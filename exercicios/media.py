import math
nt1 = float(input("Informe a NOTA 1: "))
nt2 = float(input("Informe a NOTA 2: "))
nt3 = float(input("Informe a NOTA 3: "))

media = (nt1 + nt2 + nt3) / 3

if(media >= 10 or media == 5 ):
    print(f"Você passou com {round(media)} valores")
else: 
     print(f"Você reprovou com {round(media)} valores :( ")