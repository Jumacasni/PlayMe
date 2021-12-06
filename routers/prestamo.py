import sys
import os
sys.path.append('playme/')

from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from juego import Juego
from prestamo import Prestamo
from controlador_prestamo import ControladorPrestamo
from datetime import datetime

router = APIRouter(prefix="/prestamo")

class PrestamoModel(BaseModel):
	fecha_inicio: Optional[datetime]
	fecha_fin: Optional[datetime]
	juego: int
	activo: Optional[bool]

@router.get("/fecha_inicio/{id}")
def crear_prestamo(id: int):
	prestamo = Prestamo(Juego(id))
	
	return prestamo.get_fecha_inicio()

@router.get("/fecha_fin")
def crear_prestamo(prestamo: PrestamoModel):
	pr = Prestamo(Juego(prestamo.juego.id, prestamo.juego.nombre))
	pr.fecha_fin = prestamo.fecha_fin
	pr.activo = prestamo.activo

	res = pr.get_fecha_fin()

	if res is None:
		raise HTTPException(status_code=404, detail="El préstamo no ha finalizado aún")

	return res