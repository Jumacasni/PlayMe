# Diseño general de la API

Para el diseño de la API usando **FastAPI** se han tenido en cuenta las siguientes **buenas prácticas**:

- Se ha creado una carpeta [routers](https://github.com/Jumacasni/PlayMe/tree/main/routers) donde se almacenan los distintos archivos que contienen las rutas de cada clase y se adjuntan todas las rutas en el fichero principal [app.py](https://github.com/Jumacasni/PlayMe/tree/main/app.py) (por ahora sólo hay un fichero de routers, pero habrá más en el futuro)
- **FastAPI** hace uso de la librería [pydantic](https://pydantic-docs.helpmanual.io/) que permite crear modelos de clases para realizar una validación de datos de forma automática
- Se unifican lo máximo posible las rutas de forma que un mismo endpoint sirva tanto para un **get** como para un **post** (en este caso)

A los endpoints que requieren de un juego como argumento, este argumento se le pasa en el *request body* a través de la clase *JuegoModel* usando la librería **pydantic**:

```python
class JuegoModel(BaseModel):
	id: int
	nombre: str
```

## Endpoints


### Controlador de préstamos
- [[HU1] Como usuario, necesito saber cuánto tiempo restante le queda a un préstamo](https://github.com/Jumacasni/PlayMe/issues/31):
	
	- [```"/prestamo"```]:
		- **POST** - Crea un préstamo de un juego pasando un juego como argumento. Siempre devuelve un **201**.
	
	- [```"/prestamo/{id}"```]:
		- **GET** - Devuelve un préstamo (si está activo) de un juego pasando un juego como argumento. Si no existe el juego o no hay un préstamo asociado al juego, devuelve un **404**.

	- [```"/finalizar_prestamo"```]:
		- **POST** - Finaliza el préstamo de un juego pasando un juego como argumento. Si el juego no tiene ningún préstamo activo, devuelve un **404**; en caso contrario, devuelve un **201**.


	- [```"/tiempo_restante/{id}"```]:
		- **GET** - Devuelve el tiempo restante de un préstamo de un juego pasando el id de un juego. Si no existe el juego o no hay un préstamo asociado al juego, devuelve un **404**.

- [[HU2] Como usuario, quiero conocer el tiempo medio estimado de un juego](https://github.com/Jumacasni/PlayMe/issues/38):

	- [```"/tiempo_medio/{id}"```]:
		- **GET** - Devuelve el tiempo medio de un juego pasando un id de un juego como argumento. Si no existen préstamos asociados al juego, devuelve un **404**.

- [[[HU3] Como usuario, quiero saber cuáles son los juegos que más y menos usa la gente]](https://github.com/Jumacasni/PlayMe/issues/39):

	- [```"/mas_usados"```]:
		- **GET** - Devuelve un ranking de los juegos más usados. Siempre devuelve un **200**.

	- [```"/menos_usados"```]:
		- **GET** - Devuelve un ranking de los juegos menos usados. Siempre devuelve un **200**.
