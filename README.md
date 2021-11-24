# PlayMe

:warning: **Este proyecto aún está en desarrollo** *(versión 4.2)* :warning:

🔧 [Configuración del entorno](docs/configuracion_git.md)

📝 [Descripción del problema](docs/descripcion.md)

🎉 [Solución propuesta y lógica de negocio](docs/propuesta.md)

:airplane: [Planificación de hitos y HUs](docs/planificacion.md)

## Rúbricas hito 4

- **R1: Integración continua funcionando y correcta justificación de la misma**:
	- [Justificación y documentación de uso de Travis](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_ci/sistemas_ci.md#travis)
	- [.travis.yml](.travis.yml)
- **R2: configuración de algún sistema de integración continua adicional**:
	- **Circle CI**:
		- [Justificación y documentación de uso de Circle CI](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_ci/sistemas_ci.md#circle-ci)
		- [.circleci/config.yml](https://github.com/Jumacasni/PlayMe/blob/main/.circleci/config.yml)
	- **Github Action**:
		- [Justificación y documentación de uso de Github Action](https://github.com/Jumacasni/PlayMe/blob/main/docs/justificacion_ci/sistemas_ci.md#github-action)
		- [.github/workflows/ci.yml](https://github.com/Jumacasni/PlayMe/blob/main/.github/workflows/ci.yml)

- **R3: uso correcto del gestor de tareas y otras buenas prácticas en todos los casos anteriores**:
	- Incluido en los archivos de **R1** y **R2**

- **R4: aprovechamiento del contenedor de Docker generado en el hito anterior en alguno de los sistemas de CI**:
	- Se ha aprovechado el contenedor Docker en **Circle CI** [(.circleci/config.yml)](https://github.com/Jumacasni/PlayMe/blob/main/.circleci/config.yml) y **Github Action** [(.github/workflows/ci.yml)](https://github.com/Jumacasni/PlayMe/blob/main/.github/workflows/ci.yml)

Además, se ha hecho un [avance de código](docs/avance_codigo/avance_hito4.md) del proyecto

## Correcciones realizadas del hito 3

- Se ha corregido el Dockerfile para ejecutar ```pip``` sin privilegios de superusuario y se justifica la adición de ```bash``` [aquí](https://github.com/Jumacasni/PlayMe/issues/66)

## Documentación adicional

- [Elección y justificación de la biblioteca de aserciones](docs/justificacion_herramientas_testing/justificacion_biblioteca_aserciones.md)
- [Elección y justificación del marco de prueba](docs/justificacion_herramientas_testing/justificacion_test_framework.md)
- [Elección y justificación del gestor de tareas](docs/justificacion_herramientas_testing/justificacion_gestores_tareas.md)
- [Creación de Dockerfile y elección del contenedor base](docs/justificacion_docker/justificacion_dockerfile.md)
- [Dockerfile](Dockerfile)
- [Subida del contenedor a Docker Hub con actualización automática](docs/justificacion_docker/justificacion_dockerhub.md)
- [Subida del contenedor a Github Container Registry](docs/justificacion_docker/justificacion_gcr.md)

## Licencia 📄

Este proyecto está bajo licencia [GNU Affero General Public License v3.0](LICENSE)
