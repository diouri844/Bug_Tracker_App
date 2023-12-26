from Package.Models.Project import Project
from Package.BluePrints.Project.Service import ProjectService
from Package.BluePrints import Project_PREFIXER, API_PREFIXER
from flask import request, jsonify, Blueprint 
# import flask cors configuration lib : 
from flask_cors import cross_origin




project_api = Blueprint("project_api", __name__)
Prefixer = API_PREFIXER+Project_PREFIXER



@project_api.route(Prefixer+"/Ping", methods=["GET"])
@cross_origin()
def ping_handler():
        return jsonify({"Response": "Team Pong"}),200
