from Package.Db import my_database
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime, func


class Invitation(my_database.Model):
    id = my_database.Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    description = my_database.Column(my_database.String(1000))
    sender = my_database.Column(UUID(as_uuid=True), my_database.ForeignKey('user.id'))
    reciver = my_database.Column(UUID(as_uuid=True), my_database.ForeignKey('user.id')) 
    state = my_database.Column(my_database.String(50))
    received_at = my_database.Column(DateTime(timezone=True), default=func.now())
    accepted_at = my_database.Column(DateTime(timezone=True))
    def __init__(self,sender="",reciver="",description=""):
        self.sender = sender
        self.reciver = reciver
        self.description = description
        self.state = "pending"
    @classmethod
    def setState(self,newState):
        self.state = newState
        return
    def toDict(self):
        return dict(
            id=self.id,
            description=self.description,
            sender=self.sender,
            reciver=self.reciver,
            state=self.state,
            received_at=self.received_at,
            accepted_at=self.accepted_at
        )