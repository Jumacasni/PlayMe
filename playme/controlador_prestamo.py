from prestamo import Prestamo
from datetime import datetime

class ControladorPrestamo:

	def __init__(self):
		self.prestamos = {}

	def crear_prestamo(self, juego):
		p = Prestamo(juego)

		if juego.id not in self.prestamos:
			self.prestamos[juego.id] = [p]
		else:
			self.prestamos[juego.id].append(p)

	def devolver_prestamo_activo(self, juego):
		prestamo = self.prestamos[juego.id][-1]

		if prestamo.activo:
			return prestamo
		else:
			return None

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

	def tiempo_medio(self, juego):
		prestamos = self.prestamos[juego.id]

		# Elimina el último préstamo si está activo
		if prestamos[-1].activo:
			prestamos = prestamos[:-1]

		tiempo_total = 0

		for prestamo in prestamos:
			print(prestamo.get_tiempo_empleado())
			tiempo_total += prestamo.get_tiempo_empleado()

		return round(tiempo_total / len(prestamos), 0)