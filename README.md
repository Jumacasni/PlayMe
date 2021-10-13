# PlayMe

:warning: **Este proyecto aún está en desarrollo** *(versión 1.1)* :warning:

🔧 [Configuración del entorno](docs/configuracion_git.md)

📝 [Descripción del problema](docs/descripcion.md)

🎉 [Solución propuesta y lógica de negocio](docs/propuesta.md)

## Hitos e historias de usuario 👥

Se han definido los siguientes 5 hitos (5 productos mínimamente viables):

- [1. Administración del catálogo de juegos de mesa](https://github.com/Jumacasni/PlayMe/milestone/2): contiene historias de usuario que crean un producto mínimamente viable cuya funcionalidad que los trabajadores puedan **ofrecer un catálogo de juegos de mesa** de un local:
	- [[HU1] Registrar cuenta de un trabajador](https://github.com/Jumacasni/PlayMe/issues/3)
	- [[HU3] Añadir un juego de mesa](https://github.com/Jumacasni/PlayMe/issues/5)
	- [[HU4] Eliminar un juego de mesa ](https://github.com/Jumacasni/PlayMe/issues/6)
	- [[HU5] Modificar un juego de mesa ](https://github.com/Jumacasni/PlayMe/issues/7)
	- [[HU6] Dejar de mostrar un juego de mesa en el catálogo de los clientes](https://github.com/Jumacasni/PlayMe/issues/8)
	- [[HU7] Mostrar un juego de mesa en el catálogo de los clientes](https://github.com/Jumacasni/PlayMe/issues/9)

- [2. Gestión de préstamos de juegos de mesa](https://github.com/Jumacasni/PlayMe/milestone/3): contiene historias de usuario que crean un producto mínimamente viable cuya funcionalidad es registrar los préstamos de juegos de mesa asociados a un cliente y sacar beneficio de ello sabiendo **cuánto tiempo de juego le queda a los clientes**:
	- [[HU2] Registrar cuenta de un cliente](https://github.com/Jumacasni/PlayMe/issues/4)
	- [[HU8] Registrar préstamo de juego a un cliente](https://github.com/Jumacasni/PlayMe/issues/10)
	- [[HU9] Aumentar tiempo de préstamo de un juego](https://github.com/Jumacasni/PlayMe/issues/11)
	- [[HU10] Finalizar préstamo de juego a un cliente](https://github.com/Jumacasni/PlayMe/issues/12)
	- [[HU11] Ver cuánto tiempo le queda a un juego prestado para volver a estar disponible](https://github.com/Jumacasni/PlayMe/issues/13)

- [3. Reseñas de juegos de mesa](https://github.com/Jumacasni/PlayMe/milestone/4): contiene historias de usuario que crean un producto mínimamente viable cuya funcionalidad es **recomendar juegos de mesa** a los usuarios en base a sus reseñas:
	- [[HU12] Añadir reseña de un juego de mesa](https://github.com/Jumacasni/PlayMe/issues/14)
	- [[HU13] Editar reseña de un juego de mesa](https://github.com/Jumacasni/PlayMe/issues/15)
	- [[HU14] Eliminar reseña de un juego de mesa](https://github.com/Jumacasni/PlayMe/issues/16)
	- [[HU15] Recibir recomendaciones de juegos de mesa](https://github.com/Jumacasni/PlayMe/issues/17)

- [4. Navegar en el catálogo de juegos de mesa](https://github.com/Jumacasni/PlayMe/milestone/5): contiene historias de usuario que crean un producto mínimamente viable cuya funcionalidad es ofrecer una navegación del catálogo a todos los usuarios pudiendo **aplicar distintos filtros** en base a sus necesidades:
	- [[HU16] Consultar el catálogo de juegos para clientes](https://github.com/Jumacasni/PlayMe/issues/18)
	- [[HU17] Consultar el catálogo de juegos para trabajadores](https://github.com/Jumacasni/PlayMe/issues/19)
	- [[HU18] Consultar información sobre un juego](https://github.com/Jumacasni/PlayMe/issues/20)
	- [[HU19] Filtrar catálogo de juegos por tiempo estimado de juego](https://github.com/Jumacasni/PlayMe/issues/21)
	- [[HU20] Filtrar catálogo de juegos por juegos que están disponibles ahora mismo](https://github.com/Jumacasni/PlayMe/issues/22)
	- [[HU21] Filtrar catálogo de juegos por número de jugadores](https://github.com/Jumacasni/PlayMe/issues/23)

- [5. Estadísticas de juegos de mesa](https://github.com/Jumacasni/PlayMe/milestone/6): contiene historias de usuario que crean un producto mínimamente viable cuya funcionalidad es ofrecer estadísticas a los trabajadores para que puedan saber c**uáles son los juegos que más y menos gustan**, y de esa forma hacer cambios en el catálogo del local:
	- [[HU22] Analizar estadísticas del uso de juegos de mesa por los clientes](https://github.com/Jumacasni/PlayMe/issues/24)

## Avances en las historias de usuario ✏️

En el fichero [cc.yaml](cc.yaml) se encuentran las entidades creadas para el avance de las primeras historias de usuario:
- Clase [**Usuario**](playme/src/usuario.py): se define la clase Usuario, que representa un usuario de un local, ya sea un trabajador o un cliente. Avanza [[HU1] Registrar cuenta de un trabajador](https://github.com/Jumacasni/PlayMe/issues/3).
- Clase [**Trabajador**](playme/src/trabajador.py): se define la clase Trabajador, que es un trabajador de un local. Avanza [[HU1] Registrar cuenta de un trabajador](https://github.com/Jumacasni/PlayMe/issues/3).
- Clase [**Cliente**](playme/src/cliente.py): se define la clase Cliente, que es un cliente de un local. Avanza [[HU2] Registrar cuenta de un cliente](https://github.com/Jumacasni/PlayMe/issues/4).
- Clase [**Juego**](playme/src/juego.py): se define la clase Juego, que representa un juego de mesa. Avanza [[HU3] Añadir un juego de mesa](https://github.com/Jumacasni/PlayMe/issues/5).
- Clase [**Catalogo**](playme/src/catalogo.py): se define la clase Catalogo, que representa el catálogo y que está formado por juegos de mesa. Avanza [[HU3] Añadir un juego de mesa](https://github.com/Jumacasni/PlayMe/issues/5).


## Licencia 📄

Este proyecto está bajo licencia [GNU Affero General Public License v3.0](LICENSE)
