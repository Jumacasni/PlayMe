from usuario import Usuario
from datetime import datetime

class Cliente(Usuario):
	def __init__(self, nombre, email):
		super().__init__(nombre, email)
		self.fecha_alta = datetime.now()