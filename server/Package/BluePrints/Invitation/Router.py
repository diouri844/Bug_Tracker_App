from Package.Models.invitation import Invitation
from Package.Db import my_database
from Package.BluePrints.User.Service import UserService
from Package.BluePrints.Invitation.Service import InvitationService 
from Package.BluePrints import API_PREFIXER, Invitation_PREFIXER
from flask import request, jsonify, Blueprint
from flask_cors import cross_origin


invitation_api = Blueprint("invitation_api", __name__)
Prefixer = API_PREFIXER+Invitation_PREFIXER



@invitation_api.route(Prefixer+"/Ping", methods=["GET"])
@cross_origin()
def ping_handler():
        return jsonify({"Response": "Invitation Pong"}),200

#get all invitiation sended to a user with a specific state : 
@invitation_api.route(Prefixer+"/<target_id>", methods=["GET"])
@cross_origin()
def get_invitation(target_id):
        #get the invit query arg : 
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page",10))
        #add the invit state in the query :
        # definded state  Pending , Sended, Rejected , Accepted
        all_state = ["Pending" , "Sended", "Rejected" , "Accepted"] 
        state = request.args.get("state", all_state[1])
        #check if is a valid state : 
        if not state in all_state:
                return jsonify({"message": "Invalid state "}),400
        #check if the target is already exist : 
        userTarget = UserService.alreadyExists(target_id)
        if not userTarget:
                return jsonify({"message": "User does not exist"}),404
        #call static service to get all pended  invitiation :
        paginatedInvitList = InvitationService.getActiveInvitations(
                user_id=target_id,
                state= state,
                page=page,
                per_page=per_page
        )
        return jsonify({"data": paginatedInvitList}),200

#get all paginated user invitation :
@invitation_api.route(Prefixer+"/<target_id>/list",methods=["GET"])
@cross_origin()
def get_all_invitations(target_id):
        #get the invit query arg : 
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page",10))
        userTarget = UserService.alreadyExists(target_id)
        if not userTarget:
                return jsonify({"message": "User does not exist"}),404
        paginatedInvitList = InvitationService.getUserInvitations(
                target_id,
                page,
                per_page
        )
        return jsonify({"data":paginatedInvitList}),200

#get invitation details by id : 
@invitation_api.route(Prefixer+"/<invitation_id>/details",methods=["GET"])
@cross_origin()
def get_invitation_details(invitation_id):
        #call the static sservice to get the details of the invitation :
        inivtationTargetResult = InvitationService.get_invitation_details(invitation_id)
        if not inivtationTargetResult["state"]:
                return jsonify({"message":"Invitation not found"}),404
        return jsonify({"data":inivtationTargetResult["data"]}),201

#update invitation state : 
@invitation_api.route(Prefixer+"/<invitation_id>/state/<new_state>",methods=["PUT"])
@cross_origin()
def update_invitation_state(invitation_id,new_state):
        #ckeck if the invitation exist : 
        invitationTarget = InvitationService.getInvitationById(invitation_id)
        if not invitationTarget:
                return jsonify({"message":"Invitation not found"}),404
        #update the current state :
        updateStateResult = InvitationService.updateInvitationState(
                invitationTarget,new_state
        )
        if not updateStateResult:
                return jsonify({"message":"Faild to update Invitation state "}),403
        return jsonify({"message": "State updated successufully "}),202
