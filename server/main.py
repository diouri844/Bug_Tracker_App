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
        user_name = data['name']
        user_email = data['email']
        user_pswd = data['pswd']
        connexion_state = 0
        response = get_connexion_details(user_name,user_email,user_pswd)
        if response == "welcom back again  "+str(user_name):
            connexion_state = 1
        return jsonify({"message":response,"statelogin":connexion_state})

@my_app.route("/get-registration",methods=["POST"])
@cross_origin()
def registration():
    if request.method == "POST":
        registration_data = request.form.to_dict()
        registration_state = 0
        response = check_account_registration(
            registration_data['FerstName'],
            registration_data['LastName'],
            registration_data['Email'],
            registration_data['Password']
            )
        if response == 1: 
            return jsonify({"message": "account already exists ",'RegistrationState':registration_state })
        else:
             # creation new user document :
            registration_state = 1 
            response_insert_user = create_user_document(registration_data['FerstName'],
                                              registration_data['LastName'],
                                              registration_data['Email'],
                                              registration_data['Password'])
            return jsonify({"message": response_insert_user,'RegistrationState':registration_state})


@my_app.route("/add/<subject>",methods=["POST"])
@cross_origin()
def add_data(subject):
    list_subject_dispo = ['Project','Team','Invitation']
    message_response = ""
    state = ""
    if request.method=='POST':
        if subject in list_subject_dispo:
            if subject == 'Invitation':
                current_invitation = request.form.to_dict()
                reponse_invitation_sender = send_invitation(current_invitation)
                if reponse_invitation_sender < 0:
                    message_response = "We can't send out the invitation to "+str(current_invitation['To'])+" try again."
                    state = "error"
                else:
                    message_response = "The user "+str(current_invitation['To'])+" has been successfully logged in."
                    state = "success"
            if subject == 'Project':
                response_project_creator = create_project(request.form.to_dict())
                if response_project_creator < 0:
                    message_response = "We cannot create a project at this time, please try again."
                    state = "error"
                else:
                    message_response = "Project created successfully"
                    state = "success"
            if subject == 'Team':
                response_team_creator = create_team(request.form.to_dict())
                if response_team_creator < 0:
                    message_response = "We can't get your team together right now, please try again."
                    state = "error"
                else:
                    message_response = "Your team has been successful."
                    state = "success"
    return jsonify({"message": message_response,'CreateState':state})

@my_app.route("/add/Team/Project",methods=["POST"])
@cross_origin()
def add_project_to_team():
    if request.method == "POST":
        message_response = ""
        data = request.form.to_dict()
        team_name = data['Team']
        project_name = data['Project']
        project_state = data['State']
        # it shuld send invitation for each team membre :
        response_insert = add_project_team(team_name,project_name,project_state)
        if response_insert < 0:
            message_response =  "We can not add selected project to the team target "
        else:
            message_response = " add project to team project list done :) ......"
        return jsonify({"message": message_response})

@my_app.route("/update/<subject>", methods=["POST"])
@cross_origin()
def update_subject_custom(subject):
    if request.method == 'POST':
        subject_dispo = ['Team']
        response_message = ""
        response_state = ""
        if subject in subject_dispo:
            if subject == subject_dispo[0]:
                # update team : new team to old project :
                print("update team : new team to old project")
                new_data = request.form.to_dict()
                print(new_data)
                # update the form of invitation:
                invitation = {}
                invitation['from'] = new_data['ProjectOwner']
                invitation['To'] = new_data['TeamManager']
                invitation['Type'] = 'Project'
                invitation['Target'] = new_data['Project']
                invitation['Subject'] = 'I want you to give us a hand with '+str(new_data['Project'])
                invitation['TeamName'] = new_data['Team']
                invitation['State'] = 'Sended'
                response_custom_invit = send_invitation(invitation)
                # when i update state of the costum initation all is done great but the project state in 
                # the team target project state is null " " that is an error to fixe 
                # some time the project collection , team name attribute don't get the value of the new 
                # team added to project , and the value stay " Not-found " as the ferst use case this is another 
                # error to fixe it later ........ , djaaana :)
                 
                if response_custom_invit < 0:
                    response_message = "We can't send out the invitation to "+str(invitation['To'])+" try again."
                    response_state = "error"
                else:
                    response_message = "The user "+str(invitation['To'])+" has been successfully logged in."
                    response_state = "success"
        return jsonify({"message":response_message,"state":response_state})


@my_app.route("/update/Invitation/<state>", methods=["POST","DELETE"])
@cross_origin()
def update_invitation(state):
    if request.method == 'POST':
        state_dispo = ['Accept','Refuse']
        if state in state_dispo:
            target_invitation = request.form.to_dict()
            # update state of notification :
            update_invit_state = update_invit(target_invitation, state)
            # check return state :
            if update_invit_state == 1:
                response_message = "Invitation status updated successfully."
                response_state="succses"
                if state ==  'Accept':
                    # check if target is an team :
                    if target_invitation['Type'] == 'Team':
                        reponse_user = target_invitation['To']+" accept your invitation" 
                        # add user target to team contributors list :
                        reponse_push_user = add_user_to_team(target_invitation['To'],target_invitation['Target'])
                        if reponse_push_user == 1:
                            #create new custom invitation :
                            push_invitation = {
                                'from':target_invitation['Target'],
                                'To':target_invitation['From'],
                                'Type':target_invitation['Type'],
                                'Target':target_invitation['Target'],
                                'Subject':target_invitation['To']+" join "+target_invitation['Target'],
                                'State':state        
                            }
                            push_reponse_invit = send_invitation(push_invitation)
                    # check if target if  project : 
                    if target_invitation['Type'] ==  'Project':
                        reponse_user = target_invitation['To']+" accept your invitation"
                        # add project name to user project liste :
                        # target_invitation['Target'] => project name 
                        project_data = get_project_Id(target_invitation['Target'])
                        owner_project = project_data[0]['Owner']
                        # use owner to add project name to list : 
                        response_push_project_to_user = add_user_project(owner_project,target_invitation['Target'])
                        # add user target to team contributors list : 
                        list_contrib = get_contributors(target_invitation['TeamName'])
                        if len(list_contrib)!=0:
                            response_push_contributors = add_contribs_to_project(target_invitation['Target'],list_contrib)
                            if response_push_contributors == 1:
                                # add contributors list successfully :
                                #create new custom invitation :
                                # to update later :
                                for user in list_contrib:
                                    push_invitation = {
                                        'from':target_invitation['Target'],
                                        'To':target_invitation['From'],
                                        'Type':target_invitation['Type'],
                                        'Target':target_invitation['Target'],
                                        'Subject':user+" join "+target_invitation['Target'],
                                        'State':''        
                                    }
                                    #invitation state error to be fixed 
                                    push_reponse_invit = send_invitation(push_invitation)
                                # add project name to team project list target is the project name :
                                response_add_project_team = add_project_team(target_invitation['TeamName'],
                                                                            target_invitation['Target'],'')
                else:
                    # invitation not ignored : 
                    if target_invitation['Type'] ==  'Team':
                        # remove team name from project team:
                        response_remove_project= remove_project(target_invitation['Target'])
                        print(response_remove_project)
                        # for ignoring invitation team join is done
                    if target_invitation['Type'] ==  'Project':
                        reponse_user = target_invitation['To']+" has a different commitment in the present time."
                        # the current team taregt ignore invitation => project without team 
                        # delete the name of team form the project attributs:
                        response_remove_project_team_name = remove_team_from_project(target_invitation['Target'])
                        print(response_remove_project_team_name)
                        # solution 1 : delete project 
                        # solution 2: ask for new team 
                        print(" to be continu ........")
                # create formdata response:
                reponse_to_current_invitation = {
                    'from':target_invitation['To'],
                    'To':target_invitation['From'],
                    'Type':target_invitation['Type'],
                    'Target':target_invitation['Target'],
                    'Subject':reponse_user,
                    'State':state
                }
                #add this invitation : 
                add_reponse_invit = send_invitation(reponse_to_current_invitation)
                #delet current invitation:
                delet_invitation(target_invitation)
            else:
                response_message = "Error updating the status on the invitation."
                response_state = "error"
            #generate new Notification to display response to the sender user :
        return jsonify({"message":response_message,"state":response_state})
    if request.method == "DELETE":
        # clear all notifications :
        drup_all_invitation(state)
        return jsonify({"message":"all done "})


@my_app.route("/get-all-project/<subject>/<key>",methods=["GET"])
@cross_origin()
def fetch_data_endpoint(subject,key):
    subject_list_enable = ['Id','User','Team','Invitation']
    message_response = ""
    if subject in subject_list_enable:
        # get connexion wit the dba :
        if subject == 'Id':
            project_list = get_project_Id(key)
            print(project_list)
        if subject == 'User':
            project_list = get_project_user(key)
            print(project_list)
        if subject == 'Team':
            project_list = get_project_team(key)
            print(project_list)
        if subject == 'Invitation':
            result = get_invitation_user(key)
            if result != -1:
                project_list = result
            else:
                project_list = []
        message_response = "fetch data from dba : get "+str(subject)+" with key :  "+str(key)
    else:
        message_response = "fetch data from dba : get subject not enable yet "
    return jsonify({"message": message_response,"reponse_data":project_list})

@my_app.route("/check/user/<key>",methods=["GET"])
@cross_origin()
def check_user_data(key):
    response_message = ""
    check_response = get_user_data(key)
    if check_response == 1:
        response_message = "accounrt exist "
    else:
        response_message = "we can not find user :( "
    return jsonify({"message":response_message,"state":check_response})

@my_app.route("/delete/<subject>",methods=["POST"])
@cross_origin()
def delete(subject):
    response_message = ""
    check_response = 0
    state_response = ""
    subject_dispo = ["Project"]
    if subject in subject_dispo:
        if subject == subject_dispo[0]:
            # delete the project with id = key.Name:
            project_to_delete = request.form.to_dict()
            check_response = remove_project(project_to_delete['Name'])
            #update response_message:
            if check_response == 1:
                response_message = "your project has been successfully removed."
                state_response = "succses"
            else:
                response_message = "your project is not deleted at the moment, please try again later."
                state_response = "error"
    return jsonify({"message":response_message,"state":state_response})



@my_app.route("/",methods=["GET"])
@cross_origin()
def ping():
    return jsonify({"message":"Api pong"})


if __name__=="__main__":
    my_app.secret_key = 'super secret key'
    my_app.config['SESSION_TYPE'] = 'filesystem'
    print("Bug tracker runing on : http://localhost:5000" )
    my_app.run(debug=True)