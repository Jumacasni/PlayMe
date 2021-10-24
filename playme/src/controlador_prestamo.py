from prestamo import Prestamo
from datetime import datetime

class ControladorPrestamo:

	def __init__(self):
		self.prestamos = []

	def crear_prestamo(self, id_juego):
		p = Prestamo(id_juego)
		self.prestamos.append(p)