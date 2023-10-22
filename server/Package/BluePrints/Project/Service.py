from flask import jsonify
from dotenv import load_dotenv
from os.path import dirname, abspath
from pymongo import MongoClient
# importing ObjectId from bson library
from bson.objectid import ObjectId
import os



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

def add_contribs_to_project(project,list_contrib):
    # define cofig vars : 
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    try:
        # get team name 
        my_db.Project.update_one({
            # filter :
            'Name':project
        },
        {
            '$set':{
                'Contributors':list_contrib
            }
        })
        return 1
    except Exception as e:
        print("[ add contrib to project error ] : "+str(e))
        return -1

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

def get_project_state(key):
    #get connexion with atlas mongodb:
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    try:
        return list(my_db.Project.find({
            #filter :
            'Name':key
            },{
            'State':1
            }))[0]['State']
    except Exception as e:
        print("[ Get project state Error ] : "+str(e))
        return ""

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
        my_db.Project.insert_one({
            'Name':data['Name'],
            'Team':data['Team'],
            'Owner':data['Owner'],
            'Contributors':data['Contributors'],
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
        my_state = get_project_state(project)
        print("\n Project : ",project," state :  ",my_state)
        if my_state != "":
            state = my_state
            print("\n Project : ",project," state :  ",state)
        my_client = MongoClient(connexion_uri)
        my_db = my_client.BUG_TRAKER_DBA
        # step 1 : get all project name and all project state 
        data_team = list(
            my_db.Team.find(
                {
            'TeamName':team
                },{
                    'TeamName':0,
                    'TeamManager':0,
                    '_id':0,
                    'TeamGroup':0
                }))
        # [{'TeamProject': ['tkinter_app', 'Qt_app', 'project_D'], 'ProjectState': ['On hold', 'On progress']}]
        project_list = data_team[0]['TeamProject']
        state_list = data_team[0]['ProjectState']
        # step 2 : add the new project to to list project exported 
        if not project in project_list:
            project_list.append(project)
            state_list.append(state)
        # update the collection document :
        my_db.Team.update_one({
            'TeamName':team
        },{
            '$set':
                {
                'TeamProject':project_list,
                'ProjectState':state_list
                }
            }
        )
        # update project team name if is "Not-definded ":
        project_team_name = list(
            my_db.Project.find({
                'Name':project
            },{
                '_id':0
            })
        )[0]['Team']
        # check if team name is : Not-found
        if project_team_name == 'Not-found':
            # update team name :
            my_db.Project.update_one(
                {
                    'Name':project
                },
                {
                    '$set':{
                        'Team':team
                    }
                }
            )
    except Exception as e:
        print("[Error add project to team ]: "+str(e))
        reponse = -1
    return reponse

def remove_project(project):
    # get connexion with atlas mongodb:
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    response = 0
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    try:
        my_db.Project.delete_one({
            # filter :
            'Name':project
        })
        response =  1
    except Exception as e:
        print("[ delet team name from project error ] : "+str(e))
        response =  -1
    return response


def remove_team_from_project(project):
    # get connexion with atlas mongodb:
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    response = 0
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    my_db = my_client.BUG_TRAKER_DBA
    try:
        my_db.Project.update_one(
            {
             'Name':project   
            },
            {
                '$set':{
                    'Team':'Not-found'
                }
            })
        response = 1
    except Exception as e:
        print("[ delete tema name from project error ] : "+str(e))
        response = -1
    return response

