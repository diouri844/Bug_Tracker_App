import datetime
from Package.Models.Ticket import Ticket
from Package.Db import my_database
from sqlalchemy import and_



class TicketService:
    @staticmethod
    def get_ticket_list(page=1, per_page=10, status="open"):
        #fetch for all tickets :
        TicketList = Ticket.query.filter(
            status==status
        ).paginate(
            page=page, 
            per_page=per_page,
            error_out=False
        )
        #clean data :
        formated_data = {
            "items": [ ticket.toDict() for ticket in TicketList],
            "page":TicketList.page,
            "per_page":TicketList.per_page,
            "total_pages":TicketList.pages,
            "total_items":TicketList.total
        }
        return formated_data
    @staticmethod
    def get_ticket_details(ticket_id):
        response = dict(
            state=False,
            data={}
        )
        try:
            target = Ticket.query.filter_by(id=ticket_id).first()
            if not target:
                response["state"] = False
            response["data"] = target.toDict()
            response["state"] = True
        except Exception as e:
            print("Error getting ticket details ", e)
            response["state"] = False
        return response