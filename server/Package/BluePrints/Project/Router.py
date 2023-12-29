from Package.Models.Project import Project
from Package.Models.User import User
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
        #try to get the project by id :
        projectFindResult = ProjectService.get_project_by_id(project_id)
        #check the values :
        if not projectFindResult["state"]:
                return jsonify({"message": "Project not found"}),404
        return jsonify({"data": projectFindResult["data"]}),200

#get project by name :
@project_api.route(Prefixer+"/Find/Name/<project_name>", methods=["GET"])
@cross_origin()
def get_project_by_name(project_name):
        try:
                projectTarget = ProjectService.get_project_by_name(project_name)
                if not projectTarget["state"]:
                        return jsonify({"message": "Project not found"}),404
                return jsonify({"data": projectTarget["data"]}),202
        except Exception as e:
                print( e )
                return jsonify({"message": "Faild to find Project"}),400

#get a project manager by the project id :
@project_api.route(Prefixer+"/Manager/<project_id>", methods=["GET"])
@cross_origin()
def get_project_manager(project_id):
        #check if the project exist :
        isProjectExist = ProjectService.get_project_by_id(project_id)
        if not isProjectExist:
                return jsonify({"message": "Project not found"}),404
        #project is already exit : extract the manager id from the project dict :
        manager_id = isProjectExist["manager"]
        #call user service to get the manager ( user ) by id :
        managerTarget = User.query.filter_by(id=manager_id).first()
        if not managerTarget:
                return jsonify({"message": "Manager not found"}),404
        return jsonify({"data":managerTarget.toDict()}),202

#get teams information that working on the project by project id :
@project_api.route(Prefixer+"/TeamList/<project_id>", methods=["GET"])
@cross_origin()
def get_prject_team_list(project_id):
        return jsonify(),200