import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app import app
from assertpy import assert_that
from datetime import datetime
import pytest
import json

client = TestClient(app)

def test_get_fecha_inicio():
	response = client.get("/prestamo/fecha_inicio/1")

	assert_that(response.status_code).is_equal_to(200)

def test_get_fecha_fin():
	response = client.get("/prestamo/fecha_fin",
		json={"fecha_fin": "2032-06-01T12:13:14", "juego": {"id": 1, "nombre": "Aventureros al Tren"}, "activo": False}
	)

	assert_that(response.status_code).is_equal_to(200)

def test_get_fecha_fin_fail():
	response = client.get("/prestamo/fecha_fin",
		json={"juego": {"id": 1, "nombre": "Aventureros al Tren"}, "activo": True}
	)

	res = json.loads(response.text)

	assert_that(response.status_code).is_equal_to(404)
	assert_that(res["detail"]).is_equal_to("El préstamo no ha finalizado aún")