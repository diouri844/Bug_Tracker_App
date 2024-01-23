from Package.Models.invitation import Invitation
from Package.BluePrints import API_PREFIXER, Invitation_PREFIXER
from flask import request, jsonify, Blueprint
from flask_cors import cross_origin


invitation_api = Blueprint("invitation_api", __name__)
Prefixer = API_PREFIXER+Invitation_PREFIXER



@invitation_api.route(Prefixer+"/Ping", methods=["GET"])
@cross_origin()
def ping_handler():
        return jsonify({"Response": "Invitation Pong"}),200
