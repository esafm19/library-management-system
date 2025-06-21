class TentangDAO():
	def __init__(self, DAO):
		self.db = DAO
		self.db.table = "users"


	