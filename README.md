# PlayMe

:warning: **Este proyecto aún está en desarrollo** *(versión 0.1)* :warning:

🔧 La configuración del entorno se puede encontrar [aquí](docs/configuracion_git.md)

## Descripción del problema 📝

Hace ya un tiempo que se popularizaron los bares que cuentan con varias estanterías llenas de juegos de mesa para todo tipo de jugadores. Estos sitios se han convertido en el mejor plan para muchas familias, grupos de amigos y amigas, etc. Por ejemplo, aquí en Granada es muy conocido el pub *Continental*, que cuenta con más de 200 juegos de mesa diferentes.

El problema que se encuentra en estos lugares es que es muy difícil elegir un juego entre tantos disponibles y entonces lo que se hace es coger varios de ellos y llevarlos a la mesa. Esto puede derivar a su vez varios problemas:
* Los dueños del local no pueden proporcionar un juego de mesa porque otras mesas se han adelantado y tampoco pueden predecir el tiempo que van a invertir en él, es decir, el tiempo que pasará hasta que vuelva a estar disponible.
* El juego resulta aburrido porque no es el tipo de juego que les gusta a los de la mesa, con lo cual todo el tiempo que se ha invertido leyendo las instrucciones, preparando el juego y demás se ha perdido
* Una mesa puede haber cogido diez juegos de mesa pero sólo va a estar utilizando uno (y no se levantan para devolver los nueve restantes), con lo cual estos juegos restantes podrían estar siendo aprovechados por otra mesa
* Un juego de mesa tiene un tiempo de juego estimado, pero una mesa está perdiendo el tiempo a propósito desaprovechando el juego y por lo tanto dejando a otras personas sin disfrutar de él
* Hay juegos que no son usados prácticamente y ocupan un espacio que podrían ocupar otros juegos que sí tienen más interés entre los clientes del local, al igual que hay juegos que gustan mucho y de los que podría haber más unidades en el local.

## Solución propuesta y lógica de negocio 🎉

Se propone crear una aplicación para automatizar y facilitar todas las gestiones relacionadas con el préstamo de juegos de mesa.

Los usuarios disponen del catálogo completo de juegos de mesa del local. A este catálogo se le podrán aplicar distintos filtros tales como: número de jugadores en la mesa, tipo de juego, estado del juego (si está incompleto o le faltan piezas), disponibilidad (si el juego está siendo usado por otra mesa), etc. Los usuarios podrán ver todo lo relacionado con el juego, incluyendo reseñas de usuarios, las propias instrucciones del juego y vídeo tutoriales de cómo jugar. Esto evitará que los usuarios tengan que levantarse frecuentemente y tener que mirar caja por caja para ver si finalmente eligen el juego o no. Si un juego no está disponible porque está usándose en otras mesas, podrán ver **el tiempo estimado para que un juego vuelva a estar disponible**.

Los usuarios podrán calificar los juegos de mesa de acuerdo a su experiencia y, a partir de estas calificaciones, recibir **recomendaciones** de otros juegos de mesa que pueden resultarles interesantes a través de un **sistema de recomendación**.

Los dueños del local podrán **optimizar el tiempo** que las mesas usan los distintos juegos, basándose en el tiempo medio de un juego para un cierto número de jugadores. De esta manera, pueden también **calcular el tiempo para que una mesa termine de jugar a un juego**.

Los dueños del local también podrán analizar **cuáles son los juegos más (menos) usados** en el local y **predecir** qué juegos nuevos pueden tener más (menos) éxito.

## Licencia 📄

Este proyecto está bajo licencia [GNU Affero General Public License v3.0](LICENSE)
