import sys
import os
sys.path.append(os.path.abspath('../src/'))

from _prestamo import Prestamo
from _controlador_prestamo import ControladorPrestamo
from datetime import datetime
import unittest

class TestControladorPrestamo(unittest.TestCase):
	def test_crear_prestamo(self):
		controlador = ControladorPrestamo()
		prestamo = Prestamo(1)

		controlador.crear_prestamo(1)

		self.assertEqual(len(controlador.prestamos), 1)
		self.assertTrue(prestamo.activo)
		self.assertIsNone(prestamo.fecha_fin)
		self.assertIsInstance(prestamo.fecha_inicio, datetime)
		self.assertIsInstance(prestamo, Prestamo)

	def test_finalizar_prestamo_activo(self):
		controlador = ControladorPrestamo()
		prestamo = Prestamo(1)

		controlador.crear_prestamo(1)
		res = controlador.finalizar_prestamo(prestamo)

		self.assertTrue(res)
		self.assertFalse(prestamo.activo)
		self.assertIsNotNone(prestamo.fecha_fin)
		self.assertIsInstance(prestamo.fecha_fin, datetime)

	def test_finalizar_prestamo_inactivo(self):
		controlador = ControladorPrestamo()
		prestamo = Prestamo(1)

		controlador.crear_prestamo(1)
		controlador.finalizar_prestamo(prestamo)
		res = controlador.finalizar_prestamo(prestamo)

		self.assertFalse(res)

	def test_tiempo_restante_prestamo_activo(self):
		controlador = ControladorPrestamo()
		prestamo = Prestamo(1)
		formato = "%H:%M"

		res = controlador.tiempo_restante(prestamo)

		self.assertTrue(datetime.strptime(res, formato))

	def test_tiempo_restante_prestamo_inactivo(self):
		controlador = ControladorPrestamo()
		prestamo = Prestamo(1)
		formato = "%H:%M"

		controlador.finalizar_prestamo(prestamo)
		res = controlador.tiempo_restante(prestamo)

		self.assertIsNone(res)

if __name__ == '__main__':
    unittest.main()