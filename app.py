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

SLACK_VERIFICATION_TOKEN = 'lhbdgYshgpvXAtiqQ733M55e'
SLACK_BOT_TOKEN = 'xoxb-1101498483268-1105954847428-uwiOHt0WpJ42LjEXRHnZf5bf'
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
@app.route('/event', methods=['POST'])
def event_handler():
    client.chat_postMessage(
        channel='general',
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "What would you like to do?"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Make New Event",
                            "emoji": True
                        },
                        "value": "new_event"
                    }
                ]
            }
        ]
    )
    return ''


# Real time events
@app.route('/slack/actions', methods=['POST'])
def action_handler():
    msg_action = json.loads(request.form["payload"])
    actions = msg_action.get("actions")[0]
    if msg_action.get("type") == "block_actions" and 'Make New Event' in actions['text']['text']:
        client.views_open(
            trigger_id=msg_action["trigger_id"],
            view={
                "type": "modal",
                "callback_id": "modal-id",
                "title": {
                    "type": "plain_text",
                    "text": "Create a New Event"
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Submit"
                },
                "close": {
                    "type": "plain_text",
                    "text": "Cancel"
                },
                "blocks": [
                    {
                        "type": "input",
                        "element": {
                            "type": "datepicker",
                            "initial_date": "1990-4-28",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select a Date",
                                "emoji": True
                            }
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Set Date",
                            "emoji": True
                        }

                    }
                ]
            }
        )
        # client.chat_update(channel=cid, text="Creating your event...")
    return make_response("", 200)


# Prompts user when @ed
@slack_events_adapter.on('app_mention')
def ask(payload):
    event = payload.get('event', {})
    user_id = event.get("user")
    cid = event.get('channel')
    client.chat_postMessage(channel=cid, text="What can I do for you, " + get_mention(user_id) + "?")


if __name__ == "__main__":
    app.run(port=5000)
