#import user model from models 
from Package.Models.User import User
from Package.BluePrints.User.Service import UserService
#import User prefixer endpoint : 
from Package.BluePrints import User_PREFIXER, API_PREFIXER
from Package.Db import my_database
#define user bluePrint here with all the routes and the controllers : 
from flask import request, jsonify, Blueprint 
# import flask cors configuration lib : 
from flask_cors import cross_origin



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
	formated_data = UserService.getUserListPaginated(page,per_page)
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

#add route to create a new user : 
@user_api.route(Prefixer+"/",methods=["POST"])
@cross_origin()
def create_user():
	#extrct user payload from request json body : 
	userPayaload = request.json
	#validate the payload via the userService: 
	isValidPayaload = UserService.validatePayload(userPayaload)
	if not isValidPayaload:
		return jsonify({"message": "Invalid payload for user"}),400
	#check if the userName already used : 
	userAlreadyUsed = UserService.alreadyUsed(userPayaload)
	if userAlreadyUsed:
		return jsonify({"message": "User name already used "}),402
	try:
		createdUser = UserService.createUser(userPayaload)
		return jsonify({"message": "User created successfully ", "user":createdUser}),201
	except Exception as e:
		print( e )
		return jsonify({"message": "Failed to create user "}), 401