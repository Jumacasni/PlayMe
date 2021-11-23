# Sistemas de integración continua

La fase de intregación continua es **esencial** para el futuro despliegue de la aplicación.

En este documento se presenta la documentación de los 3 sistemas de integración continua que se han probado para un despliegue continuo:

- **Travis**: cuenta con la función de especificar distintas versiones del lenguaje para probar que el proyecto funciona correctamente en ellas.
- **Circle CI**: con este sistema se puede hacer uso del contenedor Docker generado en el hito anterior y que está subido en **Docker Hub** y así lanzar los tests automáticamente.
- **Github Action**: con las Github Action que proporciona Github también se puede aprovechar el contenedor Docker para lanzarlo y así lanzar los tests automáticamente. Además, es una buena combinación ya que también se hizo una Github Action en el hito anterior para subir automáticamente el contenedor a **Docker Hub** en cada ```push```.

## Travis

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

## Circle CI

Para usar este sistema de integración continua se han seguido los [pasos](https://circleci.com/docs/2.0/first-steps/) y [configuración](https://circleci.com/docs/2.0/configuration-reference/) de su página web:

1. Iniciar sesión usando la cuenta de Github

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/circleci01.png" width="100%" height="100%">

2. Se selecciona el repositorio de este proyecto

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/circleci02.png" width="100%" height="100%">

3. Se crea el archivo [.circleci/config.yml](https://github.com/Jumacasni/PlayMe/blob/main/.circleci/config.yml) con ayuda de la interfaz web para asegurar que la sintaxis es correcta (el contenido se explica más adelante)

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/circleci03.png" width="100%" height="100%">

4. Se sube el archivo a la rama ```main``` del repositorio y se selecciona en la interfaz web de Circle CI

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/circleci04.png" width="100%" height="100%">

5. Se ejecutan los tests y pasan con éxito

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/circleci05.png" width="100%" height="100%">

### Config.yml

El fichero [.circleci/config.yml](https://github.com/Jumacasni/PlayMe/blob/main/.circleci/config.yml) cuenta con la siguiente configuración:

```
version: 2.1

jobs:
  test:
    docker:
      - image: jumacasni/playme:latest
    steps:
      - checkout
      - run: invoke test

workflows:
  test_playme:
    jobs:
      - test
```

Lo que se pretende con este sistema de integración continua es lanzar nuestro contenedor de tests que se hizo en el hito anterior. Para lanzar imágenes Docker con Circle CI se ha seguido la [documentación](https://circleci.com/docs/2.0/building-docker-images/) disponible en su página web.

- El campo ```job``` especifica lo que queremos hacer, que en nuestro caso es lanzar nuestro contenedor que ejecuta los tests
- En el campo ```docker``` se especifica el contenedor que se debe ejecutar
- En el campo ```steps``` se especifican las acciones que se deben ejecutar, que debe incluir el lanzamiento de tests usando el **gestor de tareas**

## Github Action

Resulta interesante realizar una Github Action para la integración continua ya que esta también permite utilizar el contenedor docker. De esta forma, se ha creado el archivo [ci.yml](https://github.com/Jumacasni/PlayMe/blob/main/.github/workflows/ci.yml) previamente seleccionando la plantilla **Docker image** en las acciones del repositorio:

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/githubactionci01.png" width="100%" height="100%">

El archivo archivo [ci.yml](https://github.com/Jumacasni/PlayMe/blob/main/.github/workflows/ci.yml) tiene la siguiente configuración:

```
name: Docker Image CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:

  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Build the Docker image
      run: docker build -t playme .
    - name: Test
      run: docker run -t -v `pwd`:/app/test playme
```

Lo que se hace es ```docker build``` para construir la imagen para posteriormente usar ```docker run``` montando el volumen correspondiente. De esta manera, al hacer **push** sobre el repositorio, se ejecuta esta Github Action obteniendo el éxito de los tests

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/githubactionci02.png" width="100%" height="100%">

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/githubactionci03.png" width="100%" height="100%">
