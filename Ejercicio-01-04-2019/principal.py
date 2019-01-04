from modelado.modelo import Equipo
from manejoArchivos.archivo import MiArchivo, ArchivoEscribir
from manejoArchivos.Operaciones import Operaciones


equipos = MiArchivo()
equiposOrdenados = ArchivoEscribir()
listaEquipos = equipos.obtenerInformacion()
listaEquipos = [l.split("|") for l in listaEquipos]
listaNueva = []
for l in listaEquipos:
    equipo = Equipo(l[0], l[1], l[2], l[3])
    listaNueva.append(equipo)
#    print(equipo)
#    equiposOrdenados.agregarInformacion(equipo)
opt = int(input("¿Cómo desea ordenar los equipos?:\n1. Nombre\n2. Número de campeonatos ganados\n"))
newLista = Operaciones(listaNueva)
if opt == 1:
    listaOrdenada = newLista.ordenar1()
    equiposOrdenados.agregarInformacion2()
    for l in listaOrdenada:
        print(l)
        equipo = l
        equiposOrdenados.agregarInformacion(equipo)
elif opt == 2:
    listaOrdenada = newLista.ordenar2()
    equiposOrdenados.agregarInformacion3()
    for l in listaOrdenada:
        print(l)
        equipo = l
        equiposOrdenados.agregarInformacion(equipo)
equipos.cerrarArchivo()
equiposOrdenados.cerrarArchivo()
