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
	response = client.get("/prestamo/fecha_inicio",
		json={"juego": {"id": 1, "nombre": "Aventureros al Tren"}}
	)

	assert_that(response.status_code).is_equal_to(200)
