# Creación de Dockerfile y elección del contenedor base

A continuación se van a discutir distintos contenedores base de los cuales uno será justificado como contenedor base para la aplicación.

Las imágenes que se van a usar para los contenedores van a ser las siguientes:

- [Ubuntu 18.04](https://hub.docker.com/_/ubuntu): una imagen de la distribución más popular de Linux, concretamente la versión 18.04 que es la que también uso actualmente en mi ordenador
- [Python 3.8 alpine](https://hub.docker.com/_/python): una imagen que trae lo justo y necesario para poder trabajar con Python 3.8, haciendo que se reduzca el peso de la imagen
- [Pypy 3.8 slime](https://hub.docker.com/_/pypy): Pypy es una implementación alternativa de Python, con lo que es interesante probar esta imagen y así comparar diferencias con la anterior

## Pasos para crear Dockerfile con buenas prácticas

Para hacer una buena justificación, se ha creado un Dockerfile por cada imagen base que ejecuta los tests de la aplicación. Para la creación del Dockerfile se han tenido en cuenta las siguientes [buenas prácticas](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/):

- Uso de imágenes oficiales como base
- Uso de la etiqueta ```LABEL``` para proporcionar ayuda e información en caso de que sea necesario
- Creación de un usuario sin privilegios para instalar lo necesario y testear la aplicación
- Unificar lo máximo posible las instrucciones ```RUN```, ya que cada instrucción de estas genera una capa que ocupa espacio
- Instalación de los paquetes de Python estrictamente necesarios, usando para ello el archivo ```requirements.txt``` de Python

## Comparación

### Ubuntu 18.04

En esta imagen es necesario instalar ```Python 3.8```, siguiendo para ello esta [guía de instalación](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/)

```
FROM ubuntu:18.04

LABEL maintainer ="Juan Manuel Castillo Nievas <jumacasni@correo.ugr.es>"

RUN apt-get update \
	&& apt-get -y install software-properties-common \
	&& add-apt-repository ppa:deadsnakes/ppa \
	&& apt-get -y install python3.8 python3-pip \
	&& useradd -ms /bin/bash playme \
	&& mkdir -p /app/test \
	&& chown playme /app/test \
	&& pip3 install invoke pytest assertpy

WORKDIR /app/test

USER playme

CMD ["invoke", "test"]
```

El contenedor ocupa **520MB**.

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/docker-ubuntu.png" width="100%" height="100%">

### Python 3.8 alpine

Para la construcción de este contenedor se debe instalar [bash](https://stackoverflow.com/questions/40944479/docker-how-to-use-bash-with-an-alpine-based-docker-image), ya que ```alpine``` no lo instala por defecto, y se añade un usuario usando ```adduser``` en lugar de ```useradd``` [(ver aquí)](https://stackoverflow.com/questions/49955097/how-do-i-add-a-user-when-im-using-alpine-as-a-base-image).

```
FROM python:3.8-alpine

LABEL maintainer ="Juan Manuel Castillo Nievas <jumacasni@correo.ugr.es>"

RUN apk update \
	&& apk add bash \
	&& adduser -D -h /home/playme -s /bin/bash playme \
	&& mkdir -p /app/test \
	&& chown playme /app/test \
	&& pip3 install invoke pytest assertpy

WORKDIR /app/test

USER playme

CMD ["invoke", "test"]
```

El contenedor ocupa **59.9MB**, que son más de 400MB de diferencia con respecto al contenedor anterior.

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/docker-python-alpine.png" width="100%" height="100%">

### Pypy 3.8 slim

Este Dockerfile es el que menos capas tiene debido a que es el que menos instrucciones ```RUN```posee.

```
FROM pypy:3.8-slim

LABEL maintainer ="Juan Manuel Castillo Nievas <jumacasni@correo.ugr.es>"

RUN useradd -ms /bin/bash playme \
	&& mkdir -p /app/test \
	&& chown playme /app/test \
	&& pip3 install invoke pytest assertpy

WORKDIR /app/test

USER playme

CMD ["invoke", "test"]
```

Este contenedor pesa **244MB**.

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/docker-pypy-slim.png" width="100%" height="100%">

## Ejecución del contenedor

Finalmente se testea el contenedor para comprobar que los tests se ejecutan correctamente

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/docker-run.png" width="100%" height="100%">

## Conclusiones

- Se descarta ```Ubuntu 18.04``` como imagen base ya que posee un tamaño bastante grande, siendo el contenedor que más ocupa de todos
- A pesar de que ```Pypy 3.8 slime``` es una alternativa bastante buena para Python, el contenedor final sigue ocupando mucho más que la versión ```alpine``` de Python.
- La imagen base que se va a utilizar va a ser ```Python 3.8 alpine```, ya que solamente instala lo justo y necesario para poder usar el propio lenguaje, y todo ello junto a los paquetes que necesita esta aplicación hace que el contenedor final sea muy ligero, con apenas 60MB de peso. 