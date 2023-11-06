# User Class : 
from passlib.hash import pbkdf2_sha256
import uuid 
from sqlalchemy.dialects.postgresql import UUID
from Package.Db import my_database
# from Modules.Database.Permission import Permission
class User(my_database.Model):
	id = my_database.Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
	userName = my_database.Column(my_database.String(64),unique=True, nullable=False)
	password = my_database.Column(my_database.String(256), nullable=False)
	teams = my_database.relationship(
			'Team', 
			secondary='user_team_role', 
			back_populates='users'
	)
	#permissions = my_database.relationship('Permission', secondary='user_permission')
	def __init__(self, username="", password=""):
		self.userName = username
		self.setPassword(password)
		# self.setPermissions()
	def setPassword(self, password):
		self.password = pbkdf2_sha256.hash(password)
	def checkPassword(self, password):
		return pbkdf2_sha256.verify(password, self.password)
	@staticmethod
	def hashPassword(password):
		return pbkdf2_sha256.hash(password)
	@staticmethod
	def isSamePassword(password, hasehdPswd):
		return pbkdf2_sha256.verify(password,hasehdPswd)
	# def setPermissions(self):
		# for permission_data in Permission.query.all():
		# 	self.permissions.append(permission_data)
	# def get_permissions(self):
	# 	return [permission.name for permission in self.permissions] 
	def get_password(self):
		return self.password
	def toDict(self):
		return dict(
			id=self.id, 
			userName=self.userName
		)