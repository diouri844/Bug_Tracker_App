from flask import Flask,request,jsonify
from Package import *
from flask_cors import CORS, cross_origin



my_app = Flask(__name__)
cors = CORS(my_app)
my_app.config['CORS_HEADERS'] = 'Content-Type'



@my_app.route("/get-auth",methods=["POST"])
@cross_origin()
def authentification():
    if request.method == "POST":
        data = request.form.to_dict()
        print("server authentification is loaded !! ")
        user_name = data['name']
        user_email = data['email']
        user_pswd = data['pswd']
        response = get_connexion_details(user_name,user_email,user_pswd)
        print(response)
        return jsonify({"message":response})

@my_app.route("/get-registration",methods=["POST"])
@cross_origin()
def registration():
    if request.method == "POST":
        registration_data = request.form.to_dict()
        response = check_account_registration(registration_data['FerstName'],
                                              registration_data['LastName'],
                                              registration_data['Email'],
                                              registration_data['Password'])
        if response == 1: 
            return jsonify({"message": "account already exists " })
        else:
             # creation new user document : 
            response_insert_user = create_user_document(registration_data['FerstName'],
                                              registration_data['LastName'],
                                              registration_data['Email'],
                                              registration_data['Password'])
            return jsonify({"message": response_insert_user})



if __name__=="__main__":
    my_app.secret_key = 'super secret key'
    my_app.config['SESSION_TYPE'] = 'filesystem'
    my_app.run(debug=True)