from typing import List


lista1 = [(3,5,'a'), (5,3,'b'), (7,5,'c'), (9,3,'c'), (6,2, 'd')]
lista2 = [(1,2,'a'), (4,2, 'b'), (4,4,'c'), (6,3,'d'), (2,1,'e'), (6,1,'f'), (2,4,'g'), (6,2,'h')]

def detectar_vectores(listaPuntos: List[tuple]):
    """
    Recibe una lista de puntos y devuelve una lista de vectores con angulo recto
    """
    vectores = []
    vectores_nombre=[]
    
    for i in range(len(listaPuntos)):
    
        for j  in range(i+1, len(listaPuntos)):
            #print(i,j)
            
            if (listaPuntos[i][0] == listaPuntos[j][0]) or (listaPuntos[i][1] == listaPuntos[j][1]):
                
                vectores.append((listaPuntos[j][0] - listaPuntos[i][0],  listaPuntos[j][1] - listaPuntos[i][1], listaPuntos[j][2] + listaPuntos[i][2]))
                
                vectores_nombre.append(listaPuntos[j][2] + listaPuntos[i][2])

                
    return vectores, vectores_nombre


#----------Crear una función que recorra vectores_perpendiculares y busque los puntos perpendiculares correspondientes
def hacerTriangulo(vectores_perpendiculares, lista_puntos):
    
    puntos_dict = {nombre: (x, y) for x, y, nombre in lista_puntos}
    puntos_faltantes = []
    resultados = []
    
    for nombre in vectores_perpendiculares:
        punto1_nombre = nombre[0]
        punto2_nombre = nombre[1]
        punto1 = puntos_dict.get(punto1_nombre)
        punto2 = puntos_dict.get(punto2_nombre)       
        if punto1 and punto2:
            resultados.append((nombre, (punto1, punto2)))
            
            
#----------------------------mejorar esta vuelta
    for i in range(len(vectores_perpendiculares)):
        for j in range(i + 1, len(vectores_perpendiculares)):
            
            p1 = vectores_perpendiculares[i]
            p2 = vectores_perpendiculares[j]
            
            if p1[1] == p2[0]:
                punto1 = puntos_dict.get(p1[0])
                punto2 = puntos_dict.get(p2[1])
                puntos_faltantes.append((p1[0] +p2[1], punto1, punto2))
                #print(punto1,'  ', punto2)
                
            if p1[0] == p2[1]:
                punto1 = puntos_dict.get(p1[1])
                punto2 = puntos_dict.get(p2[0])
                puntos_faltantes.append((p1[1] + p2[0], (punto1, punto2)))
                #print(punto1,'  ', punto2)
            
            if p1[0] == p2[0]:
                punto1 = puntos_dict.get(p1[1])
                punto2 = puntos_dict.get(p2[1])
                puntos_faltantes.append((p1[1] + p2[1], (punto1, punto2)))
                #print(punto1,'  ', punto2)
            
            if p1[1] == p2[1]:
                punto1 = puntos_dict.get(p1[0])
                punto2 = puntos_dict.get(p2[0])
                puntos_faltantes.append((p1[0] + p2[0], (punto1, punto2)))
                #print(punto1,'  ', punto2)
        

    
    return resultados, puntos_faltantes

    
    
vectores, vectores_per = detectar_vectores(lista2)

resultados, otros = hacerTriangulo(vectores_per, lista2)

print('otros: ',otros)
# print(vectores)
print(vectores_per)