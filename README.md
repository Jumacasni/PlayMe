# PlayMe

:warning: **Este proyecto a煤n est谩 en desarrollo** *(versi贸n 5.1)* :warning:

馃敡 [Configuraci贸n del entorno](docs/configuracion_git.md)

馃摑 [Descripci贸n del problema](docs/descripcion.md)

馃帀 [Soluci贸n propuesta y l贸gica de negocio](docs/propuesta.md)

:airplane: [Planificaci贸n de hitos y HUs](docs/planificacion.md)

## R煤bricas hito 5

- **R1: Justificaci贸n t茅cnica del framework elegido para el microservicio**:
	- [Elecci贸n del framework para el microservicio](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_microservicios/justificacion_framework.md)

- **R2: Dise帽o en general del API, las rutas (o tareas), tests y documentaci贸n de todo, justificando como se ajustan a las historias de usuario, de forma que reflejen correctamente un dise帽o por capas que desacopla la l贸gica de negocio del API**:
	- [Dise帽o general de la API](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_microservicios/disenio_api.md)
	- Rutas implementadas: [routers/controlador_prestamo.py](https://github.com/Jumacasni/PlayMe/blob/main/routers/controlador_prestamo.py)
	- Tests implementados: [tests/test_api_controlador_prestamo.py](https://github.com/Jumacasni/PlayMe/blob/main/tests/test_api_controlador_prestamo.py)

- **R3: uso de buenas pr谩cticas: configuraci贸n distribuida.**:
	- [Documentaci贸n de configuraci贸n distribuida](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_microservicios/configuracion_distribuida.md)

- **R4: uso de logs, incluyendo justificaci贸n del framework y herramienta elegida.**
	- [Elecci贸n y justifcaci贸n del framework usado](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_microservicios/justificacion_logs.md)
	- Uso de loguru en [routers/controlador_prestamo.py](https://github.com/Jumacasni/PlayMe/blob/main/routers/controlador_prestamo.py)
- **R5: tests correctos y de acuerdo con las historias de usuario.**:
	- Incluido en los tests implementados en **R2**

## Documentaci贸n adicional

- [Elecci贸n y justificaci贸n de la biblioteca de aserciones](docs/justificacion_herramientas_testing/justificacion_biblioteca_aserciones.md)
- [Elecci贸n y justificaci贸n del marco de prueba](docs/justificacion_herramientas_testing/justificacion_test_framework.md)
- [Elecci贸n y justificaci贸n del gestor de tareas](docs/justificacion_herramientas_testing/justificacion_gestores_tareas.md)
- [Creaci贸n de Dockerfile y elecci贸n del contenedor base](docs/justificacion_docker/justificacion_dockerfile.md)
- [Dockerfile](Dockerfile)
- [Subida del contenedor a Docker Hub con actualizaci贸n autom谩tica](docs/justificacion_docker/justificacion_dockerhub.md)
- [Subida del contenedor a Github Container Registry](docs/justificacion_docker/justificacion_gcr.md)
- [Justificaci贸n y documentaci贸n de uso de Travis](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_ci/sistemas_ci.md#travis)
- [Justificaci贸n y documentaci贸n de uso de Circle CI](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_ci/sistemas_ci.md#circle-ci)
- [Justificaci贸n y documentaci贸n de uso de Github Action](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_ci/sistemas_ci.md#github-action)

## Licencia 馃搫

Este proyecto est谩 bajo licencia [GNU Affero General Public License v3.0](LICENSE)
