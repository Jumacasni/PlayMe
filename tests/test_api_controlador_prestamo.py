import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app import app
from assertpy import assert_that
import pytest
import json

client = TestClient(app)

# [HU1] Como usuario, necesito saber cuánto tiempo restante le queda a un préstamo
def test_crear_prestamo():
	response = client.post("/prestamo",
		json={"id": 1, "nombre": "Aventureros al Tren"}
	)

	assert_that(response.status_code).is_equal_to(200)

def test_devolver_prestamo():
	response = client.get("/prestamo",
		json={"id": 1, "nombre": "Aventureros al Tren"}
	)

	assert_that(response.status_code).is_equal_to(200)

def test_finalizar_prestamo():
	response = client.post("/finalizar_prestamo",
		json={"id": 1, "nombre": "Aventureros al Tren"}
	)

	assert_that(response.status_code).is_equal_to(200)

def test_finalizar_prestamo_fail():
	response = client.post("/finalizar_prestamo",
		json={"id": 1, "nombre": "Aventureros al Tren"}
	)

	res = json.loads(response.text)

	assert_that(response.status_code).is_equal_to(404)
	assert_that(res["detail"]).is_equal_to("El préstamo no está activo")

def test_devolver_prestamo_fail():
	response = client.get("/prestamo",
		json={"id": 1, "nombre": "Aventureros al Tren"}
	)

	res = json.loads(response.text)

	assert_that(response.status_code).is_equal_to(404)
	assert_that(res["detail"]).is_equal_to("El préstamo no está activo")

def test_tiempo_restante():
	client.post("/prestamo",
		json={"id": 1, "nombre": "Aventureros al Tren"}
	)

	response = client.get("/tiempo_restante",
		json={"id": 1, "nombre": "Aventureros al Tren"}
	)

	assert_that(response.status_code).is_equal_to(200)

def test_tiempo_restante():
	client.post("/finalizar_prestamo",
		json={"id": 1, "nombre": "Aventureros al Tren"}
	)

	response = client.get("/tiempo_restante",
		json={"id": 1, "nombre": "Aventureros al Tren"}
	)

	res = json.loads(response.text)

	assert_that(response.status_code).is_equal_to(404)
	assert_that(res["detail"]).is_equal_to("El préstamo no está activo")

# [HU2] Como usuario, quiero conocer el tiempo medio estimado de un juego
def test_tiempo_medio():
	response = client.get("/tiempo_medio",
		json={"id": 1, "nombre": "Aventureros al Tren"}
	)

	assert_that(response.status_code).is_equal_to(200)

def test_tiempo_medio_fail():
	response = client.get("/tiempo_medio",
		json={"id": 2, "nombre": "Ensalada de puntos"}
	)

	res = json.loads(response.text)

	assert_that(response.status_code).is_equal_to(404)
	assert_that(res["detail"]).is_equal_to("No existe el juego")