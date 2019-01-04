class Operaciones(object):  # Clase que contiene los procesos para ordenar

    def __init__(self, listado):
        self.equiposOrdenados = listado

    def ordenar1(self):
        return sorted(self.equiposOrdenados, key=lambda equipo: equipo.getNombre())

    def ordenar2(self):
        return sorted(self.equiposOrdenados, key=lambda equipo: equipo.getCampeonatos())
