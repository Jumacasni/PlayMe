# Elección de gestor de tareas y justificación

Los gestores de tareas que se van a discutir para este proyecto son:
- Doit
- Invoke

---

## Doit

**Ventajas :white_check_mark:**

- Las dependencias se calculan dinámicamente

- Está basado en ```Python```, con lo cual la forma de código ya se conoce

- Visualización DAG que es muy interesante para visualizar la dependencia de tareas

Los ficheros necesarios para ejecutar ```Doit``` en este proyecto se puede encontrar en el [commit #f1ebf5f](https://github.com/Jumacasni/PlayMe/commit/f1ebf5f7376672b87e240f6a6e171608d0bdc6fb)

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/doit.png" width="100%" height="100%">

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

Ambos gestores están basados en ```Python```, pero finalmente se decide usar ```Invoke``` ya que el fichero queda mucho más limpio y ordenado y su Github tiene actualizaciones más frecuentes.

---

## Referencias

- [Poetry](https://pypyr.io/)
- [Invoke](https://www.pyinvoke.org/)