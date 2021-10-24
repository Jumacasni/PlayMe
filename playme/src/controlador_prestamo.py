from prestamo import Prestamo
from datetime import datetime

class ControladorPrestamo:

	def __init__(self):
		self.prestamos = []

	def crear_prestamo(self, id_juego):
		p = Prestamo(id_juego)
		self.prestamos.append(p)

	def finalizar_prestamo(self, prestamo):
		if (prestamo.activo):
			prestamo.activo = False
			prestamo.fecha_fin = datetime.now()
			return True

		else:
			return False