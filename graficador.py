import numpy as np
import matplotlib.pyplot as plt
from typing import List

def planoCartesiano(max: int, Ncolor):
    
    #----------HACER PLANO CARTESIANO---------
    plt.plot([-max, max], [0,0], color = Ncolor) #Eje X
    plt.plot([0,0], [-max, max], color = Ncolor) #eje y

    #--------------------- Añadir títulos y etiquetas
    plt.title("Detector de figuras")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")


def plotPuntos(listaPuntos: List[tuple], set_color, set_size: int):
    for punto in listaPuntos:
        plt.scatter(punto[0], punto[1], color= set_color, s=set_size) 
    