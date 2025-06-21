from App.Tentang import Tentang

class TentangManager():
    def __init__(self, DAO):
	    self.user = Tentang(DAO.db.user)
	    self.book = DAO.db.book
		self.dao = self.user.dao
		
    def list(self):
		user_list = self.dao.list()

		return user_list