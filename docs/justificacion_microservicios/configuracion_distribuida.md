# Configuración distribuida

Aunque de momento no se ha pedido una "aplicación" lanzable, sí que es necesario proporcionar una configuración de nuestro proyecto. La configuración distribuida permite definir, entre otros, la dirección IP y el puerto necesarios para los microservicios (aunque en este caso sólo hay un microservicio, de momento). Entre las distintas opciones se han barajado 3 de las más importantes:

- Etcd
- Consul
- Zookeper

En este [artículo](https://medium.com/micro/deprecating-consul-in-favour-of-etcd-421941a538a6) de 2019 se describe la necesidad de dejar Consul hacia un lado y moverse hacia Etcd debido a los cambios que están sucediendo en las tecnologías cloud que están haciendo aparecer ciertos issues en Consul.

Para decidir entre Etcd y Zookeper he echado un vistazo a este [artículo](https://dzone.com/articles/apache-zookeeper-vs-etcd3) en el cual se muestran las diferentes ventajas y desventajas de cada uno de ellos. Sin duda, Etcd resulta más adecuado para este proyecto debido a una configuración mucho más sencilla y debido a que Zookeper abre uan nueva conexión por cada petición, haciendo las conexiones mucho más complejas.

## Configuración de Etcd

Python cuenta con el paquete ```etcd3``` para poder coger la configuración deseada (en este caso, la dirección IP y el puerto).

A modo de simulación, en mi máquina local y usando ```etcdctl``` (etcd command line) he configurado un puerto y un host:

<img src="https://github.com/Jumacasni/PlayMe/blob/main/img/etcd.png" width="100%" height="100%">

A continuación, he creado un archivo [server.py](https://github.com/Jumacasni/PlayMe/blob/main/server.py) para simular el lanzamiento de la aplicación retomando el puerto y el host usando el paquete de Python3:

```python
if __name__ == "__main__":
	client = etcd3.client()

	puerto = client.get('puerto')[0]
	host = client.get('host')[0]
```
