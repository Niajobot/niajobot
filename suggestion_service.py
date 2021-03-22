import logging

import firebase_admin
from firebase_admin import db


class SuggestionService():
    def __init__(self, firebase_conf_path, data_base_url):
        cred_obj = firebase_admin.credentials.Certificate(firebase_conf_path)
        default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': data_base_url})

    def addSuggestion(self, streamer, author, game):
        value = {
            "game": game,
            "author": author
        }
        logging.info("User %s add the suggestion (%s), for the streamer %s", author, game, streamer)
        ref = db.reference("/")
        ref.child(streamer).child("suggestions").push(value)
