from App.Tentang import Tentang

class TentangManager():
    def __init__(self, DAO):
		self.tentang = Tentang(DAO.db.user)
		self.dao = self.user.dao