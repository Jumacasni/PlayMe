# Github Container Registry

Para subir el contenedor a **Github Container Registry** se ha seguido el tutorial de [Working with the Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

1. He creado un *Personal Access Token* con los permisos adecuados

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/pat.png" width="100%" height="100%">

2. Guardo el *PAT* en una variable de entorno y la uso para hacer login en el *Container Registry*

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/login-gcr.png" width="100%" height="100%">

3. Renombro la imagen siguiendo el formato ```ghcr.io/OWNER/IMAGE_NAME:latest``` y ejecuto ```docker push```

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/gcr-push.png" width="100%" height="100%">

4. Cambio la visibilidad del paquete y lo conecto al repositorio de este proyecto

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/connect-gcr.png" width="100%" height="100%">

Se puede ver el paquete correctamente subido [aquí](https://github.com/Jumacasni/PlayMe/pkgs/container/playme).