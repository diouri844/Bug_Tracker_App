#import user model from models 
from Package.Models.User import User
#import User prefixer endpoint : 
from Package.BluePrints import User_PREFIXER, API_PREFIXER
from Package.Db import my_database
#define user bluePrint here with all the routes and the controllers : 
from flask import Flask, request, session, jsonify, Blueprint 
# import flask cors configuration lib : 
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os
import jwt
import datetime


#define my bluePrint :
user_api = Blueprint("user_api", __name__)
Prefixer = API_PREFIXER+User_PREFIXER

@user_api.route(Prefixer+"/Ping", methods=["GET"])
#@token_required
@cross_origin()
def ping_handler():
	return jsonify({"Response": "User Pong"})

#get list of users:
@user_api.route(Prefixer+"/List", methods=["GET"])
@cross_origin()
def get_user_list():
	#paginate data : 
	page = int(request.args.get('page', 1))
	per_page = int(request.args.get('per_page', 20))
	#try to get users with pagination 
	users = User.query.paginate(
		page=page,
		per_page=per_page,
		error_out=False
	)
	# format data : 
	formated_data = {
		'items': [users.toDict() for users in users.items],  
		'page': users.page,
		'per_page': users.per_page,
		'total_pages': users.pages,
		'total_items': users.total,
	}
	#return jsonify({"data":{"items":[]}}),200
	return jsonify({"data":formated_data}),200
#get a user with id :
@user_api.route(Prefixer+"/<user_id>",methods=["GET"])
@cross_origin()
def get_user_data(user_id):
	try:
		targetUser = User.query.filter_by(id=user_id).first()
		if not targetUser:
			return jsonify({"message":"Not Found"}),400
		return jsonify({"data":targetUser.toDict()}),200
	except Exception as e:
		print( e )
		return jsonify({"message": "Error getting user"}),404

