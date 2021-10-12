from usuario import Usuario

class Trabajador(Usuario):
	def __init__(self, nombre, email):
		super().__init__(nombre, email)