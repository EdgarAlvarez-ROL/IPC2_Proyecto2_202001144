from numpy import equal

class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None
        self.anterior = None


class unidadMilitar:
    def __init__(self, fila, columna, capacidad) -> None: #
        self.fila = fila
        self.columna = columna
        self.capacidad = capacidad
    
    def getFila(self):
        return self.fila



class Ciudad:
    def __init__(self, nombre, filas, columnas, todo_papa):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.todo_papa = todo_papa

    def getNombre(self):
            return self.nombre

    def getFilas(self):
            return self.filas

    def getColumnas(self):
            return self.columnas

    def getTodo_papa(self):
            return self.todo_papa

    



    class lista_Militares:
        def __init__(self):
            self.root = None

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
        
        def return_lista(self):
            if self.root is None:
                print("La lista esta vacia")
                return
            else:
                apuntador = self.root
                while apuntador is not None:
                    print(apuntador.elemento.getFila(), " ")
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







"""Tiene todas las ciudades como objeto"""
class doubleList:
    def __init__(self):
        self.root = None

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

    """"""
    def print_Data_Ciudades(self,numero):
        data = ''
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                if numero == 1:
                    print(apuntador.elemento.getNombre(), " ")
                elif numero == 2:
                    print(apuntador.elemento.getFilas(), " ")
                elif numero == 3:
                    print(apuntador.elemento.getColumnas(), " ")
                elif numero == 4:
                    print(apuntador.elemento.getTodo_papa(), " ")
                # print(apuntador.elemento, " ")
                apuntador = apuntador.siguiente
                # break
        # return 
    """"""
    """"""
    def return_infoEspecifica(self,numero):
        data = ''
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                if numero == 1:
                    data += apuntador.elemento.getNombre() + " "
                elif numero == 2:
                    data += str(apuntador.elemento.getFilas()) + " "
                elif numero == 3:
                    data += str(apuntador.elemento.getColumnas()) + " "
                elif numero == 4:
                    data += str(apuntador.elemento.getTodo_papa()) + " "
                # print(apuntador.elemento, " ")
                apuntador = apuntador.siguiente
                # break
        return data
    """"""
    """"""
    def return_Data_Ciudad(self, nombreC):
        data = ''
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                if nombreC == (apuntador.elemento.getNombre()):
                    data += str(apuntador.elemento.getFilas()) + "Y"
                    data += str(apuntador.elemento.getColumnas()) + "Y"                
                    data += str(apuntador.elemento.getTodo_papa()) + "Y"
                # print(apuntador.elemento, " ")
                apuntador = apuntador.siguiente
                # break
        return data
        """"""

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

"""
nuevaListaD = doubleList()

nuevaListaD.insertar_lista_vacia(50)
print("Prueba 0 insertar el primer elemento")
nuevaListaD.imprimir_listaD()

nuevaListaD.insertar_inicio(10)
nuevaListaD.insertar_inicio(5)
nuevaListaD.insertar_inicio(18)

print("Prueba 1 insertar elementos al inicio")
nuevaListaD.imprimir_listaD()

nuevaListaD.insertar_final(29)
nuevaListaD.insertar_final(39)
nuevaListaD.insertar_final(49)

print("Prueba 2 insertar elementos al final")
nuevaListaD.imprimir_listaD()

nuevaListaD.insertar_despues_elemento(50, 65)

print("Prueba 3 insertar el elemento 65 despues del 50")
nuevaListaD.imprimir_listaD()

nuevaListaD.insertar_antes_elemento(29,100)

print("Prueba 4 insertar el elemento 100 antes del 29")
nuevaListaD.imprimir_listaD()

nuevaListaD.eliminar_inicio()
print("Prueba 5 eliminar primer elemento")
nuevaListaD.imprimir_listaD()

nuevaListaD.eliminar_final()
print("Prueba 6 eliminar el ultimo elemento")
nuevaListaD.imprimir_listaD()

nuevaListaD.eliminar_elemento(65)
print("Prueba 7 eliminar el elemento 65")
nuevaListaD.imprimir_listaD()

print("Prueba 9 contar elementos en la lista")
print(nuevaListaD.contar_elementos())

"""