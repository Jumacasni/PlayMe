import sys
import os
sys.path.append('playme/src/')

from _prestamo import Prestamo
from _controlador_prestamo import ControladorPrestamo
from datetime import datetime
from grappa import should
import grappa

def test_crear_prestamo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)

	len(controlador.prestamos) | should.be.equal.to(1)
	prestamo.activo | should.be.true
	prestamo.fecha_fin | should.be.none
	prestamo.fecha_inicio | should.be.a(datetime)
	prestamo | should.be.a(Prestamo)

def test_finalizar_prestamo_activo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)
	res = controlador.finalizar_prestamo(prestamo)

	res | should.be.true
	prestamo.activo | should.be.false
	prestamo.fecha_fin | should.not_be.none
	prestamo.fecha_fin | should.be.a(datetime)

def test_finalizar_prestamo_inactivo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)

	controlador.crear_prestamo(1)
	controlador.finalizar_prestamo(prestamo)
	res = controlador.finalizar_prestamo(prestamo)

	res | should.be.false

def test_tiempo_restante_prestamo_activo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)
	formato = "%H:%M"

	res = controlador.tiempo_restante(prestamo)

	datetime.strptime(res, formato) | should.be.present

def test_tiempo_restante_prestamo_inactivo():
	controlador = ControladorPrestamo()
	prestamo = Prestamo(1)
	formato = "%H:%M"

	controlador.finalizar_prestamo(prestamo)
	res = controlador.tiempo_restante(prestamo)

	res | should.be.none