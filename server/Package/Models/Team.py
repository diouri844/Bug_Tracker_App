
from Package.Db import my_database
import uuid 
from sqlalchemy.dialects.postgresql import UUID


class Team(my_database.Model):
    id = my_database.Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    name = my_database.Column(my_database.String(80), unique=True, nullable=False)
    admin = my_database.Column(UUID(as_uuid=True),nullable=False)
    #projects = my_database.relationship('Project', back_populates='team')
    users = my_database.relationship('User', secondary='user_team_role', 
                                    back_populates='teams'
                                    )
    def __init__(self,name="", admin=""):
        self.name = name
        self.admin = admin
    #add class method to fetch for all users :
    def get_contributors(self):
        userList = my_database.session.query(
            "user_team_role"
        ).filter_by(
            team_id=self.id
        ).all()
        return [user.toDict() for user in userList]
    def toDict(self):
        return dict(
            id=self.id,
            admin=self.admin,
            name=self.name
        )