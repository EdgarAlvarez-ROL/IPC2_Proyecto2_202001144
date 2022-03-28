
from numpy import equal


class node:
    def __init__(self, data = None, siguiente = None, nodoHijin = None): #Constructor
        self.data = data #Este el atributo, puede mas atributo
        self.siguiente = siguiente  #Apunta al siguiente nodo
        self.nodoHijin = nodoHijin




class nodoHJjo:
    def __init__(self, nombre, R, C, F, S, codigos) -> None: #
        self.nombre = nombre
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.codigos = nodoHJjo.Codigoss()

    def datos(self):
        print(self.nombre)
        print(self.R)
        print(self.C)
        print(self.F)
        print(self.S)
        self.codigos.imprimir_lista()

    def returnAllData(self):
        returnName = self.nombre
        returnR = self.R
        returnC = self.C
        returnF = self.F
        returnS = self.S
        returnCodigitos = self.codigos.returnCodigos()

        # t=nodoHJjo(name,R,C,F,S,codigitos)
        return returnName,returnR,returnC,returnF,returnS,returnCodigitos


    def getNombre(self):
        return self.nombre

    def getR(self):
        return self.R

    def getC(self):
        return self.C

    def getF(self):
        return self.F
    
    def getS(self):
        return self.S

    def getCodigos(self):
        codigitos = self.codigos.returnCodigos()
        return codigitos
    
    def datos2(self):
        # print(self.nombre)
        print('R: '+self.R)
        print('C: '+self.C)
        print('F: '+self.F)
        print('S: '+self.S)
        
    
    # Creamos la clase Codigoss que esta dentro de la clase nodoHijo
    class Codigoss: 
        def __init__(self):#constructor
            self.root = None # root es el primer apuntador

        # Método para agregar elementos en el frente de la lista simple
        def insertar_inicio(self, data):
            self.root = node(data=data, siguiente=self.root)  

        # Método para agregar elementos al final de la lista simple
        def insertar_fin_cua(self, midato): 

            if self.root is None: #Si root es nula. Esto pasa si y si solo es el primer nodo que se esta agregando a la lista
                self.root = node(data=midato) #Creando mi primer y asignando a root
                return #finaliza
            #En caso de que root ya tenga un nodo
            auxRoot = self.root
            while auxRoot.siguiente: #Mientras exista un nodo
                auxRoot = auxRoot.siguiente
            auxRoot.siguiente = node(data=midato) #mi nuevo nodo

        # Método para imprimir la lista de nodos
        def imprimir_lista( self ):
            nodeAux = self.root #Obtiene raiz o inicial de mi lista
            while nodeAux != None:
                print(nodeAux.data)
                nodeAux = nodeAux.siguiente

        def vaciarLista (self):
            nodeAux = self.root
            while nodeAux != None:
                nodeAux.data = None
                nodeAux = nodeAux.siguiente 

        def returnCodigos(self):
            nodeAux = self.root
            a=''
            while nodeAux != None:
                a += (nodeAux.data + ' ')
                nodeAux = nodeAux.siguiente
            return a


        def obtenerPatron(self, codigoBuscar):
            nodeAux = self.root 
            x = ''
            while nodeAux != None:
                nodoNombre = nodeAux.data
                if nodoNombre == codigoBuscar:
                    x = nodeAux.siguiente
                nodeAux = nodeAux.siguiente
            return x

        """"""




"""# Creamos la clase lista_simple"""
class lista_simple: 
    def __init__(self): # constructor
        self.root = None # root es el primer apuntador

    
    def insertar_inicio(self, data):
        self.root = node(data=data, siguiente=self.root)  

    
    def insertar_fin(self, midato): 

        if self.root is None: 
            self.root = node(data=midato) 
            return 
        
        auxRoot = self.root
        while auxRoot.siguiente: 
            auxRoot = auxRoot.siguiente
        auxRoot.siguiente = node(data=midato) 

    
    def imprimir_lista( self ):
        nodeAux = self.root 
        while nodeAux != None:
            print('Nodo: ',nodeAux.data)
            nodeAux = nodeAux.siguiente

    def vaciar_lista(self):
        nodeAux = self.root 
        while nodeAux != None:
            nodeAux.data = ''
            nodeAux = nodeAux.siguiente
        print('\nLista Vaciada correctamente\n')

            
    # OBTENER COSAS
    def imprimir_nodosHijo( self ):
        nodeAux = self.root 
        while nodeAux != None:
            nodeAux.data.datos()
            print("")
            nodeAux = nodeAux.siguiente

    def imprimir_1soloNodo( self, nombrel ):
        nodeAux = self.root 
        x = ''
        while nodeAux != None:
            nodoNombre = nodeAux.data.getNombre()
            if nodoNombre == nombrel:
                nodeAux.data.datos2()
            nodeAux = nodeAux.siguiente

    
    def obtenerNombres(self):
        nodeAux = self.root 
        while nodeAux != None:
            print(nodeAux.data.getNombre())
            nodeAux = nodeAux.siguiente


    def obtenerCodigos(self):
        nodeAux = self.root 
        while nodeAux != None:
            print(nodeAux.data.getCodigos())
            nodeAux = nodeAux.siguiente
            
    
    def obtenerTodo(self):
        nodeAux = self.root 
        while nodeAux != None:
            x = (nodeAux.data.returnAllData())
            print(x,type(x))
            nodeAux = nodeAux.siguiente


    def obtener1soloNodo(self, nombrel):
        nodeAux = self.root 
        x = ''
        while nodeAux != None:
            nodoNombre = nodeAux.data.getNombre()
            if nodoNombre == nombrel:
                x = nodeAux.data.returnAllData()
            nodeAux = nodeAux.siguiente


        return x


