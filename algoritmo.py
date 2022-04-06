from __future__ import print_function
from glob import glob
from numpy import double
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

import pathGraficador
import random

""""""
class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None
        self.anterior = None

class doubleList:
    def __init__(self):
        self.root = None

    def retornar_elementoD(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                # print(apuntador.elemento, " ")
                temp = apuntador.elemento
                apuntador = apuntador.siguiente
        return temp

    def insertar_lista_vacia(self, dato):
        if self.root is None:
            nuevoNodo = Nodo(dato)
            self.root = nuevoNodo
        else:
            print("La lista no esta vacia")
    
    def insertar_inicio(self, dato):

        if self.root is None:
            self.insertar_lista_vacia(dato)
        else:
            nuevoNodo = Nodo(dato)
            nuevoNodo.siguiente = self.root
            self.root.anterior = nuevoNodo
            self.root = nuevoNodo
    
    def insertar_final(self, dato):

        if self.root is None:
            nuevoNodo = Nodo(dato)
            self.root = nuevoNodo
            return
        
        apuntador = self.root

        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente

        nuevoNodo = Nodo(dato)
        apuntador.siguiente = nuevoNodo
        nuevoNodo.anterior = apuntador
    
    def insertar_despues_elemento(self, x, dato):
        if self.root is None:
            print("La lista esta vacia")
        else:
            apuntador = self.root
            while apuntador is not None:

                if apuntador.elemento == x:
                    break
                apuntador = apuntador.siguiente
            
            if apuntador is None:
                print("El elemento no se encuentra en la lista")
            else:
                nuevoNodo = Nodo(dato)
                nuevoNodo.anterior = apuntador
                nuevoNodo.siguiente = apuntador.siguiente
                if apuntador.siguiente is not None:
                    apuntador.siguiente.anterior = nuevoNodo
                apuntador.siguiente = nuevoNodo
    
    def insertar_antes_elemento(self, x, dato):
        if self.root is None:
            print("La lista esta vacia")
        else:
            apuntador = self.root
            while apuntador is not None:
                if apuntador.elemento == x:
                    break
                apuntador = apuntador.siguiente
            
            if apuntador is None:
                print("Elemento no se encuentra en la lista")
            else:
                nuevoNodo = Nodo(dato)
                nuevoNodo.siguiente = apuntador
                nuevoNodo.anterior = apuntador.anterior

                if apuntador.anterior is not None:
                    apuntador.anterior.siguiente = nuevoNodo
                apuntador.anterior = nuevoNodo

    def imprimir_listaD(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                print(apuntador.elemento, " ")
                apuntador = apuntador.siguiente

    def lista_vacia(self):
        if self.root is None:
            return True
        else:
            return False
    
    def contar_elementos(self):
        apuntador = self.root
        cuenta = 0

        while apuntador is not None:
            cuenta = cuenta + 1
            apuntador = apuntador.siguiente
        return cuenta
    
    def eliminar_inicio(self):
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        
        if self.root.siguiente is None:
            self.root = None

        self.root = self.root.siguiente
        self.root.anterior = None
    
    def eliminar_final(self):
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        
        if self.root.siguiente is None:
            self.root = None
            return

        apuntador = self.root
        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente
        apuntador.anterior.siguiente = None
    
    def eliminar_elemento(self, x):
        if self.root is None:
            print("La lista esta vacia")
            return
        
        if self.root.siguiente is None:
            if self.root.elemento == x:
                self.root = None
            else:
                print("Elemento no encontrado")
        
        if self.root.elemento == x:
            self.eliminar_inicio()
            return
        
        apuntador = self.root
        while apuntador.siguiente is not None:
            if apuntador.elemento == x:
                break
            apuntador = apuntador.siguiente
        
        if apuntador.siguiente is not None:
            apuntador.anterior.siguiente = apuntador.siguiente
            apuntador.siguiente.anterior = apuntador.anterior
        else:
            if apuntador.elemento == x:
                self.eliminar_final()
            else:
                return print("Elemento no encontrado")
""""""
# matrix = [
#   [1, 0, 0, 1],
#   [1, 0, 0, 1],
#   [1, 0, 0, 1],
#   [1, 1, 1, 1]
# ]
listaMatrix = doubleList()


# matrix = []
x = 0
y = 0



def hacerMatrix(todo_papa, xEntrada, yEntrada, xFinaL, yFinal, filas, columnas):
    global listaMatrix
    
    # listatemp = doubleList()
    # matrix = []
    cuaT = todo_papa
    cuaT2 = todo_papa
    trra = ''
    # temp = []
    contador = 0
    for cosas in todo_papa:
        for x in cosas:
            if x == '*':
                x = 0
                trra += "0 "
            elif x == ' ':
                x = 1
                trra += "1 "
            elif x == 'M':
                x = 0
                trra += "0 "
            elif x == 'R':
                x = 0
                trra += "0 "
            elif x == 'E':
                x = 1
                trra += "1 "
            elif x == 'C':
                x = 1
                trra += "1 "
            # temp.append(x)
            cuaT[contador] = trra.rstrip()
            # cuaT[contador]

        # print(cuaT[contador])
        contador += 1

        trra = ''
       

    #   matrix.append(temp)
    #   temp = []

    # print(matrix)
    contador = 0
    for cosas in cuaT:
        temp = cosas.split(' ') 
        cuaT2[contador] = temp
        contador += 1
    
    # print(cuaT2)
    a = int(xEntrada)
    b = int(yEntrada)
    c = int(xFinaL)
    d = int(yFinal)

    usar(cuaT2, a,b,c,d,filas,columnas)

   

def hacerMatrix2(todo_papa, xEntrada, yEntrada, xFinaL, yFinal, filas, columnas):
    global listaMatrix
    
    # listatemp = doubleList()
    # matrix = []
    cuaT = todo_papa
    cuaT2 = todo_papa
    trra = ''
    # temp = []
    contador = 0
    for cosas in todo_papa:
        for x in cosas:
            if x == '*':
                x = 0
                trra += "0 "
            elif x == ' ':
                x = 1
                trra += "1 "
            elif x == 'M':
                x = 1
                trra += "1 "
            elif x == 'R':
                x = 1
                trra += "1 "
            elif x == 'E':
                x = 1
                trra += "1 "
            elif x == 'C':
                x = 0
                trra += "0 "
            # temp.append(x)
            cuaT[contador] = trra.rstrip()
            # cuaT[contador]

        # print(cuaT[contador])
        contador += 1

        trra = ''
       

    #   matrix.append(temp)
    #   temp = []

    # print(matrix)
    contador = 0
    for cosas in cuaT:
        temp = cosas.split(' ') 
        cuaT2[contador] = temp
        contador += 1
    
    # print(cuaT2)
    a = int(xEntrada)
    b = int(yEntrada)
    c = int(xFinaL)
    d = int(yFinal)

    usar(cuaT2, a,b,c,d,filas,columnas)

  

def usar(matrix, xEntradau, yEntradau, xFinalu, yFinalu, filas, columnas):
    global listaMatrix
    grid = Grid(matrix=matrix)

    start = grid.node(xEntradau, yEntradau)
    end = grid.node(xFinalu, yFinalu)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)

    # print('operations:', runs, 'path length:', len(path))
    # print(grid.grid_str(path=path, start=start, end=end))

    """"""
    # other_matrix = []
    # other_matrix.append((grid.grid_str(path=path, start=start, end=end)))
    # print(other_matrix[0])
    # for C in other_matrix[0]:
    #   if C == 's':
    #     print('SI SIRVE')
    """"""

    nuevaListaD = doubleList()
    nuevaListaD.insertar_final(grid.grid_str(path=path, start=start, end=end))
    # nuevaListaD.imprimir_listaD()
    letters = nuevaListaD.retornar_elementoD()

    # print(letters)
    if len(path) == 0:
        print('No se pudo rescatar al Civil -F')
    pathGraficador.crearGraficoEntrada(letters,filas,columnas)


