from datetime import date

class Prestamo:
	def __init__(self, id_juego):
		self.fecha_inicio = date.today()
		self.fecha_fin = None
		self.id_juego = id_juego
		self.estado = True