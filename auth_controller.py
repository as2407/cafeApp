# controller
# business logics

from models import Person
from config import firebase_config_object, database_config_object


def test():
    person = Person("Trino", "Nandi")
    with database_config_object.get_session() as session:
        session.add(person)
        session.commit()


def sign_in(email, password):
    try:
        firebase = firebase_config_object.get_firebase()
        response = firebase.auth().sign_in_with_email_and_password(email, password)
        print("Successfully Sign In!!")
    except:
        print("Wrong ! Error !")


def sign_up(first_name, last_name, email, password):
    # print(first_name, last_name, email, password)
    try:
        firebase = firebase_config_object.get_firebase()
        response = firebase.auth().create_user_with_email_and_password(email, password)
        print("Successfully Sign up!!")
    except:
        print("Already exist")


test()
