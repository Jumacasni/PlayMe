from prestamo import Prestamo
from datetime import datetime

class ControladorPrestamo:

	def __init__(self):
		self.prestamos = {}

	def crear_prestamo(self, juego):
		p = Prestamo(juego)

		if juego.id not in self.prestamos:
			self.prestamos[juego.id] = p
		else:
			self.prestamos[juego.id].append(p)

	def devolver_prestamo(self, juego):
		return self.prestamos[juego.id]

	def finalizar_prestamo(self, prestamo):
		if (prestamo.activo):
			prestamo.activo = False
			prestamo.fecha_fin = datetime.now()
			return True

		else:
			return False

	def tiempo_restante(self, prestamo):
		if (prestamo.activo):
			if (datetime.now() > prestamo.fecha_inicio):
				diferencia_hora = datetime.now() - prestamo.fecha_inicio

				# Devolver tiempo restante en formato %H:%M
				return (str(diferencia_hora).split(".")[0])[:-3]

			return None

		return None