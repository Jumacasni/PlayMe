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
