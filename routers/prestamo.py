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

class JuegoModel(BaseModel):
	id: int
	nombre: str

class PrestamoModel(BaseModel):
	fecha_inicio: Optional[datetime]
	fecha_fin: Optional[datetime]
	juego: JuegoModel
	activo: Optional[bool]

@router.get("/fecha_inicio")
def crear_prestamo(prestamo: PrestamoModel):
	prestamo = Prestamo(Juego(prestamo.juego.id, prestamo.juego.nombre))
	
	return prestamo.get_fecha_inicio()
