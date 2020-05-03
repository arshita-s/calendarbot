"""
Arshita Sandhiparthi

Main
"""
import logging
import os
import slack
import event
from bottle import run, post,request,response,route
from urllib import parse

SLACK_VERIFICATION_TOKEN = 'lhbdgYshgpvXAtiqQ733M55e'
SLACK_BOT_TOKEN = 'xoxb-1101498483268-1105954847428-uwiOHt0WpJ42LjEXRHnZf5bf'
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

"""
@post('/event')
def event():
    return "Would you like to create an event?"
"""
@route('/event',method="post")
def event():
    postdata = request.forms.get("text")
    output_path = str("sndwserv:/" + parse.quote(postdata))
    package = {"response_type": "in_channel", "text": "{}".format(output_path)}
    response.content_type = 'application/json'
    return package


if __name__ == "__main__":
    port_config = int(os.getenv('PORT', 5000))
    run(host='0.0.0.0', port=port_config)
