import sys
import os
sys.path.append('playme/')

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from juego import Juego
from prestamo import Prestamo
from controlador_prestamo import ControladorPrestamo

router = APIRouter()

controlador = ControladorPrestamo()

class JuegoModel(BaseModel):
	id: int
	nombre: str

# [HU1] Como usuario, necesito saber cuánto tiempo restante le queda a un préstamo
@router.post("/prestamo")
def crear_prestamo(juego: JuegoModel):
	juego = Juego(juego.id, juego.nombre)
	controlador.crear_prestamo(juego)

@router.get("/prestamo")
def devolver_prestamo(juego: JuegoModel):
	juego = Juego(juego.id, juego.nombre)
	res = controlador.devolver_prestamo_activo(juego)

	if res is None:
		raise HTTPException(status_code=404, detail="El préstamo no está activo")

	return res

@router.post("/finalizar_prestamo")
def finalizar_prestamo(juego: JuegoModel):
	juego = Juego(juego.id, juego.nombre)
	prestamo = controlador.devolver_prestamo_activo(juego)

	res = controlador.finalizar_prestamo(prestamo)

	if res is False:
		raise HTTPException(status_code=404, detail="El préstamo no está activo")

	return res

@router.get("/tiempo_restante")
def tiempo_restante(juego: JuegoModel):
	juego = Juego(juego.id, juego.nombre)
	prestamo = controlador.devolver_prestamo_activo(juego)

	res = controlador.tiempo_restante(prestamo)

	if res is None:
		raise HTTPException(status_code=404, detail="El préstamo no está activo")

	return res

# [HU2] Como usuario, quiero conocer el tiempo medio estimado de un juego
@router.get("/tiempo_medio")
def tiempo_medio(juego: JuegoModel):
	juego = Juego(juego.id, juego.nombre)

	res = controlador.tiempo_medio(juego)

	if res is None:
		raise HTTPException(status_code=404, detail="No existe el juego")

	return res

# [HU3] Como usuario, quiero saber cuáles son los juegos que más y menos usa la gente
@router.get("/mas_usados")
def juegos_mas_usados():
	res = controlador.contar_juegos_usados(True)

	return res

@router.get("/menos_usados")
def juegos_menos_usados():
	res = controlador.contar_juegos_usados(False)

	return res