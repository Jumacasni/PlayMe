# Diseño general de la API

Para el diseño de la API usando **FastAPI** se han tenido en cuenta las siguientes **buenas prácticas**:

- Se ha creado una carpeta [routers](https://github.com/Jumacasni/PlayMe/tree/main/routers) donde se almacenan los distintos archivos que contienen las rutas de cada clase y se adjuntan todas las rutas en el fichero principal [app.py](https://github.com/Jumacasni/PlayMe/tree/main/app.py)
- **FastAPI** hace uso de la librería [pydantic](https://pydantic-docs.helpmanual.io/) que permite crear modelos de clases para realizar una validación de datos de forma automática
- Se unifican lo máximo posible las rutas de forma que un mismo endpoint sirva tanto para un **get** como para un **post** (en este caso)

A los endpoints que requieren de un juego como argumento (o préstamo), este argumento se le pasa en el *request body* a través de la clase *JuegoModel* (ó la clase *PrestamoModel*) usando la librería **pydantic**:

```python
class JuegoModel(BaseModel):
	id: int
	nombre: str
```

```python
class PrestamoModel(BaseModel):
	fecha_inicio: Optional[datetime]
	fecha_fin: Optional[datetime]
	juego: JuegoModel
	activo: Optional[bool]
```

## Endpoints


### Controlador de préstamos
- [[HU1] Como usuario, necesito saber cuánto tiempo restante le queda a un préstamo](https://github.com/Jumacasni/PlayMe/issues/31):
	
	- [```"/prestamo"```]:
		- **POST** - Crea un préstamo de un juego pasando un juego como argumento. Siempre devuelve un **201**.
		- **GET** - Devuelve un préstamo (si está activo) de un juego pasando un juego como argumento. Si no existe el juego o no hay un préstamo asociado al juego, devuelve un **404**.

	- [```"/finalizar_prestamo"```]:
		- **POST** - Finaliza el préstamo de un juego pasando un juego como argumento. Si el juego no tiene ningún préstamo activo, devuelve un **404**; en caso contrario, devuelve un **201**.


	- [```"/tiempo_restante"```]:
		- **GET** - Devuelve el tiempo restante de un préstamo de un juego pasando un juego como argumento. Si no existe el juego o no hay un préstamo asociado al juego, devuelve un **404**.

- [[HU2] Como usuario, quiero conocer el tiempo medio estimado de un juego](https://github.com/Jumacasni/PlayMe/issues/38):

	- [```"/tiempo_medio"```]:
		- **GET** - Devuelve el tiempo medio de un juego pasando un juego como argumento. Si no existen préstamos asociados al juego, devuelve un **404**.

- [[[HU3] Como usuario, quiero saber cuáles son los juegos que más y menos usa la gente]](https://github.com/Jumacasni/PlayMe/issues/39):

	- [```"/mas_usados"```]:
		- **GET** - Devuelve un ranking de los juegos más usados. Siempre devuelve un **200**.

	- [```"/menos_usados"```]:
		- **GET** - Devuelve un ranking de los juegos menos usados. Siempre devuelve un **200**.

### Préstamos
- [[HU1] Como usuario, necesito saber cuánto tiempo restante le queda a un préstamo](https://github.com/Jumacasni/PlayMe/issues/31):

	- [```"/prestamo/fecha_inicio"```]:
		- **GET** - Devuelve la fecha de inicio de un préstamo de un juego pasando un juego como argumento. Siempre devuelve un **200**.

	- [```"/prestamo/fecha_fin"```]:
		- **GET** - Devuelve la fecha de finalización de un préstamo de un juego pasando un juego como argumento. Si el préstamo aún no ha finalizado o el juego no existe, devuelve un **404**.