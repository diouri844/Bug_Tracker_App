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
        projetTarget = Project.query.filter_by(id=project_id).first()
        if not projetTarget:
            return {}
        return projetTarget.toDict()