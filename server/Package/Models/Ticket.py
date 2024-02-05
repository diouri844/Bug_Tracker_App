from  Package.Db import my_database
import uuid 
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime, func


class Ticket(my_database.Model):
    id = my_database.Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    title = my_database.Column(my_database.String(100), nullable=False)
    description = my_database.Column(my_database.Text, nullable=False)
    status = my_database.Column(my_database.String(20), default='Open')
    priority = my_database.Column(my_database.String(20), default='Low')
    assigned_user_id = my_database.Column(UUID(as_uuid=True), my_database.ForeignKey('user.id'))
    project_id = my_database.Column(UUID(as_uuid=True), my_database.ForeignKey('project.id'))
    opend_at =  my_database.Column(DateTime(timezone=True), default=func.now())
    closed_at = my_database.Column(DateTime(timezone=True))
    #define contructor : 
    def __init__(self,title="",description="",user_id="",project_id=""):
        self.title = title
        self.description = description
        self.assigned_user_id = user_id
        self.status = "Open"
        self.priority = "Low"
        self.project_id = project_id
    #define my toDict caster method 
    @classmethod
    def toDict(self):
        return dict(
            id=self.id,
            title=self.title,
            description=self.description,
            status=self.status,
            assigned_user_id=self.assigned_user_id,
            status=self.status,
            project_id=self.project_id,
            opend_at = self.opend_at,
            closed_at = self.closed_at
        )