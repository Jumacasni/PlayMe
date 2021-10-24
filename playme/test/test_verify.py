import sys
import os
sys.path.append('playme/src/')

from _prestamo import Prestamo
from _controlador_prestamo import ControladorPrestamo
from datetime import datetime
from verify import expect

def test_crear_prestamo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)

	expect(controlador.prestamos).to_have_length()
	expect(prestamo.activo).to_be_truthy()
	expect(prestamo.fecha_fin).to_be_none()
	expect(prestamo.fecha_inicio).to_be_type(datetime)
	expect(prestamo).to_be_type(Prestamo)

def test_finalizar_prestamo_activo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)
	res = controlador.finalizar_prestamo(prestamo)

	expect(res).to_be_truthy()
	expect(prestamo.activo).to_be_falsy()
	expect(prestamo.fecha_fin).to_not_be_none()
	expect(prestamo.fecha_fin).to_be_type(datetime)

def test_finalizar_prestamo_inactivo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)
	controlador.finalizar_prestamo(prestamo)
	res = controlador.finalizar_prestamo(prestamo)

	expect(res).to_be_falsy()

def test_tiempo_restante_prestamo_activo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)
	formato = "%H:%M"

	res = controlador.tiempo_restante(prestamo)

	expect(datetime.strptime(res, formato)).to_be_truthy()

def test_tiempo_restante_prestamo_inactivo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)
	formato = "%H:%M"

	controlador.finalizar_prestamo(prestamo)
	res = controlador.tiempo_restante(prestamo)

	expect(res).to_be_none()