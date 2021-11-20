# Sistemas de integración continua

# Travis

Para integrar este sistema en este proyecto se ha seguido el [tutorial](https://docs.travis-ci.com/user/tutorial/) disponible en su página web:

1. Iniciar sesión con Github

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/travis01.png" width="100%" height="100%">

2. Permitir el acceso al repositorio del proyecto

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/travis02.png" width="100%" height="100%">
<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/travis03.png" width="100%" height="100%">

3. Añadir el archivo [travis.yml](travis.yml) al repositorio

Un fichero muy básico de travis es el siguiente:

```
language: python
python:
  - "3.6"
  - "3.8"
  - "3.10"

dist: focal

arch:
	- aarch64

before_install:
  - pip3 install invoke pytest assertpy

script:
  - invoke test
```

- En ```language``` se especifica el lenguaje de programación y justo debajo se especifican las versiones que se quieren testear
- En ```before_install``` se especifican las acciones que se desean realizar antes de ```install``` (el gestor de tareas, por ejemplo)
- En ```sript``` se invoca al gestor de tareas para que lance los tests

**Notas adicionales**

La versión **3.10.0** sólo está disponible en **aarch64** de la distribución **20.04** (ver [aquí](https://docs.travis-ci.com/user/languages/python/#python-versions)), con lo cual se debe añadir a Travis la siguiente configuración:
- ```dist```: focal (20.04)
- ```arch```: aarch64


4. En Travis se puede ver que pasan todos los *checks*

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/travis04.png" width="100%" height="100%">
