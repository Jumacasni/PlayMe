# PlayMe

:warning: **Este proyecto aún está en desarrollo** *(versión 0.1)* :warning:

🔧 La configuración del entorno se puede encontrar [aquí](docs/configuracion_git.md)

## Descripción del problema 📝

Hace ya un tiempo que se popularizaron los bares que cuentan con varias estanterías llenas de juegos de mesa para todo tipo de jugadores. Estos sitios se han convertido en el mejor plan para muchas familias, grupos de amigos y amigas, etc. Por ejemplo, aquí en Granada es muy conocido el pub *Continental*, que cuenta con más de 200 juegos de mesa diferentes.

El problema que se encuentra en estos lugares es que es muy difícil elegir un juego entre tantos disponibles y entonces lo que se hace es coger varios de ellos y llevarlos a la mesa. Esto puede derivar a su vez varios problemas:
* El juego resulta aburrido porque no es el tipo de juego que les gusta a los de la mesa, con lo cual todo el tiempo que se ha perdido leyendo las instrucciones, preparando el juego y demás se ha perdido
* Una mesa puede haber cogido diez juegos de mesa pero sólo va a estar utilizando uno (y no se levantan para devolver los nueve restantes), con lo cual estos juegos restantes podrían estar siendo aprovechados por otra mesa
* Hay juegos que no están completos y no se puede jugar porque faltan piezas imprescindibles para poder empezar una partida, y los dueños del local desconocen en qué momento desaparecieron esas piezas
* Para jugar a un juego se necesita un mínimo y máximo número de personas, y el número de personas en la mesa no está en ese rango, con lo cual no se puede empezar la partida y de nuevo se ha perdido el tiempo invertido en decidir el juego

## Solución propuesta y lógica de negocio 🎉

Se propone crear una aplicación para automatizar y facilitar todas las gestiones relacionadas con el préstamo de juegos de mesa.

Los usuarios disponen del catálogo completo de juegos de mesa del local. A este catálogo se le podrán aplicar distintos filtros tales como: número de jugadores en la mesa, tipo de juego, estado del juego (si está incompleto o le faltan piezas), disponibilidad (si el juego está siendo usado por otra mesa), etc. Los usuarios podrán ver todo lo relacionado con el juego, incluyendo reseñas de usuarios, las propias instrucciones del juego y vídeo tutoriales de cómo jugar. Esto evitará que los usuarios tengan que levantarse frecuentemente y tener que mirar caja por caja para ver si finalmente eligen el juego o no.

Los usuarios podrán calificar los juegos de mesa de acuerdo a su experiencia y, a partir de estas calificaciones, recibir recomendaciones de otros juegos de mesa que pueden resultarles interesantes a través de un sistema de recomendación basado en filtrado colaborativo.

El usuario podrá pedir un juego de mesa a traves de la aplicación y quedará registrado con la fecha y hora correspondiente junto con el estado actual del juego. Una vez el juego se devuelva, se registrará la fecha y hora de devolución y de nuevo el estado del juego. Esto permitirá a los dueños del local "descubrir" a los posibles usuarios sospechosos que son responsables de la pérdida de piezas de un juego.

Gracias a esta aplicación los dueños del local podrán mantener un control de los préstamos de juegos de mesa y podrán revisar con más facilidad el estado de estos.


## Licencia 📄

Este proyecto está bajo licencia [GNU Affero General Public License v3.0](LICENSE)