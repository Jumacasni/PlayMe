# Elección de gestor de tareas y justificación

Los gestores de tareas que se van a discutir para este proyecto son:
- Poetry
- Invoke

---

## Poetry

**Ventajas :white_check_mark:**

- Uso del fichero ```pyproject.toml``` para guardar toda la información necesaria acerca del proyecto:

```python
[tool.poetry]
name = "poet"
version = "0.1.0"
description = ""
authors = ["lewoudar <XXX@XXX.com>"]

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
```

- Se pueden ver todas las dependencias en el archivo ```poetry.lock``` que se genera automáticamente
- Añadir una dependencia se hace de forma directa con ```poetry add requests``` (igual de rápido que eliminar una dependencia con la opción ```remove```)
- Se puede ver de forma rápida todas las dependencias del proyecto con ```poetry show --tree```
- Si se desconoce si se tiene la última versión de una dependencia, se puede usar ```poetry show --latest``` para ver todos los paquetes con su versión actual y la última versión de los mismos
- Se crea un entorno virtual automáticamente

**Ejemplo de uso :desktop_computer:**

Los ficheros necesarios para ejecutar ```Poetry``` en este proyecto se puede encontrar en el [commit #fc4e3f5](https://github.com/Jumacasni/PlayMe/commit/fc4e3f5846e05d118516d73635d760d58a2e367a)

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/poetry.png" width="100%" height="100%">

---

## Invoke

**Ventajas :white_check_mark:**


- Está basado en ```Python3``` y el fichero ```tasks.py``` queda de manera muy similar a un fichero de Python:
```python
from invoke import task

@task
def build(c):
    print("Building!")

@task
def build(c, clean=False):
    if clean:
        print("Cleaning!")
    print("Building!")
```

- Permite ejecutar varias tareas en un mismo comando:
```sh 
invoke clean build
```

**Ejemplo de uso :desktop_computer:**

Los ficheros necesarios para ejecutar ```Invoke``` en este proyecto se puede encontrar en el [commit #8a55e13](https://github.com/Jumacasni/PlayMe/commit/8a55e137e7e7b181a0a53df4c6002555b4376a9f)

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/invoke.png" width="100%" height="100%">

---
## Conclusión

**Poetry** simplifica mucho el trabajo con el archivo ```pyproject.toml``` haciendo que sea una herramienta muy potente gracias a todo lo que se puede controlar en dicho archivo. Permite manejar un entorno virtual haciendo que sólo existan las dependencias justas y necesarias.

Es por esto que este proyecto va a usar **Poetry** como gestor de tareas.

---

## Referencias

- [Poetry](https://medium.com/analytics-vidhya/poetry-finally-an-all-in-one-tool-to-manage-python-packages-3c4d2538e828)
- [Invoke](https://www.pyinvoke.org/)