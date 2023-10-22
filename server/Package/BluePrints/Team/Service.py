from flask import jsonify
from dotenv import load_dotenv
from os.path import dirname, abspath
from pymongo import MongoClient
# importing ObjectId from bson library
from bson.objectid import ObjectId
import os


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

def get_contributors(team):
    # define cofig vars : 
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    try:
        return list(my_db.Team.find({
            # filter :
            'TeamName':team   
        },{
            '_id':0,
            'TeamName':0,
            'TeamManager':0,
            'TeamProject':0,
            'ProjectState':0
        }))[0]['TeamGroup']
    except Exception as e:
        print("[error get tema contribs ]:  "+str(e))
        return [] 
