class Equipo(object):

    def __init__(self, nom, ciudad, camp, numJ):
        self.nombre = nom
        self.ciudad = ciudad
        self.campeonatos = int(camp)
        self.numJugadores = int(numJ)

    def setNombre(self, nom):
        self.nombre = nom

    def getNombre(self):
        return self.nombre

    def setCiudad(self, ciudad):
        self.ciudad = ciudad

    def getCiudad(self):
        return self.ciudad

    def setCampeonatos(self, camp):
        self.campeonatos = int(camp)

    def getCampeonatos(self):
        return self.campeonatos

    def setNumJugadores(self, numJ):
        self.numJugadores = int(numJ)

    def getNumJugadores(self):
        return self.numJugadores

    def __repr__(self):
        return "%s %s %d %d\n" % (self.getNombre(), self.getCiudad(), self.getCampeonatos(), self.getNumJugadores())
