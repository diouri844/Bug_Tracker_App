from Package.Models.Ticket import Ticket
from Package.Db import my_database
from Package.BluePrints import API_PREFIXER, Ticker_PREFIXER
from flask import request, jsonify , Blueprint
from flask_cors import cross_origin



ticket_api = Blueprint("ticket_api", __name__)
Prefixer = API_PREFIXER + Ticker_PREFIXER


@ticket_api.route(Prefixer+"/Ping", methods=["GET"])
@cross_origin()
def ping_handler():
    return jsonify({"Response": "Ticket Pong"}),200
