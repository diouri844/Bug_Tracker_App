from flask import jsonify
from dotenv import load_dotenv
from os.path import dirname, abspath
from pymongo import MongoClient
# importing ObjectId from bson library
from bson.objectid import ObjectId
import os




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
            if 'TeamName' in invitation:
                my_db.InvitationContib.insert_one({
                    'From':invitation['from'],
                    'To':invitation['To'],
                    'Type':invitation['Type'],
                    'Target':invitation['Target'],
                    'Subject':invitation['Subject'],
                    'TeamName':invitation['TeamName'],
                    'State':invitation['State']
                })
            else:
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
        my_db.InvitationContib.delete_many(
            {
                'To':user,
                'State':{
                    '$in':["Accept","Refuse",""]
                }
            })
    except Exception as e:
        print("[clear all invitations error ] : "+str(e))
    return