import uvicorn
from fastapi import FastAPI
from routers import controlador_prestamo, prestamo
import etcd3

app = FastAPI()
app.include_router(controlador_prestamo.router)
app.include_router(prestamo.router)

if __name__ == "__main__":
	client = etcd3.client()

	puerto = client.get('puerto')[0]
	host = client.get('host')[0]
	