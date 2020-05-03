"""
Arshita Sandhiparthi

Main
"""
import logging
import os
import slack
import event
from flask import abort, Flask, make_response, request

SLACK_VERIFICATION_TOKEN = 'lhbdgYshgpvXAtiqQ733M55e'
SLACK_BOT_TOKEN = 'xoxb-1101498483268-1105954847428-uwiOHt0WpJ42LjEXRHnZf5bf'
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# initializing clients

slack_token = SLACK_BOT_TOKEN
client = slack.WebClient(token=slack_token)
rtm_client = slack.RTMClient(token=slack_token, connect_method='rtm.start')


# find the id of the bot

def get_mention(user):
    return '<@{user}>'.format(user=user)


# greeting message from calendarbot

botID = None
users = client.api_call("users.list").get('members')
for user in users:
    if user.get('name') == 'calendarbot':
        botID = user.get('id')
        break

response = client.chat_postMessage(channel="general", text="Hello, this is your " + get_mention(botID) + ". :calendar:")
rtm_client.start()


# Slash commands

@app.route('/event', methods=['POST'])
def event():
    info = request.form

    channelMsg = client.chat_postMessage(
        channel="#" + info["channel_name"],
        text="Would you like to create an event?"
    )
    return make_response("", 200)


def verify_slack_token(request_token):
    if SLACK_VERIFICATION_TOKEN != request_token:
        print("Error: invalid verification token!")
        print("Received {} but was expecting {}".format(request_token, SLACK_VERIFICATION_TOKEN))
        return make_response("Request contains invalid Slack verification token", 403)


if __name__ == "__main__":
    app.run()
