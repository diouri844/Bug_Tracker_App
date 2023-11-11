from flask import jsonify
from Package.Models.User import User
from Package.Db import my_database

class UserService:
    @staticmethod
    def validatePayload(payload):
        if "userName" in payload and "password" in payload:
            #test len of userName and password: 
            if len(payload["userName"]) < 5 or len(payload["password"]) < 6:
                return False
            #test the content :
            if ' ' in payload["userName"] or ' ' in payload["password"]:
                return False
            return True
        return False
    @staticmethod
    def alreadyUsed(payload):
        userName = payload["userName"]
        #try to get a fetch for user by the user name :
        targetUser = User.query.filter_by(userName=userName).first()
        if targetUser:
            #print( targetUser.toDict())
            return True
        return False
    @staticmethod
    def createUser(userPayload):
        createUser = User(userPayload["userName"], userPayload["password"])
        my_database.session.add(createUser)
        my_database.session.commit()
        return createUser.toDict()
    @staticmethod
    def getUserListPaginated(page=1,per_page=10):
        users = User.query.paginate(
		    page=page,
		    per_page=per_page,
		    error_out=False
	    )
        formated_data = {
		    'items': [users.toDict() for users in users.items],  
		    'page': users.page,
		    'per_page': users.per_page,
		    'total_pages': users.pages,
		    'total_items': users.total,
	    }
        return formated_data
        
