from __future__ import division
from email.headerregistry import ContentTransferEncodingHeader
from turtle import shape
from graphviz import Digraph
from graphviz import Graph



dot = Digraph(comment='creadorimagen')



def crearGraficoEntrada(letras, filas, columnas):

    lx = letras
    fx = filas
    cx = columnas

    cua = escritorLabel(lx, fx, cx)


    
    dot.node('patron', label='<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">' + cua +'</TABLE>>')
    # print(dot.source)  
    dot.render('test-output/test.gv', view=True)



def escritorLabel(letras, filas, columnas):
    text = ''
    filas = int(filas)
    columnas = int(columnas)
    contador = 0
    
    characters = "'+-|\n"

    for x in range(len(characters)):
        letras = letras.replace(characters[x],"")
    
    # print(letras)
    
    for cosas in letras:
        if contador == 0:
            text += '<TR>' 
            pass
        

        if cosas == '#':
            text += '<TD BGCOLOR="black">*</TD>'
        elif cosas == ' ':
            text += '<TD BGCOLOR="white"> </TD>'
        elif cosas == 'e':
            text += '<TD BGCOLOR="blue">C</TD>'
        elif cosas == 's':
            text += '<TD BGCOLOR="green">E</TD>'
        elif cosas == 'x':
            text += '<TD BGCOLOR="yellow">X</TD>'
        # elif cosas == '+':
        #     text += '<TD BGCOLOR="white">+</TD>'
        # elif cosas == '-':
        #     text += '<TD BGCOLOR="white">-</TD>'

        contador += 1

        if contador == columnas:
            text += '</TR>' 
            contador = 0
    """"""  
    return text


letters = """
+----------+
|##########|
|### # e  #|
|### ######|
|### ######|
|### #    #|
|s   ######|
|### ######|
|### ######|
|### ######|
|###      #|
+----------+"""

# crearGraficoEntrada(letters,'10','10')
# escritorLabel(letters,'10','10')

# print(letters[0])