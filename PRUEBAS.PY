from cgi import print_arguments
from re import X
import ListaDoble
from ListaSimpleDentro import lista_simple

listaRobots = ListaDoble.lista_Robots()

robot1 = ListaDoble.Robot('','','')
robot1.tipo = 'ChapinFighter'
robot1.capacidad = 20
robot1.nombre ='Robocop'

robot3 = ListaDoble.Robot('','','')
robot3.tipo = 'ChapinFighter'
robot3.capacidad = 10
robot3.nombre ='MaxSteel'



robot2 = ListaDoble.Robot('','','')
robot2.tipo = 'ChapinRescue'
robot2.capacidad = 0
robot2.nombre ='Ironman'


robot4 = ListaDoble.Robot('','','')
robot4.tipo = 'ChapinRescue'
robot4.capacidad = 0
robot4.nombre ='OptimusPrime'



listaRobots.insertar_final(robot1)
listaRobots.insertar_final(robot2)
listaRobots.insertar_final(robot3)
listaRobots.insertar_final(robot4)

tiposRobots = listaRobots.return_infoEspecifica_ROBOTS(1)

list_tRbts = (tiposRobots).rstrip().split(' ')
cont = 0
for x in list_tRbts:
    print(str(cont) + ') ' + str(x))
    cont += 1


cont = 0
nCiud = input("ingrese el numero del robot: ")
dif_robots = ''
for x in list_tRbts:
    if cont == int(nCiud):
        dif_robots = listaRobots.return_Data_ROBOT(x)
        # listicaRobot = 
    cont += 1


dif_robots = (dif_robots[:-1].split('Y'))
print('Escoja su robot: ')

cont = 0
for x in dif_robots:
    if x.isnumeric():
        # cont += -1
        pass
    elif x!= '0':
        print(str(cont) + ') ' + str(x))
    cont += 1


cont = 0
nCiud = input("ingrese el su robot de rescate: ")
capacidad_rR = ''
for x in dif_robots:
    if cont == int(nCiud):
        capacidad_rR = listaRobots.return_Data_ROBOT(x)
        # listicaRobot = 
    cont += 1

print(capacidad_rR)