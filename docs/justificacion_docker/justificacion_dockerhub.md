# Subida del contenedor a Docker Hub con actualización automática

## Pasos para subir imagen a Docker Hub

Para subir el contenedor a Docker Hub se han seguido las [instrucciones](https://docs.docker.com/docker-hub/repos/) que aparecen en su página web:

1. Se crea un repositorio con el nombre en minúscula de la aplicación

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/repository.png" width="100%" height="100%">

2. Renombro la imagen local con el formato ```docker tag <existing-image> <hub-user>/<repo-name>[:<tag>]```

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/rename-container.png" width="100%" height="100%">

3. Hago login a mi cuenta de Docker Hub desde la terminal

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/docker-login.png" width="100%" height="100%">

4. Se hace push al repositorio creado siguiendo el formato del paso 2

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/docker-push.png" width="100%" height="100%">

5. Como resultado se puede ver que se ha subido la imagen [(ver aquí)](https://hub.docker.com/repository/docker/jumacasni/playme)

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/docker-hub.png" width="100%" height="100%">

## Pasos para permitir la actualización automática

Para la actualización automática se va a hacer uso de una [**Github Action**](https://github.com/marketplace/actions/build-and-push-docker-images) ya que la funcionalidad de *automated builds* de Docker Hub dejó de ser gratuita en [Junio de 2021](https://www.docker.com/blog/changes-to-docker-hub-autobuilds/).

Se ha seguido [este tutorial](https://github.com/marketplace/actions/build-and-push-docker-images#git-context):

1. Selecciono **Docker images** en el menú de *Actions* del repositorio

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/github-action-docker-image.png" width="50%" height="50%">

2. Se crea el archivo **docker-image.yaml** con los pasos correspondientes

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/docker-image-yaml.png" width="100%" height="100%">

3. Se crean las dos variables secretas necesarias para hacer el push desde la Github Action

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/secrets.png" width="100%" height="100%">
