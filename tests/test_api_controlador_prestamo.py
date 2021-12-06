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
