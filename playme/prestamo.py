from datetime import datetime
import itertools

class Prestamo:

	def __init__(self, juego):
		self.fecha_inicio = datetime.now()
		self.fecha_fin = None
		self.juego = juego
		self.activo = True

	def get_fecha_inicio(self):
		return self.fecha_inicio.strftime("%d-%m-%Y %H:%M")

	def get_fecha_fin(self):
		if (self.activo):
			return self.fecha_fin.strftime("%d-%m-%Y %H:%M")

		return None