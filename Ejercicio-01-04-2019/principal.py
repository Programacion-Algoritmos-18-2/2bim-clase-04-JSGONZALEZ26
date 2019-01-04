from modelado.modelo import Equipo  # Importación de la clase Equipo
from manejoArchivos.archivo import MiArchivo, ArchivoEscribir  # Importación de las clases para manejo de archivos
from manejoArchivos.Operaciones import Operaciones  # Importación de las operaciones para ordenar los elementos


equipos = MiArchivo()  # Creación de los objetos
equiposOrdenados = ArchivoEscribir()
listaEquipos = equipos.obtenerInformacion()  # Se obtiene la información del archivo inicial
listaEquipos = [l.split("|") for l in listaEquipos]  # Se separa los elementos de la lista
listaNueva = []  # Creación de una nueva lista vacía
for l in listaEquipos:
    equipo = Equipo(l[0], l[1], l[2], l[3])  # Se crea nuevos objetos de la clase equipo
    listaNueva.append(equipo)  # Estos objetos se vuelven elementos de la lisa vacía
#    print(equipo)
#    equiposOrdenados.agregarInformacion(equipo)
opt = int(input("¿Cómo desea ordenar los equipos?:\n1. Nombre\n2. Número de campeonatos\n"))  # Variable para elegir como ordenar los elementos
newLista = Operaciones(listaNueva)  # Se crea el objeto que devolverá la lista ordenada
if opt == 1:  # Uso de un condicional para la selección del tipo de ordenación
    listaOrdenada = newLista.ordenar1()  # Se ordena la lista
    equiposOrdenados.agregarInformacion2()  # Se agrega un encabezado al nuevo documento
    for l in listaOrdenada:  # Se recorre la lista ordenada
        print(l)  # Referencia para mostrar en consola que la lista está ordenada
        equiposOrdenados.agregarInformacion(l)  # Agregar la informacion al nuevo archivo
elif opt == 2:  # Se repite el proceso de la opcion 1
    listaOrdenada = newLista.ordenar2()
    equiposOrdenados.agregarInformacion3()
    for l in listaOrdenada:
        print(l)
        equiposOrdenados.agregarInformacion(l)
equipos.cerrarArchivo()  # Se cierra el archivo original
equiposOrdenados.cerrarArchivo()  # Se cierra el archivo nuevo
