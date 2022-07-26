from flask import jsonify
from dotenv import load_dotenv
from os.path import dirname, abspath
from pymongo import MongoClient
# importing ObjectId from bson library
from bson.objectid import ObjectId
import os



def get_connexion_details(user_name,user_email,user_password):
    # define cofig vars : 
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    fetch_result_name = list(my_db.User.find(
        {'userEmail':user_email,
         'userPassword':user_password
        }
        ,{'_id':0,'userEmail':0,'userPassword':0}))
    # check datat response :
    if len(fetch_result_name)!=0:
        #data is in the ferst list :
        # check if email == email and pswd == pswd :
        if fetch_result_name[0]['userFname']==user_name or fetch_result_name[0]['userLname']==user_name:
            return "welcom back again  "+str(user_name)
        else:
            return "User account not found "
    return "User Name/email/password is not valid"

def check_account_registration(user_fname,user_lname,user_email,user_password):
    # define cofig vars : 
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    fetch_email = list(my_db.User.find(
        {'userEmail':user_email},{
            'userFName':0,
            'userLName':0,
            'userPassword':0
        }
    ))
    if len(fetch_email)>0: 
        return 1
    else:
        return -1

def create_user_document(user_fname,user_lname,user_email,user_password):
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA    
    try:
        my_db.User.insert_one({
            "userFname":user_fname,
            "userLname":user_lname,
            "userEmail":user_email,
            "userPassword":user_password
        })
        response = "Inser User Documet succuefly "
    except Exception as e:
        print("[ insert user document error ] :  "+str(e))
        response = e
    return response

def get_user_data(user_key):
    # user_key : user_fname, user_lname:
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    response = 0
    try:
        user_check = list(my_db.User.find({'$or':[
            {'userFname':user_key},
            {'userLname':user_key}
        ]},
        {'_id':0}
        ))
        if len(user_check)== 1:
            response = 1
    except Exception as e:
        print("[Error]: "+str(object=e))
        response = -1
    
    return response



# ============= All projects functions services :

def get_project_user(user_target):
    # define cofig vars : 
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    # get query user owner of project :
    project_result = list(my_db.Project.find(
        {
            'Owner':user_target
        },{
            '_id':0
        }
    ))
    # that return a list of project :
    return project_result


def get_project_team(team_target):
    # define cofig vars : 
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    results = list(my_db.Team.find({'$or':[
        {
            "TeamName":team_target
        },
        {
            "TeamManager":team_target
        }]
        },{
            '_id':0
        }))
    return results

def get_project_Id(key):
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    #get project from dba by name :
    results = list(my_db.Project.find({
        'Name':key
    },{
        '_id':0
    }
    ))
    return results

def create_project(data):
    # get connexion with atlas mongodb:
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    # data is an dict:
    return_state = 1
    try:
        contrib_array = []
        for contrib in data['Contributors'].split(","):
            contrib_array.append(contrib)
        my_db.Project.insert_one({
            'Name':data['Name'],
            'Team':data['Team'],
            'Owner':data['Owner'],
            'Contributors':contrib_array,
            'State':data['State'],
            'Discription':data['Describ'],
            'Edate':data['Edate'],
            'Sdate':data['Sdate']
        })
    except Exception as e:
        return_state = -1
    return return_state

def add_project_team(team,project,state):
    reponse = 1
    try:
        # get connexion with atlas mongodb:
        path = dirname(abspath(__file__)) + '/.env'
        load_dotenv(path)
        connexion_uri = os.getenv('DBA_URI')
        # get connexion with atlas mongodb :
        my_client = MongoClient(connexion_uri)
        my_db = my_client.BUG_TRAKER_DBA
        my_db.Team.update_one({
            'TeamName':team
        },{
            '$addToSet':
                {
                'TeamProject':project,
                'ProjectState':state
                },
                'upsert': true
            }
        )
    except Exception as e:
        print("[Error add project to team ]: "+str(e))
        response = -1
    return reponse


# =========== All team functions services : 

def create_team(team_data):
    # get connexion with atlas mongodb:
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    response = 1
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    # insert document :
    try:
        my_db.Team.insert_one({
            'TeamName':team_data['TeamName'],
            'TeamManager':team_data['TeamManeger'],
            'TeamGroup':[],
            'TeamProject':[],
            'ProjectState':[]
        })
    except Exception as e:
        response = -1
    return response

def add_user_to_team(user_target,team_target):
    # get connexion with atlas mongodb:
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    response = 1
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    # try  update contrib liste :
    try:
        my_db.Team.update_one({
            #filter:
            'TeamName':team_target
        },{
            #update scope:
            '$addToSet':{
                'TeamGroup':user_target
            }
        })
    except Exception as e:
        print("[add user to team contrib error ] : "+str(e))
        response = -1
    return response

# ============= invitations processe : 
def send_invitation(invitation):
    reponse = 1
    # get connexion with atlas mongodb:
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    try:
        if 'State' in invitation:
            my_db.InvitationContib.insert_one({
                'From':invitation['from'],
                'To':invitation['To'],
                'Type':invitation['Type'],
                'Target':invitation['Target'],
                'Subject':invitation['Subject'],
                'State':invitation['State']
            })
        else:
            my_db.InvitationContib.insert_one({
                'From':invitation['from'],
                'To':invitation['To'],
                'Type':invitation['Type'],
                'Target':invitation['Target'],
                'Subject':invitation['Subject'],
                'State':'Sended'
            })
    except Exception as e:
        print("add invit error : "+str(e))
        reponse = -1
    return reponse

def get_invitation_user(user):
    # get connexion with atlas mongodb:
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    try:
        invitations = list(my_db.InvitationContib.find({
            'To':user
        },
        {
            '_id':0
        }))
        return invitations
    except Exception as e:
        return -1

def update_invit(invitation,state):
    # get connexion with atlas mongodb :
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    # try update state :
    try:
        my_db.InvitationContib.update_one({
            'From':invitation['From'],
            'Type':invitation['Type'],
            'Target':invitation['Target']
        },{
            "$set":{
                'State':state
            }
        })
        return 1
    except Exception as e:
        print("[ update_invit Error ] : "+str(e))
        return -1

def delet_invitation(invitation):
    # get connexion with atlas mongodb :
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    # try delet- invitation :
    try:
        my_db.InvitationContib.delete_one({
            # filter : 
            'From':invitation['From'],
            'Type':invitation['Type'],
            'Target':invitation['Target'],
            'To':invitation['To']
        })
    except Exception as e:
        print("[ delet invitation error ] : "+str(e))
    return

def drup_all_invitation(user):
    # get connexion with atlas mongodb :
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    try:
        my_db.InvitationContib.delete_many({'To':user})
    except Exception as e:
        print("[clear all invitations error ] : "+str(e))
    return