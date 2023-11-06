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
        
