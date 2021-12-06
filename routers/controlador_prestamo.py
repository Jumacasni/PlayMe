import sys
import os
sys.path.append('playme/')

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from juego import Juego
from prestamo import Prestamo
from controlador_prestamo import ControladorPrestamo
from loguru import logger

controlador = ControladorPrestamo()

router = APIRouter()

class JuegoModel(BaseModel):
	id: int
	nombre: str

# [HU1] Como usuario, necesito saber cuánto tiempo restante le queda a un préstamo
@router.post("/prestamo", status_code=201)
def crear_prestamo(juego: JuegoModel):
	juego = Juego(juego.id, juego.nombre)
	controlador.crear_prestamo(juego)

	logger.info("Préstamo creado con éxito")

@router.get("/prestamo/{id}")
def devolver_prestamo(id: int):
	juego = Juego(id)
	res = controlador.devolver_prestamo_activo(juego)

	if res is None:
		logger.error("Error al devolver un préstamo activo")
		raise HTTPException(status_code=404, detail="El préstamo no está activo")

	logger.info("Préstamo activo devuelto con éxito")
	return res

@router.post("/finalizar_prestamo", status_code=201)
def finalizar_prestamo(juego: JuegoModel):
	juego = Juego(juego.id, juego.nombre)
	prestamo = controlador.devolver_prestamo_activo(juego)

	res = controlador.finalizar_prestamo(prestamo)

	if res is False:
		logger.error("Error al finalizar un préstamo, no hay ninguno activo")
		raise HTTPException(status_code=404, detail="El préstamo no está activo")

	logger.info("Préstamo finalizado con éxito")
	return res

@router.get("/tiempo_restante/{id}")
def tiempo_restante(id: int):
	juego = Juego(id)
	prestamo = controlador.devolver_prestamo_activo(juego)

	res = controlador.tiempo_restante(prestamo)

	if res is None:
		logger.error("Error en el tiempo restante de un préstamo")
		raise HTTPException(status_code=404, detail="El préstamo no está activo")

	logger.info("Petición de tiempo restante de un préstamo con éxito")
	return res

# [HU2] Como usuario, quiero conocer el tiempo medio estimado de un juego
@router.get("/tiempo_medio/{id}")
def tiempo_medio(id: int):
	juego = Juego(id)

	res = controlador.tiempo_medio(juego)

	if res is None:
		logger.error("Error en el tiempo medio de un juego - No existe el juego")
		raise HTTPException(status_code=404, detail="No existe el juego")

	logger.info("Petición de tiempo medio de un juego con éxito")
	return res

# [HU3] Como usuario, quiero saber cuáles son los juegos que más y menos usa la gente
@router.get("/mas_usados")
def juegos_mas_usados():
	res = controlador.contar_juegos_usados(True)

	logger.info("Petición de juegos más usados con éxito")

	return res

@router.get("/menos_usados")
def juegos_menos_usados():
	res = controlador.contar_juegos_usados(False)

	logger.info("Petición de juegos menos usados con éxito")

	return res