# Elección y justificación del logging usado

Se contemplan dos opciones para el logging:

- **logging**: esta librería ya viene por defecto en Python, con lo cual no es necesario instalar nada adicional.
- **loguru**: se posiciona como la librería de logging más simple en Python

En este [artículo](https://alimbekov.com/en/python-logging-vs-loguru/) he encontrado una comparación exhaustiva de ambas librerías y me parece importante remarcar el apartado de **Basic Usage** (de momento los demás apartados no son tan relevantes en este proyecto):

```python
import logging
logging.basicConfig(filename='logs/logs.log', level=logging.DEBUG)
logging.debug('Error')
logging.info('Information message')
logging.warning('Warning')
```

```python
from loguru import logger
logger.add('logs/logs.log', level='DEBUG')
logger.debug('Error')
logger.info('Information message')
logger.warning('Warning')
```

A pesar de que ambas librerías tienen una sintaxis muy parecida, la salida que producen tanto en consola como en un fichero es mucho más informativa en **luguru**, y por ello es el framework que se va a usar para el logging.