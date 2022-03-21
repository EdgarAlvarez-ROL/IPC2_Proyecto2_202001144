
from xml.dom import minidom

# vARIABLES GLOBALES

def lectorXML(rutanueva):
    global ruta, mydoc, pisos, nodoHijo, lista1, listaCodigos
    ruta = rutanueva

    mydoc = minidom.parse(ruta)            

    pisos = mydoc.getElementsByTagName('piso')      

    """Lo que esta comentado de PRINT NO TOCAR"""
    # Intentando leer los pisos
    for x in pisos:
        if x.hasAttribute("nombre"):
            """print("\nnombre:", x.getAttribute("nombre"))"""
            nodoHijo.nombre = x.getAttribute("nombre")

            # elemento de R
            lasR = x.getElementsByTagName('R')[0]
            """print(lasR.nodeName, ':', str.strip(lasR.childNodes[0].data))"""
            nodoHijo.R = (str.strip(lasR.childNodes[0].data))
            # listaNombres.insertar_fin(str.strip(lasR.childNodes[0].data))

            # elemento de C
            lasC = x.getElementsByTagName('C')[0]
            """print(lasC.nodeName, ':', str.strip(lasC.childNodes[0].data))"""
            nodoHijo.C = (str.strip(lasC.childNodes[0].data))

            # elemento de F
            lasF = x.getElementsByTagName('F')[0]
            """print(lasF.nodeName, ':', str.strip(lasF.childNodes[0].data))"""
            nodoHijo.F = (str.strip(lasF.childNodes[0].data))

            # elemento de S
            lasS = x.getElementsByTagName('S')[0]
            """print(lasS.nodeName, ':', str.strip(lasS.childNodes[0].data))"""
            nodoHijo.S = (str.strip(lasS.childNodes[0].data))

            # Instancio el minidom que leera los patron dentro del xml no es necesario poner patrones ya que ira directo a la clase que quiero y sus datos
            patrones = x.getElementsByTagName('patron')
            # print('numero de patrones')
            # print(len(patrones))

            for i in range(len(patrones)):
                cod = patrones[i].getAttribute('codigo')
                patronPiso = str.strip(patrones[i].childNodes[0].data)
                varCod = cod+' '+(str.strip(patronPiso))
                # print('codigo :'+cod)
                # print('patron :'+varCod)

                nodoHijo.codigos.insertar_fin_cua(varCod)

            # nodoHijo.codigos = listaCodigos


            lista1.insertar_fin((nodoHijo))
            nodoHijo = ListaSimpleDentro.nodoHJjo('','','','','','')
    
    # lista1.ordenamiento()
    print('\nDatos analizados correctamente\n')

