from Package.Models.Ticket import Ticket
from Package.BluePrints.Ticket.Service import TicketService
from Package.BluePrints.Project.Service import ProjectService
from Package.BluePrints.User.Service import UserService
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


#get ticket list by status :
@ticket_api.route(Prefixer+"/list", methods=["GET"])
@cross_origin()
def get_tcket_list():
    #get query parameters :
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page",10))
    #target state of ticket needed : opened , cloded :
    status = request.args.get("status", "open")
    #call static service to get the ticket list :
    tickerList = TicketService.get_ticket_list(
        page=page,
        per_page=per_page,
        status=status
    )
    return jsonify({"data":tickerList}),200


#get ticket dtails by id :
@ticket_api.route(Prefixer+"/<ticket_id>/details", methods=["GET"])
@cross_origin()
def getTicketDtails(ticket_id):
    #call static method to get ticket dtails by ticket id or none :
    targetObject = TicketService.get_ticket_details(ticket_id)
    if not targetObject["state"]:
        return jsonify({"message": "Ticket not found"}),404
    return jsonify({"data":targetObject["data"]}),201


#get a project related ticket list :
@ticket_api.route(Prefixer+"/Projects/<project_id>/tickets",methods=["GET"])
@cross_origin()
def getProjectsTicket(project_id):
    #ckeck if the project exist : 
    projectTarget = ProjectService.get_project_by_id(project_id)
    #chcekt the result :
    if not projectTarget["state"]:
        return jsonify({"message": "Project not found"}),404
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page",10))
    #call static service to fetch all the ticket related to the project target :
    projectTicket = TicketService.get_project_ticket(
        project_id=project_id,
        page=page,
        per_page=per_page
    )
    return jsonify({"data":projectTicket}),201

#get ticket list assigned to a user :
@ticket_api.route(Prefixer+"/User/<user_id>", methods=["GET"])
@cross_origin()
def getUserTickets(user_id):
    #check the user id :
    userTarget = UserService.alreadyExists(user_id)
    if not userTarget:
        return jsonify({"message": "User not found"}),404
    status = request.args.get("status","All")
    if status and not status in ["Open", "Closed", "All"]:
        return jsonify({"message": "Status not available"}),403
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page",10))
    
    userTicket = TicketService.get_user_ticket(
        user_id=user_id,
        page=page,
        per_page=per_page,
        status=status
    )
    return jsonify({"data":userTicket}),201