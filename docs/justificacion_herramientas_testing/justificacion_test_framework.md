# Elección de marco de prueba y justificación

Los marcos de prueba que pueden usarse en este proyecto y que se van a discutir son:
- Unittest
- Nose2
- Pytest

A continuación se van a discutir las ventajas y desventajas de cada uno para, al final de este documento, proporcionar una elección final.

---

## Unittest

**Ventajas :white_check_mark:**
- Incluido por defecto en las librerías de Python

```python
import unittest
```

- Permite marcar un test como "que se espera a fallar", es decir, un test que sabemos que va a fallar pero que no debería contarse como un fallo [(ver referencia)](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures)

```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass
```

- Incluye su propio test runner

```python
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
```

**Desventajas :x:**
- Es obligatorio escribir un test dentro de una clase test, no se puede testear una función que no esté en una clase test

```python
class TestMethods(unittest.TestCase):
```
- Se genera mucho código repetido (*boilerplate code*)

**Ejemplo de uso :desktop_computer:**

Un ejemplo de uso de ```Unittest``` para este proyecto se puede encontrar en el [commit #8e6de51](https://github.com/Jumacasni/PlayMe/commit/8e6de511fe7d111764fff3c6b52b76630c807522)

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/unittest.png" width="100%" height="100%">

---
## Nose2


- Es una extensión de ```Unittest```, con lo cual los tests realizados anteriormente no cambian con ```Nose2```
- Permite parametrizar métodos
```python
class Test(unittest.TestCase):

    @params((1, 2), (2, 3), (4, 5))
    def test_less_than(self, a, b):
        assert a < b
```
- Permite ejecutar tests en paralelo usando el plugin [mp](https://docs.nose2.io/en/latest/plugins/mp.html), usando para esto un fichero de configuración

```python
[unittest]
plugins = nose2.plugins.mp

[multiprocess]
processes = 2
```
**Desventajas :x:**
- No incluye la funcionalidad de saltar tests, que sí incluye ```Unittest```
- Sólo soporta versiones de Python actualmente soportadas por el equipo de Python, con lo cual si en un futuro la versión de Python del proyecto deja de tener soporte, los tests también dejarán de tenerlo [(ver referencia)](https://docs.nose2.io/en/latest/differences.html#python-versions)
- No permite lanzar los tests de un archivo cuyo nombre no sea ```test*.py```

**Ejemplo de uso :desktop_computer:**

Un ejemplo de uso de ```Nose2``` para este proyecto se puede encontrar en el [commit #e3d13cd](https://github.com/Jumacasni/PlayMe/commit/e3d13cde0e36eb38fc551333b0860263ba226ef6)

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/nose2.png" width="100%" height="100%">

---

## PyTest

**Ventajas :white_check_mark:**
- Los tests son más compactos y no se genera código repetido
- No es necesario incluir los tests en clases
```python
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
```
- Permite parametrizar los métodos test
```python
import pytest

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```
- Permite la ejecución de tests en paralelo usando el plugin [pytest-xdist](https://github.com/pytest-dev/pytest-xdist)
```sh
pytest -n NUMCPUS
```

**Desventajas :x:**
- No es compatible con otros frameworks

**Ejemplo de uso :desktop_computer:**

Un ejemplo de uso de ```PyTest``` para este proyecto se puede encontrar en el [commit #bcd5537](https://github.com/Jumacasni/PlayMe/commit/bcd5537ec3fc63a57134df3028ee7be43c412f10)

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/pytest.png" width="100%" height="100%">

---

## Conclusión

Teniendo en cuenta la necesidad de pequeños y concisos tests para este proyecto, queriendo minimizar la cantidad de código repetido (*boilerplate code*) y tras haber probado distintas librerías, se va a usar **PyTest** como librería para los tests.