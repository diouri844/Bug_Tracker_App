from Package.Models.Project import Project
from Package.BluePrints.Project.Service import ProjectService
from Package.BluePrints import Project_PREFIXER, API_PREFIXER
from flask import request, jsonify, Blueprint 
# import flask cors configuration lib : 
from flask_cors import cross_origin




project_api = Blueprint("project_api", __name__)
Prefixer = API_PREFIXER+Project_PREFIXER


#test ping :
@project_api.route(Prefixer+"/Ping", methods=["GET"])
@cross_origin()
def ping_handler():
        return jsonify({"Response": "Project Pong"}),200

#get all project list :
@project_api.route(Prefixer+"/List", methods=["GET"])
@cross_origin()
def get_project_list():
        #get metadata from request params :
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page",10))
        #call static method to get project list:
        projectList = ProjectService.get_project_list(page,per_page)
        return jsonify({"data": projectList}),200

#get a project by id :
@project_api.route(Prefixer+"/<project_id>", methods=["GET"])
@cross_origin()
def get_project_by_id(project_id):
        return jsonify()

