import logging

from firebase_admin import db


class SuggestionService():

    def addSuggestion(self, streamer, author, game):
        value = {
            "game": game,
            "author": author,
            "status": "SUBMITED"
        }
        logging.info("User %s add the suggestion (%s), for the streamer %s", author, game, streamer)
        ref = db.reference("/")
        ref.child(streamer).child("suggestions").push(value)

    def getSuggestionForStreamer(self, streamer):
        def extractValue(suggestion):
            return suggestion[1]

        ref = db.reference("/")
        return list(map(extractValue, ref.child(streamer).child("suggestions") \
                        .order_by_child("status") \
                        .equal_to("SUBMITED") \
                        .get() \
                        .items()))
