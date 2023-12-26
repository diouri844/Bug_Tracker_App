from flask import jsonify
from Package.Models.Project import Project
from Package.Db import my_database



class ProjectService:
    @staticmethod
    def sayHey():
        return "Hey"