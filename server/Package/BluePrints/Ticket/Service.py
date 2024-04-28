import datetime
from Package.Models.Ticket import Ticket
from Package.Db import my_database
from sqlalchemy import and_



class TicketService:
    @staticmethod
    def get_ticket_list(page=1, per_page=10, status="Open"):
        #fetch for all tickets :
        ticket_list = Ticket.query.filter(Ticket.status == status).paginate(
            page=page, per_page=per_page, error_out=False
        )
        # Format the paginated ticket data into a dictionary
        formated_data = {
            "items": [
                { 
                    "id":ticket.id,
                    "title":ticket.title,
                    "description":ticket.description,
                    "status":ticket.status,
                    "assigned_user_id":ticket.assigned_user_id,
                    "project_id":ticket.project_id,
                    "opend_at":ticket.opend_at,
                    "closed_at":ticket.closed_at
                 } for ticket in ticket_list.items],
            "page": ticket_list.page,
            "per_page": ticket_list.per_page,
            "total_pages": ticket_list.pages,
            "total_items": ticket_list.total
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
    @staticmethod
    def get_project_ticket(project_id, page=1, per_page=10):
        TicketList = Ticket.query.filter(
            project_id==project_id
        ).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        #format data :
        formated_data = {
            "items": [ ticker.toDict() for ticker in TicketList],
            "page":TicketList.page,
            "per_page":TicketList.per_page,
            "total_pages":TicketList.pages,
            "total_items":TicketList.total
        }
        return formated_data
    @staticmethod
    def get_user_ticket(user_id,page=1,per_page=10, status="All"):
        TickerList = Ticket.query.filter(
            and_(
                Ticket.assigned_user_id==user_id,
                Ticket.status==status
            )
        ).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        #format data : 
        formated_data = {
            "items": [ item.toDict() for item in TickerList.items ],
            "page":TickerList.page,
            "per_page":TickerList.per_page,
            "total_pages":TickerList.pages,
            "total_items":TickerList.total
        }
        return formated_data
    @staticmethod
    def set_ticket_status(ticket_payload, new_date):
        try:
            ticket_payload["status"] = "Closed"
            ticket_payload["closed_at"] = new_date
            my_database.session.commit()
        except Exception as e:
            print( "Error Updating ticket ", e)
            my_database.session.rollback()
            return False
    @staticmethod
    def set_ticket_priority(ticket_payload, ticket_priority):
        try:
            ticket_payload["priority"] = ticket_priority
            my_database.session.commit()
        except Exception as e:
            print( "Error Updating ticket priority ", e)
            my_database.session.rollback()
            return False
    @staticmethod
    def create_ticket(ticket_payload, project_id):
        try:
            ticker_to_add = Ticket(
                title=ticket_payload["title"],
                description=ticket_payload["description"],
                user_id=ticket_payload["assigned_user_id"],
                project_id=project_id
            )
            my_database.session.add(ticker_to_add)
            my_database.session.commit()
            return True
        except Exception as e:
            print( "Error Creating ticket ", e)
            my_database.session.rollback()
            return False