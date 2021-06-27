import firebase_admin


class FirebaseConfiguration():
    def __init__(self, firebase_conf_path, data_base_url):
        cred_obj = firebase_admin.credentials.Certificate(firebase_conf_path)
        default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': data_base_url})