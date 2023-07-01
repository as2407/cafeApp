# controller
# business logics
def sign_in(firebase_config_object, email, password):
    try:
        firebase = firebase_config_object.get_firebase()
        response = firebase.auth().sign_in_with_email_and_password(email, password)
        print("Successfully Sign In!!")
    except:
        print("Wrong ! Error !")


def sign_up(firebase_config_object, first_name, last_name, email, password):
    # print(first_name, last_name, email, password)
    try:
        firebase = firebase_config_object.get_firebase()
        response = firebase.auth().create_user_with_email_and_password(email, password)
        print("Successfully Sign up!!")
    except:
        print("Already exist")
