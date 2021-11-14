import sys
import os
sys.path.append('playme/')

from prestamo import Prestamo
from juego import Juego
from controlador_prestamo import ControladorPrestamo
from datetime import datetime, timedelta
import pytest

def test_crear_prestamo():
	controlador = ControladorPrestamo()
	juego = Juego(1, "Aventureros al Tren")
	prestamo = Prestamo(juego)

	controlador.crear_prestamo(juego)

	assert len(controlador.prestamos) == 1
	assert prestamo.activo == True
	assert prestamo.fecha_fin == None
	assert type(prestamo.fecha_inicio) == datetime
	assert type(prestamo) == Prestamo

def test_finalizar_prestamo_activo():
	controlador = ControladorPrestamo()
	juego = Juego(1, "Aventureros al Tren")
	prestamo = Prestamo(juego)

	controlador.crear_prestamo(juego)
	res = controlador.finalizar_prestamo(prestamo)

	assert res == True
	assert prestamo.activo == False
	assert prestamo.fecha_fin != None
	assert type(prestamo.fecha_fin) == datetime

def test_finalizar_prestamo_inactivo():
	controlador = ControladorPrestamo()
	juego = Juego(1, "Aventureros al Tren")
	prestamo = Prestamo(juego)

	controlador.crear_prestamo(juego)
	controlador.finalizar_prestamo(prestamo)
	res = controlador.finalizar_prestamo(prestamo)

	assert res == False

def test_tiempo_restante_prestamo_activo():
	controlador = ControladorPrestamo()
	juego = Juego(1, "Aventureros al Tren")
	prestamo = Prestamo(juego)

	controlador.crear_prestamo(juego)
	formato = "%H:%M"

	res = controlador.tiempo_restante(prestamo)

	assert datetime.strptime(res, formato)

def test_tiempo_restante_prestamo_inactivo():
	controlador = ControladorPrestamo()
	juego = Juego(1, "Aventureros al Tren")
	prestamo = Prestamo(juego)

	controlador.crear_prestamo(juego)
	formato = "%H:%M"

	controlador.finalizar_prestamo(prestamo)
	res = controlador.tiempo_restante(prestamo)

	assert res == None

def test_devolver_prestamo():
	controlador = ControladorPrestamo()
	juego = Juego(1, "Aventureros al Tren")
	prestamo = Prestamo(juego)

	controlador.crear_prestamo(juego)
	res = controlador.devolver_prestamo_activo(juego)

	assert res.juego == juego

def test_tiempo_medio():
	controlador = ControladorPrestamo()
	juego = Juego(1, "Aventureros al Tren")

	prestamo = Prestamo(juego)
	controlador.crear_prestamo(juego)
	res_prestamo = controlador.devolver_prestamo_activo(juego)
	controlador.finalizar_prestamo(res_prestamo)
	res_prestamo.fecha_fin = datetime.now() + timedelta(minutes = 10)

	prestamo2 = Prestamo(juego)
	controlador.crear_prestamo(juego)
	res_prestamo2 = controlador.devolver_prestamo_activo(juego)
	controlador.finalizar_prestamo(res_prestamo2)
	res_prestamo2.fecha_fin = datetime.now() + timedelta(minutes = 20)

	res = controlador.tiempo_medio(juego)

	assert res == 15