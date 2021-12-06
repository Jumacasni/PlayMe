# PlayMe

:warning: **Este proyecto aún está en desarrollo** *(versión 5.1)* :warning:

🔧 [Configuración del entorno](docs/configuracion_git.md)

📝 [Descripción del problema](docs/descripcion.md)

🎉 [Solución propuesta y lógica de negocio](docs/propuesta.md)

:airplane: [Planificación de hitos y HUs](docs/planificacion.md)

## Rúbricas hito 4

- **R1: Justificación técnica del framework elegido para el microservicio**:
	- [Elección del framework para el microservicio](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_microservicios/justificacion_framework.md)

- **R2: Diseño en general del API, las rutas (o tareas), tests y documentación de todo, justificando como se ajustan a las historias de usuario, de forma que reflejen correctamente un diseño por capas que desacopla la lógica de negocio del API**:
	- [Diseño general de la API](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_microservicios/disenio_api.md)
	- Rutas implementadas: [routers/controlador_prestamo.py](https://github.com/Jumacasni/PlayMe/blob/main/routers/controlador_prestamo.py)
	- Tests implementados: [tests/test_api_controlador_prestamo.py](https://github.com/Jumacasni/PlayMe/blob/main/tests/test_api_controlador_prestamo.py)

- **R3: uso de buenas prácticas: configuración distribuida.**:
	- [Documentación de configuración distribuida](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_microservicios/configuracion_distribuida.md)

- **R4: uso de logs, incluyendo justificación del framework y herramienta elegida.**
	- [Elección y justifcación del framework usado](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_microservicios/justificacion_logs.md)
	- Uso de loguru en [routers/controlador_prestamo.py](https://github.com/Jumacasni/PlayMe/blob/main/routers/controlador_prestamo.py)
- **R5: tests correctos y de acuerdo con las historias de usuario.**:
	- Incluido en los tests implementados en **R2**

## Documentación adicional

- [Elección y justificación de la biblioteca de aserciones](docs/justificacion_herramientas_testing/justificacion_biblioteca_aserciones.md)
- [Elección y justificación del marco de prueba](docs/justificacion_herramientas_testing/justificacion_test_framework.md)
- [Elección y justificación del gestor de tareas](docs/justificacion_herramientas_testing/justificacion_gestores_tareas.md)
- [Creación de Dockerfile y elección del contenedor base](docs/justificacion_docker/justificacion_dockerfile.md)
- [Dockerfile](Dockerfile)
- [Subida del contenedor a Docker Hub con actualización automática](docs/justificacion_docker/justificacion_dockerhub.md)
- [Subida del contenedor a Github Container Registry](docs/justificacion_docker/justificacion_gcr.md)
- [Justificación y documentación de uso de Travis](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_ci/sistemas_ci.md#travis)
- [Justificación y documentación de uso de Circle CI](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_ci/sistemas_ci.md#circle-ci)
- [Justificación y documentación de uso de Github Action](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_ci/sistemas_ci.md#github-action)

## Licencia 📄

Este proyecto está bajo licencia [GNU Affero General Public License v3.0](LICENSE)
