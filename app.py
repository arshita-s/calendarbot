"""
Arshita Sandhiparthi

Main
"""
import logging
import os
import slack
from flask import Flask, request, make_response
from slackeventsapi import SlackEventAdapter
import json
import blocks
import calendar
import datetime

events = list()

SLACK_BOT_TOKEN = 'xoxb-1101498483268-1105954847428-uwiOHt0WpJ42LjEXRHnZf5bf'
SLACK_VERIFY = 'lhbdgYshgpvXAtiqQ733M55e'
SLACK_SIGNING_SECRET = '6ee8492929d135bf1ba948350114e6f4'
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

# initializing clients

slack_token = SLACK_BOT_TOKEN
client = slack.WebClient(token=slack_token)
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events", app)


# find the id of the bot

def get_mention(user):
    return '<@{user}>'.format(user=user)


# greeting message from calendarbot
@slack_events_adapter.on('team_join')
def greeting():
    botID = 'U0133U2QXCL'
    client.chat_postMessage(channel="general",
                            text="Hello, this is your " + get_mention(botID) + ". :calendar:")


# Slash commands

# Event command will prompt the user for a choice and open up the corresponding modal
@app.route('/event', methods=['POST'])
def event_handler():
    user = str(request.form.get("user_id"))
    client.chat_postEphemeral(
        channel='general',
        blocks=blocks.make_new_event_button,
        user=user,
        text='',
    )
    return ''


# Real time events

# Handles button clicks
chan = 'general'


@app.route('/slack/actions', methods=['POST'])
def action_handler():
    msg_action = json.loads(request.form["payload"])

    # make new event
    if msg_action.get("type") == "block_actions" and (msg_action.get("actions")[0]['block_id'] == 'msg_new_event'):
        global chan
        chan = msg_action.get("channel")
        client.views_open(
            trigger_id=msg_action["trigger_id"],
            view=blocks.make_new_event_modal
        )
    elif msg_action.get("type") == "view_submission" and msg_action.get("view")['callback_id'] == 'make-new-event':
        print(msg_action)
        events.append(msg_action.get('view')['state']['values']['set-date']['date-set']['selected_date'])
        event_name = msg_action.get('view')['state']['values']['name']['name-set']['value']
        datestr = msg_action.get('view')['state']['values']['set-date']['date-set']['selected_date']
        date = datetime.datetime.strptime(datestr, '%Y-%m-%d')
        weekday = calendar.day_name[date.weekday()]
        d = date.day
        y = date.year
        m = calendar.month_name[date.month]
        user_id = msg_action.get('user')['id']
        client.chat_postMessage(
            channel='general',
            text=get_mention(user_id) + " has created an event, " + event_name + ", happening on " + weekday + " " + m + " " + str(d) + ", " + str(y) + "."
        )

    return make_response("", 200)


# Prompts user when @ed
@slack_events_adapter.on('app_mention')
def ask(payload):
    event = payload.get('event', {})
    user_id = event.get("user")
    cid = event.get('channel')
    client.chat_postMessage(channel=cid, text="What can I do for you, " + get_mention(user_id) + "?")


# When a user wants to create a new event, sends a request to populate categories menu
@app.route('/options-load-endpoint', methods=['POST'])
def populate_categories():
    return make_response({
        "options": [
        {
          "text": {
            "type": "plain_text",
            "text": "*this is plain_text text*"
          },
          "value": "value-0"
        },
        {
          "text": {
            "type": "plain_text",
            "text": "*this is plain_text text*"
          },
          "value": "value-1"
        },
        {
          "text": {
            "type": "plain_text",
            "text": "*this is plain_text text*"
          },
          "value": "value-2"
        }
        ]}, 200)


if __name__ == "__main__":
    app.run(port=8080)

