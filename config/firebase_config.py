from decouple import config
import pyrebase


class FirebaseConfig:
    def __init__(self):
        self.firebase = None

    def get_firebase(self):
        if self.firebase is None:
            firebase_config = {
                'apiKey': config('FIREBASE_API_KEY'),
                'authDomain': config('FIREBASE_AUTH_DOMAIN'),
                'projectId': config('FIREBASE_PROJECT_ID'),
                'storageBucket': config('FIREBASE_STORAGE_BUCKET'),
                'messagingSenderId': config('FIREBASE_MESSAGING_SENDER_ID'),
                'appId': config('FIREBASE_APP_ID'),
                'measurementId': config('FIREBASE_MEASUREMENT_ID'),
                'databaseURL': config('FIREBASE_DATABASE_URL')
            }

            # initializing the app
            self.firebase = pyrebase.initialize_app(firebase_config)
            return self.firebase
        else:
            return self.firebase



# obj = FirebaseConfig()
