# Elección de framework para microservicio

Un requisito fundamental para la elección del framework es que este proporcione una funcionalidad de testing para **levantar el cliente con el test**, es decir, **sin necesidad de un servidor**. Es por ello que se van a discutir los siguientes frameworks:

- [FastAPI](https://fastapi.tiangolo.com/)
- [Sanic](https://sanic.readthedocs.io/en/stable/)
- [Starlette](https://github.com/encode/starlette)

## FastAPI

Su [repositorio](https://github.com/tiangolo/fastapi) cuenta con más de 39k estrellas y cuenta con casi 300 contribuidores, con lo cual es un framework que está al día y tiene un mantenimiento muy frecuente. 

Es uno de los frameworks **más rápidos**, tal y como se puede ver en [este estudio de performance](https://github.com/tiangolo/fastapi#performance).

Permite la creación de una API tanto **síncrona** como **asíncrona** simplemente añadiendo ```async``` en la definición del método:

```python
# Síncrono
@app.get("/")
def read_root():
    return {"Hello": "World"}
```

```python
# Asíncrono
@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

Incluye el módulo ```TestClient``` a través del cual permite testear la API sin necesidad de levantar un servidor:

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
	response = client.get("/")
```

## Sanic

Su [repositorio](https://github.com/sanic-org/sanic) cuenta con más de 15k estrellas y casi 300 contribuidores al igual que **FastAPI**, con la diferencia de que este framework es más viejo.

Cuenta también con el uso de ```async/await``` y su sintaxis es bastante parecida a la de **FastAPI**, además de contar con un módulo para devolver la respuesta en formato **JSON**:

```python
from sanic import Sanic
from sanic.response import json

app = Sanic("My Hello, world app")

@app.route('/')
async def test(request):
    return json({'hello': 'world'})
```

Para importar un cliente para testear la API se encuentra [sanic-testing](https://github.com/sanic-org/sanic-testing), ya que el módulo ```testing``` que viene por defecto en Sanic se va a eliminar en un futuro. Hay que tener en cuenta que este módulo es muy reciente y todavía cuenta con **TODO**, con lo cual puede que sea pronto para poder usarlo.

## Starlette

Su [repositorio](https://github.com/encode/starlette) cuenta con más de 6k de estrellas y casi 200 contribuidores. Es el que menos tiene con respecto a los dos frameworks anteriores.

Uno de los puntos fuertes de este framework es que tiene una buena performance en servicios **asíncronos**.

Incluye el módulo [TestClient](https://www.starlette.io/testclient/) para poder testear fácilmente sin necesidad de levantar un servidor:

```python
from starlette.testclient import TestClient

def test_app():
    client = TestClient(app)
```

## Conclusiones y elección final

- Se descarta el uso de **Sanic** ya que el módulo **testing** que incluye va a desaparecer en un futuro y la librería ```sanic-testing``` es demasiado nueva, con lo cual puede que aún sea inestable
- Aunque **FastAPI** y **Starlette** sean ambos muy recientes, sí que es cierto que **FastAPI** cuenta con más contribuidores y tiene mucha más colaboración en Github (fijándonos en la cantidad de estrellas y contribuidores en sus repositorios)

Teniendo en cuenta estos apuntes, finalmente se decide optar por el uso de **FastAPI**.
