from datetime import datetime
import itertools

class Prestamo:

	id_iter = itertools.count()

	def __init__(self, id_juego):
		self.id = next(self.id_iter)
		self.fecha_inicio = datetime.now()
		self.fecha_fin = None
		self.id_juego = id_juego
		self.activo = True