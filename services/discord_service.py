import requests

from firebase_admin import db


class DiscordService():

    def __init__(self, suggestion_service) -> None:
        self.suggestion_service = suggestion_service

    def formatMessage(self, streamer, suggestions):
        def extractGameStrFormat(suggestion):
            return '- {0}'.format(suggestion['game'])
        return "Voici les suggestions de jeux en cours chez {0}\n{1}".format(streamer, '\n'.join(map(extractGameStrFormat, suggestions)))

    def postMessage(self, streamer):
        refDiscord = db.reference("/").child(streamer).child("discord")
        url = refDiscord.child("url_webhook").get()
        messageId = refDiscord.child("message_id").get()

        message = self.formatMessage(streamer, self.suggestion_service.getSuggestionForStreamer(streamer))

        if url is not None:
            if messageId is None:
                messageId = requests.post(url + "?wait=true", data={'content': message}).json()['id']
                refDiscord.child("message_id").set(messageId)
            else:
                requests.patch(url + "/messages/" + messageId, data={'content': message})
