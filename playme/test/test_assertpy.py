import sys
import os
sys.path.append('playme/src/')

from _prestamo import Prestamo
from _controlador_prestamo import ControladorPrestamo
from datetime import datetime
from assertpy import assert_that

def test_crear_prestamo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)

	assert_that(controlador.prestamos).is_length(1)
	assert_that(prestamo.activo).is_true()
	assert_that(prestamo.fecha_fin).is_none()
	assert_that(prestamo.fecha_inicio).is_type_of(datetime)
	assert_that(prestamo).is_type_of(Prestamo)

def test_finalizar_prestamo_activo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)
	res = controlador.finalizar_prestamo(prestamo)

	assert_that(res).is_true()
	assert_that(prestamo.activo).is_false()
	assert_that(prestamo.fecha_fin).is_not_none()
	assert_that(prestamo.fecha_fin).is_type_of(datetime)

def test_finalizar_prestamo_inactivo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)
	controlador.finalizar_prestamo(prestamo)
	res = controlador.finalizar_prestamo(prestamo)

	assert_that(res).is_false()

def test_tiempo_restante_prestamo_activo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)
	formato = "%H:%M"

	res = controlador.tiempo_restante(prestamo)

	assert_that(datetime.strptime(res, formato)).is_true()

def test_tiempo_restante_prestamo_inactivo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)
	formato = "%H:%M"

	controlador.finalizar_prestamo(prestamo)
	res = controlador.tiempo_restante(prestamo)

	assert_that(res).is_none()