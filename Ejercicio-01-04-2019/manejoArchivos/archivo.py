import codecs


class MiArchivo:

    def __init__(self):
        self.archivo = codecs.open("Archivos/informacion.csv", "r")

    def obtenerInformacion(self):
        return self.archivo.readlines()

    def cerrarArchivo(self):
        self.archivo.close()


class ArchivoEscribir:
    def __init__(self):
        self.archivo = codecs.open("Archivos/informacionOrdenada.csv", "a")

    def agregarInformacion(self, p):
        self.archivo.write("%s-%s-%d-%d \n" % (
            p.getNombre(),
            p.getCiudad(),
            p.getCampeonatos(),
            p.getNumJugadores()))

    def agregarInformacion2(self):
        self.archivo.write("Equipos Ordenados Alfabeticamente\n")

    def agregarInformacion3(self):
        self.archivo.write("Equipos Ordenados Por Número de Campeonatos\n")

    def cerrarArchivo(self):
        self.archivo.close()
