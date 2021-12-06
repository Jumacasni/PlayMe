from fastapi import FastAPI
from routers import controlador_prestamo, prestamo

app = FastAPI()
app.include_router(controlador_prestamo.router)
app.include_router(prestamo.router)
