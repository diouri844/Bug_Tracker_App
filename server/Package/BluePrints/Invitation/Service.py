import datetime
from Package.Models.invitation import Invitation
from Package.Db import my_database
from sqlalchemy import and_



class InvitationService:
    @staticmethod
    def getActiveInvitations(user_id,page=1,per_page=10, state=""):
        invitListQuery = Invitation.query.filter(
            and_(
                Invitation.reciver==user_id,
                Invitation.state==state    
            )
        ).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        #clearn the data :
        formated_data = {
            "items": [invitation.toDict() for invitation in invitListQuery],
            "page": invitListQuery.page,
            "per_page": invitListQuery.per_page,
            "total_pages": invitListQuery.pages,
            "total_items": invitListQuery.total
        }
        return formated_data
    @staticmethod
    def getUserInvitations(user_id,page=1,per_page=10):
        invitationList = Invitation.query.filter_by(
            reciver=user_id
        ).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        #format data : 
        formated_data = {
            "items": [invitation.toDict() for invitation in invitationList],
            "page": invitationList.page,
            "per_page": invitationList.per_page,
            "total_pages": invitationList.pages,
            "total_items": invitationList.total
        }
        return formated_data
    @staticmethod
    def get_invitation_details(invitation_id):
        invitationTarget = Invitation.query.filter_by(id=invitation_id).first()
        if not invitationTarget:
            return {"state":False,"data":{}}
        return {
            "state":True,
            "data": invitationTarget.toDict()
        }
    @staticmethod
    def getInvitationById(invitation_id):
        return Invitation.query.filter_by(id=invitation_id).first()
    @staticmethod
    def updateInvitationState(invitationTarget,new_state):
        try:
            invitationTarget["state"] = new_state
            #check if the state is Accepted :
            if new_state == "Accepted":
                #update the accpeted at prop :
                invitationTarget["accepted_at"] = str(datetime.today()).split()[0]
            my_database.session.commit()
            return True
        except Exception as e:
            print("Error updating state of Invitation ", e)
            my_database.session.rollback()
            return False
    @staticmethod
    def create_invitation(payload):
        try:
            InvitationTarget = Invitation(
                sender=payload['sender'],
                reciver=payload['reciver'],
                description=payload["description"]
            )
            #save the Invitation target :
            my_database.session.add(InvitationTarget)
            #commit the transaction
            my_database.session.commit()
            return True
        except Exception as e:
            print("Error creating Invitation ", e)
            my_database.session.rollback()
            return False
    @staticmethod
    def delete_invitation(invitation_id):
        try:
            targetItem = Invitation.query.filter_by(id=invitation_id).first()
            #delete the target :
            my_database.session.delete(targetItem)
            #save the changes :
            my_database.session.commit()
            return True
        except Exception as e:
            print("Error deleting Invitation ", e)
            my_database.session.rollback()
            return False