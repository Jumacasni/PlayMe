import uvicorn
from fastapi import FastAPI
from routers import controlador_prestamo
import etcd3

app = FastAPI()

app.include_router(controlador_prestamo.router)
