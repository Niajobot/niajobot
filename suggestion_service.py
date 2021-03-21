import firebase_admin
from firebase_admin import db

class SuggestionService():
    def __init__(self, firebase_conf_path, data_base_url):
        cred_obj = firebase_admin.credentials.Certificate(firebase_conf_path)
        default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL':data_base_url})
        
    def addSuggestion(self, streamer, author, game):
        value = {
            "game" : game
        }
        ref = db.reference("/")
        ref.child(streamer).child("suggestions").child(author).push(value)