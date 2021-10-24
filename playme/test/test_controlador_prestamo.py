import sys
import os
sys.path.append(os.path.abspath('../src/'))

from _prestamo import Prestamo
from _controlador_prestamo import ControladorPrestamo
from datetime import datetime
import pytest

def test_crear_prestamo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)

	assert len(controlador.prestamos) == 1
	assert prestamo.activo == True
	assert prestamo.fecha_fin == None
	assert type(prestamo.fecha_inicio) == datetime
	assert type(prestamo) == Prestamo

def test_finalizar_prestamo_activo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)
	res = controlador.finalizar_prestamo(prestamo)

	assert res == True
	assert prestamo.activo == False
	assert prestamo.fecha_fin != None
	assert type(prestamo.fecha_fin) == datetime

def test_finalizar_prestamo_inactivo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)
	controlador.finalizar_prestamo(prestamo)
	res = controlador.finalizar_prestamo(prestamo)

	assert res == False

def test_tiempo_restante_prestamo_activo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)
	formato = "%H:%M"

	res = controlador.tiempo_restante(prestamo)

	assert datetime.strptime(res, formato)

def test_tiempo_restante_prestamo_inactivo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)
	formato = "%H:%M"

	controlador.finalizar_prestamo(prestamo)
	res = controlador.tiempo_restante(prestamo)

	assert res == None