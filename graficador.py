from __future__ import division
from turtle import shape
from graphviz import Digraph
from graphviz import Graph

# p = Graph(name='parent')
# p.edge('spam', 'eggs')

# with p.subgraph(name='child', node_attr={'shape': 'box'}) as c:
#     c.edge('foo', 'bar')


# p.subgraph(c)
# p.view()


#  ESCRITOR DIGRAPH DOT
dot = Digraph(comment='creadorimagen')

# dot.node('A', 'King Arthur')
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')
# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')

# dot.node('Nodo0', 'A')
# dot.node('Nodo1', 'B', shape='box', style='filled', fillcolor='black')

# print(dot.source)  






def crearGraficoEntrada(letras, filas, columnas):

    lx = letras
    fx = filas
    cx = columnas

    cua = escritorLabel(lx, fx, cx)
    

    # dot.node('abc', shape="record" ,label="<f0> one|<f1> two")

    # dot.node('node', shape='plaintext')
#     dot.node('structure', label="""<
# <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
#   <TR><TD>left</TD><TD PORT="f1">mid dle</TD><TD PORT="f2">right</TD></TR>

#   <TR><TD>left</TD><TD PORT="f1">mid dle</TD><TD PORT="f2">right</TD></TR>
# </TABLE>>""")

    dot.node('patron', label='<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">' + cua +'</TABLE>>')



    # print(dot.source)  
    dot.render('test-output/patronEntrada.gv', view=True)




def crearGraficoSalida(letras, filas, columnas):

    lx = letras
    fx = filas
    cx = columnas

    cua = escritorLabel(lx, fx, cx)
    

    # dot.node('abc', shape="record" ,label="<f0> one|<f1> two")

    # dot.node('node', shape='plaintext')
#     dot.node('structure', label="""<
# <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
#   <TR><TD>left</TD><TD PORT="f1">mid dle</TD><TD PORT="f2">right</TD></TR>

#   <TR><TD>left</TD><TD PORT="f1">mid dle</TD><TD PORT="f2">right</TD></TR>
# </TABLE>>""")

    dot.node('patron', label='<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">' + cua +'</TABLE>>')



    # print(dot.source)  
    dot.render('test-output/patronSalida.gv', view=True)




def escritorLabel(letras, filas, columnas):
    text = ''
    filas = int(filas)
    contador = 0
    for x in range(filas):
        text += '<TR>'
        # filasL = ((len(letras))/2)
        for y in range(int(columnas)):
            text +='<TD'
            if letras[contador] == 'B':
                text+= ' BGCOLOR="black"'
            text += '>'+ letras[contador] +'</TD>'
            contador+=1
        text += '</TR>' 

    return text




# oli = escritorLabel('BWBWWWWW',2,4)
# print(oli)