from Package.Models.Team import Team
from Package.BluePrints.Team.Service import TeamService
from Package.BluePrints.User.Service import UserService
#import User prefixer endpoint : 
from Package.BluePrints import Team_PREFIXER, API_PREFIXER
from Package.Db import my_database
#define user bluePrint here with all the routes and the controllers : 
from flask import request, jsonify, Blueprint 
# import flask cors configuration lib : 
from flask_cors import cross_origin



team_api = Blueprint("team_api",__name__)
Prefixer = API_PREFIXER+Team_PREFIXER


#define my test ping for team endpoint:

@team_api.route(Prefixer+"/Ping", methods=["GET"])
@cross_origin()
def ping_handler():
    return jsonify({"Response": "Team Pong"})


# router endpoint to get the list of all teams in the database : 

@team_api.route(Prefixer+"/List", methods=["GET"])
@cross_origin()
def get_team_list():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page",20))
    #call the service :
    formated_data = TeamService.getTeamListPaginated(page, per_page)
    return jsonify({"data":formated_data}),200

#get team by id :
@team_api.route(Prefixer+"/<team_id>",methods=["GET"])
@cross_origin()
def get_team_data(team_id):
    try:
        targetTeam = Team.query.filter_by(id=team_id).first()
        if not targetTeam:
            return jsonify({"message":"Not Found"}),400
        return jsonify({"data":targetTeam.toDict()}),200
    except Exception as e:
        print( e )
        return jsonify({"message": "Error getting team"}),404


#get team admin information :
@team_api.route(Prefixer+"/<team_id>/Administrator",methods=["GET"])
@cross_origin()
def get_team_admin(team_id):
    #check it the team exist :
    isExist = TeamService.alreadyExist(team_id)
    if not isExist:
        return jsonify({"message": "Team not found"}),400
    #call the service method:
    adminTarget = TeamService.getTeamAdmin(team_id)
    print( adminTarget )
    return jsonify({"data": adminTarget }),200


#create new team :
@team_api.route(Prefixer+"/New/<admin_id>", methods=["POST"])
@cross_origin()
def create_new_team(admin_id):
    #check is admin exist :
    adminTarget = UserService.alreadyExists(admin_id)
    if not adminTarget:
        return jsonify({"message": "User not found"}),400
    #extract the paload from the request : 
    newTeamPayload = request.json
    #check if the payload has a name prop :
    if not "name" in newTeamPayload:
        return jsonify({"message": "Name is required"}),404
    #check if the provided name is not already used :
    teamName = newTeamPayload["name"]
    teamNameExist = TeamService.checkTeamByName( teamName )
    if teamNameExist:
        return jsonify({"message": "Team Name is already in use "}),404
    #call static method to create new team:
    createdTeamResponse = TeamService.createNewTeam(teamName,admin_id)
    if not createdTeamResponse["created"]:
        return jsonify({"message": "Faild create Team "}),500
    return jsonify({
        "message": "Team Created successfully",
        "team":createdTeamResponse["target"]
        }
    ),201

#update the admin by id :
@team_api.route(Prefixer+"<team_id>/Administrator/New/<user_id>",methods=["PUT"])
@cross_origin()
def update_team_admin(team_id, user_id):
    #check if team exists:
    alreadyExist = TeamService.alreadyExist(team_id)
    if not alreadyExist:
        return jsonify({"message": "Team not found"}),400
    #check if user exists
    userAlreadyExist = UserService.alreadyExists(user_id)
    if not userAlreadyExist:
        return jsonify({"message": "User not found"}),400
    #update :
    #call service :
    updateState = TeamService.setNewTeamAdmin(team_id, user_id)
    if not updateState:
        return jsonify({"message": "Failed to update team admin"}),404
    return jsonify({"message": "Team admin updated successfully"}),201

#update the team name by id :

@team_api.route(Prefixer+"/<team_id>", methods=["PUT"])
@cross_origin()
def update_team_name(team_id):
    #check if team exists:
    alreadyExist = TeamService.alreadyExist(team_id)
    if not alreadyExist:
        return jsonify({"message": "Team not found"}),400
    newTeamPayload = request.json
    #check if team containe a new tean name prop : 
    if not "name" in newTeamPayload:
        return jsonify({"message":"Team is Up to date"}),200    
    newTeamName = newTeamPayload["name"]
    #check if the team name not already exist :
    isNameAlreadyExists = TeamService.checkTeamByName(newTeamName)
    if isNameAlreadyExists:
        return jsonify({"message":"Team name already used "}),403 
    #call the service to update the team name :
    updatedNameState = TeamService.updateteamName(team_id,newTeamName)
    #check the status of the updated service call :
    if updatedNameState:
        return jsonify({"message": "Team name updated successfully"})
    return jsonify({"message":"Faild to update team name "}),404

#get team members by id :
@team_api.route(Prefixer+"/<team_id>/members", methods=["GET"])
@cross_origin()
def get_team_members(team_id):
    #check if team exists:
    alreadyExist = TeamService.alreadyExist(team_id)
    if not alreadyExist:
        return jsonify({"message": "Team not found"}),400
    #call the service :
    contributorList = TeamService.getTeamMembers(team_id)
    return jsonify({"data":contributorList}), 200


