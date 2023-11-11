from Package.Models.User import User
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