import sys
import os
sys.path.append('playme/')

from juego import Juego
from prestamo import Prestamo
from datetime import datetime, timedelta
from assertpy import assert_that

def test_salida_fecha_inicio():
	juego = Juego(1, "Aventureros al Tren")
	prestamo = Prestamo(juego)
	formato = "%d-%m-%Y %H:%M"

	assert_that(datetime.strptime(prestamo.get_fecha_inicio(), formato)).is_true()

def test_salida_fecha_fin():
	juego = Juego(1, "Aventureros al Tren")
	prestamo = Prestamo(juego)
	prestamo.activo = False
	prestamo.fecha_fin = datetime.now()

	formato = "%d-%m-%Y %H:%M"

	assert_that(datetime.strptime(prestamo.get_fecha_fin(), formato)).is_true()

def test_tiempo_empleado():
	juego = Juego(1, "Aventureros al Tren")
	prestamo = Prestamo(juego)
	prestamo.fecha_fin = datetime.now() + timedelta(minutes = 10)

	res = prestamo.get_tiempo_empleado()

	assert res == 10