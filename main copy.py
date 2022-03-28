from csv import unix_dialect
from xml.dom import minidom
from numpy import TooHardError

from sqlalchemy import null                     # Importamos la libreria

import tkinter
from tkinter import filedialog
import re
import xml.etree.ElementTree as ET

import ListaDoble
import escritorGraphviz


obj_Ciudad = ListaDoble.Ciudad('','','')
lista_Ciudades = ListaDoble.doubleList()


# VARIABLES GLOBALES
todo_papa = ''
ruta = ''



def lectorXML(rutanueva):
    global todo_papa, ruta
    ruta = rutanueva

    sub2 = 0

    mydoc = minidom.parse(ruta)            

    ciudades = mydoc.getElementsByTagName('ciudad')      

    """Lo que esta comentado de PRINT NO TOCAR"""
    # Intentando leer los pisos
    for x in ciudades:
        todo_papa=''
        if x.getElementsByTagName("nombre")[0]:
            e_nombre = x.getElementsByTagName('nombre')[0]
            print(e_nombre.nodeName, ':', str.strip(e_nombre.childNodes[0].data))

            filas = e_nombre.getAttribute('filas')
            columnas = e_nombre.getAttribute('columnas')
            # print('Filas: ' + str(filas))
            # print('Filas: ' + str(columnas))
            
            contF = 1
            for filitas in x.getElementsByTagName('fila'):
                n_fila = filitas.getAttribute('numero')
                # print('#fila: '+ str(n_fila) + ' Data: '+  filitas.childNodes[0].data)
                todo_papa += filitas.childNodes[0].data
                contF += 1
            
            """"""
            # print(todo_papa)
            obj_Ciudad(e_nombre,filas,columnas)
            lista_Ciudades.insertar_final(obj_Ciudad)
            # lista_Ciudades.imprimir_lista()


            # e_fila = x.getElementsByTagName('fila')[0]
            # n_fila = e_fila.getAttribute('numero')
            # print('# Fila: ' + n_fila)
            # d_fila = e_fila.childNodes[0].data
            # print(e_fila.nodeName, ':', str(d_fila))


            unidadesTexto = divisorMapeador(todo_papa)

            
            for unidades in x.getElementsByTagName('unidadMilitar'):
                n_u_fila = unidades.getAttribute('fila')
                n_u_columna = unidades.getAttribute('columna')
                """"""
                # print('#fila: '+ str(n_u_fila) + ' #columna: ' + str(n_u_columna) + ' Data: '+  unidades.childNodes[0].data)
                
                nuevaCadena = ''
                cont = 0
                for cosas in unidadesTexto[int(n_u_fila)-1]:
                    # print('primero: '+cosas)
                    
                    if cont == (int(n_u_columna)-1):
                        # print(cosas)
                        cosas = 'M'
                        # print(cosas)
                    nuevaCadena += cosas
                    cont+=1
                unidadesTexto[int(n_u_fila)-1]=nuevaCadena
                

                
   
               
            """"""
            # print(unidadesTexto)
            # escritorGraphviz.crearGraficoEntrada(unidadesTexto,filas,columnas)
            """"""
        # todo_papa = ''
        print('\nDatos Ciudades correctamente\n')




    

    robots = mydoc.getElementsByTagName('robot')      
    for x in robots:
        if x.getElementsByTagName("nombre")[0]:
            e_r_nombre = x.getElementsByTagName('nombre')[0]
            # print(e_r_nombre.nodeName, ':', str.strip(e_r_nombre.childNodes[0].data))

            tipo = e_r_nombre.getAttribute('tipo')
            capacidad = e_r_nombre.getAttribute('capacidad')
            # print('Tipo: ' + str(tipo))
            # print('Capacidad: ' + str(capacidad))
            print('\n')

    # divisorMapeador(todo_papa)




def divisorMapeador(texto):
    
    d_texto =  texto.split('""')
    caracter = '\"'

    for x in range(len(d_texto)):
        d_texto[x] = d_texto[x].replace(caracter,'')
    
    # print(d_texto)
    return d_texto


# lectorXML('Entrada.xml')
# lista_Ciudades.imprimir_lista()
# divisorMapeador('"hoal""****   **C""asd *fasdf""hili                "')




def menu():
    salir = False

    while not salir:
        print('====================== MENU ======================')
        print ("1. Ingrese la ruta de su archivo XML            |")
        print ("2. Ver Ciudades                                 |")
        print ("3. Salir                                        |")
        print ("----Elige una opcion")
        print('==================================================')
        opcion = pedirNumeroEntero()

        if opcion == 1:
            print('\n \n======================OPCION 1======================')
            # ruta = input("introduzca a ruta de tu archivo XML a analizar:    ")
            # print('\nsu ruta escogida es: '+ruta)
            fn_abrirArchivo()
            print('Analizando XML...')
            lectorXML(ruta)


        elif opcion == 2:
            print('\n \n==================OPCION 2 -PISOS-==================')
            print('--Escoja una ciudad para ver su informacion--')
            # Mostrar CIUDADES





            
        elif opcion == 3:
            salir = True


def fn_abrirArchivo():
    global ruta
    ruta = filedialog.askopenfilename(title="Abrir", filetypes = (("Unicamente xml", "*.xml"), ("Archivos xml", "*.xml")) )
    


def pedirNumeroEntero():

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('ERROR, introduce un numero entero: ')
    
    return num



menu()