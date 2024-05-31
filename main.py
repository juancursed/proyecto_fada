import numpy as np
import matplotlib.pyplot as plt
import algoritmo_triangulo as alg
import graficador as graf

#---------PLANO CARTESIANO---------
graf.planoCartesiano(10, 'black')
#fig, ax = plt.subplots()

#----------PLOTEAR PUNTOS----------
lista1 = [(1,1,'a'), (1,5,'b'), (5,1,'c'), (1,-2,'d'), (5,-2, 'e')]
lista2 = [(1,2,'a'), (4,2, 'b'), (4,4,'c'), (6,3,'d'), (2,1,'e'), (6,1,'f'), (2,4,'g'), (6,2,'h')]
graf.plotPuntos(lista1, 'red', 10)
    

vectores2, perpendiculares = alg.detectar_vectores(lista2)
lineas, otras_lineas = alg.hacerTriangulo(perpendiculares, lista2)

vectores1, perpen = alg.detectar_vectores(lista1)
lineas_angulo_rec, otros = alg.hacerTriangulo(perpen, lista1) 
con = 0

for nombre, (punto1, punto2) in lineas_angulo_rec:  
    x_value =[punto2[0], punto1[0]]
    y_value =[punto2[1], punto1[1]]
    print('iteracion ',con ,' : ',x_value, ' - ', y_value)
    plt.plot(x_value, y_value, label=nombre, color='blue')
    con+=1
    
for nombre, (punto1, punto2) in otros:  
    x_value =[punto2[0], punto1[0]]
    y_value =[punto2[1], punto1[1]]
    print('iteracion ',con ,' : ',nombre,' -- ' ,x_value, ' - ', y_value)
    plt.plot(x_value, y_value, label=nombre, color='blue')
    con+=1

print(vectores2)
     
plt.show()