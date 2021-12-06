from fastapi import FastAPI
from routers import controlador_prestamo

app = FastAPI()
app.include_router(controlador_prestamo.router)
