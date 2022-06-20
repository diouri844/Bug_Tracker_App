from flask import jsonify
from dotenv import load_dotenv
from os.path import dirname, abspath
from pymongo import MongoClient
import os



def get_connexion_details(user_name,user_email,user_password):
    # define cofig vars : 
    path = dirname(abspath(__file__)) + '/.env'
    load_dotenv(path)
    connexion_uri = os.getenv('DBA_URI')
    # get connexion with atlas mongodb :
    my_client = MongoClient(connexion_uri)
    query ="{$or: [{userFName:"+str(user_name)+"},{userLName:"+str(user_name)+"}]}"
    my_db = my_client.BUG_TRAKER_DBA
    fetch_result_ferst_name = list(my_db.User.find({'userFName':user_name},{'_id':0,'userFName':0,'userLName':0}))
    fetch_result_last_name = list(my_db.User.find({'userLName':user_name},{'_id':0,'userFName':0,'userLName':0}))
    print(fetch_result_ferst_name,fetch_result_last_name)
    return fetch_result_last_name
