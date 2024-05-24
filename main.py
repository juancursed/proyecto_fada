import numpy as np
import matplotlib.pyplot as plt


#----EJEMPLOS DE PLOTEAR
plt.plot([-10, 10], [0,0], color = 'black')
plt.plot([0,0], [-10, 10], color = 'black')

#plt.plot([4.9, 5], [0,0], color = 'red')
#plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
#ax = plt.axis((0, 6, 0, 20))


#---EJEMPLO PUNTOS
x = [-2, 2, 5, 2, 4]
y = [6, 3, 7, 6, 3]
colors = ['red', 'blue', 'green', 'purple', 'orange']
sizes = [10]


#--------------------- Crear el gráfico de dispersión
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.plot([x[0], x[1]], [y[0], y[1]], color  = 'red')

#--------------------- Añadir títulos y etiquetas
plt.title("Gráfico de Dispersión Personalizado")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
