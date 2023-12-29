from flask import jsonify
from Package.Models.Project import Project
from Package.Db import my_database



class ProjectService:
    @staticmethod
    def get_project_list(page,per_page):
        Project_list = Project.query.paginate(
            page=page, 
            per_page=per_page,
            error_out=False
        )
        formated_data = {
            "items":[ project.toDict() for project in Project_list ],
            "page": Project_list.page,
            "per_page":Project_list.per_page,
            "total_pages":Project_list.pages,
            "total_items":Project_list.total
        }
        return formated_data
    @staticmethod
    def get_project_by_id(project_id):
        #define the return object :
        returnValues = {
            "state":False,
            "data":{}
        }
        projetTarget = Project.query.filter_by(id=project_id).first()
        if not projetTarget:
            return returnValues
        #update the return values:
        returnValues["state"] = True
        returnValues["data"] = projetTarget.toDict()
        return returnValues 
    @staticmethod
    def get_project_by_name(project_name):
        #make sure that the project name is in lowercase:
        name = str(project_name).lower()
        returnValues = {
            "state":False,
            "data":{}
        }
        #try to find the project by name:
        projectToFind = Project.query.filter_by(name=name).first()
        if not projectToFind:
            return returnValues
        #update states :
        returnValues["state"] = True
        returnValues["data"] = projectToFind.toDict()
        return returnValues