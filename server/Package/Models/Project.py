from Package.Db import my_database
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text


class Project(my_database.Model):
    id = my_database.Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    name = my_database.Column(my_database.String(80), unique=True, nullable=False)
    manager = my_database.Column(UUID(as_uuid=True), my_database.ForeignKey('user.id'))
    description = my_database.Column(my_database.String(1000))
    repo_url = my_database.Column(my_database.String(255), nullable=False)
    state = my_database.Column(my_database.String(50))
    teams = my_database.relationship("Team", 
                                    secondary="team_project",
                                    back_populates="projects"
                                )
    def __init__(self,name="",manager="",repo_url=""):
        self.name = name
        self.manager = manager
        self.repo_url = repo_url
        self.description = "Default description you can update it later"
        self.state = "CREATED"
    def toDict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            state=self.state,
            url=self.repo_url
        )