"""
Arshita Sandhiparthi

Main
"""
import logging
import os
import slack
from flask import Flask, request, make_response
import requests
from slackeventsapi import SlackEventAdapter
import json
import blocks
import datetime
import urllib.parse as ub

cal = {}
categories = ["Default", "Miscellaneous"]
chan = ''

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

# Event command will prompt the user for a choice (of buttons) and open up the corresponding modal
@app.route('/event', methods=['POST'])
def event_handler():
    user = str(request.form.get("user_id"))
    c_id = str(request.form.get("channel_id"))
    client.chat_postEphemeral(
        channel=c_id,
        blocks=blocks.event_buttons,
        user=user,
        text='',
    )
    return make_response("", 200)


# Real time events

# Handles button clicks
@app.route('/slack/actions', methods=['POST'])
def action_handler():
    global chan
    msg_action = json.loads(request.form["payload"])

    if msg_action.get('type') == "block_actions":

        # Make new event button press, opens modal, deleted original message
        if msg_action.get("actions")[0]['action_id'] == 'event':
            chan = msg_action.get("container")['channel_id']
            client.views_open(
                trigger_id=msg_action["trigger_id"],
                view=blocks.make_new_event_modal
            )
            resp = {
                "delete_original": True
            }
            response_url = ub.unquote(msg_action.get('response_url'))
            requests.post(response_url, headers={"content-type": "application/json"}, data=json.dumps(resp))

        # Make new category button press, opens modal, deletes original message
        elif msg_action.get("actions")[0]['action_id'] == 'category':
            chan = msg_action.get("container")['channel_id']
            client.views_open(
                trigger_id=msg_action["trigger_id"],
                view=blocks.make_new_cat_modal
            )
            resp = {
                "delete_original": True
            }
            response_url = ub.unquote(msg_action.get('response_url'))
            requests.post(response_url, headers={"content-type": "application/json"}, data=json.dumps(resp))

        # Edit event button press, opens modal, deletes original message
        elif msg_action.get("actions")[0]['action_id'] == 'edit':
            chan = msg_action.get("container")['channel_id']
            client.views_open(
                trigger_id=msg_action["trigger_id"],
                view=blocks.edit_event_modal
            )
            resp = {
                "delete_original": True
            }
            response_url = ub.unquote(msg_action.get('response_url'))
            requests.post(response_url, headers={"content-type": "application/json"}, data=json.dumps(resp))
    elif msg_action.get("type") == "view_submission":

        # After submission of created event, save the details
        if msg_action.get("view")['callback_id'] == 'make-new-event':
            values = msg_action.get('view')['state']['values']
            event_name = values['name']['name-set']['value']

            try:
                event_description = values['description']['description-set']['value']
            except KeyError:
                event_description = None
            try:
                event_category = values['category']['event-category']['selected_option']['text']['text']
            except KeyError:
                event_category = None

            start_hour = int(values['start-hour']['start-hour-set']['value'])
            start_minute = int(values['start-minute']['start-minute-set']['value'])
            end_hour = int(values['end-hour']['end-hour-set']['value'])
            end_minute = int(values['end-minute']['end-minute-set']['value'])
            startdatestr = values['set-date-start']['start-date-set']['selected_date']
            enddatestr = values['set-date-end']['end-date-set']['selected_date']
            start_date = datetime.datetime.strptime(startdatestr, '%Y-%m-%d').replace(hour=start_hour, minute=start_minute)
            end_date = datetime.datetime.strptime(enddatestr, '%Y-%m-%d').replace(hour=end_hour, minute=end_minute)
            user_id = msg_action.get('user')['id']

            if event_description and event_category:
                cal[(event_name, start_date)] = (user_id, start_date, end_date, event_description, event_category)
            elif event_category:
                cal[(event_name, start_date)] = (user_id, start_date, end_date, None, event_category)
            elif event_description:
                cal[(event_name, start_date)] = (user_id, start_date, end_date, event_description, None)
            else:
                cal[(event_name, start_date)] = (user_id, start_date, end_date, None, None)

            client.chat_postMessage(
                channel='general',
                text=get_mention(user_id)
                     + "Has created an event, "
                     + event_name
                     + start_date.strftime(", happening from %A %B %-d, %Y at %-I:%M to ")
                     + end_date.strftime("%A %B %-d, %Y at %-I:%M")
            )

        # After submission of new category, save the result in 'categories'
        elif msg_action.get("view")['callback_id'] == 'make-new-cat':
            name = msg_action.get('view')['state']['values']['name']['name-set']['value']
            categories.append(name)
        elif msg_action.get("view")['callback_id'] == 'edit-a-event':
            print(msg_action)
            """
            client.views_push(
                trigger_id=msg_action.get("trigger_id"),
                view=blocks.edit_ask
            )
            """
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
def populate():
    pay = json.loads(request.form["payload"])
    action = pay.get("action_id")
    options = []

    if action == 'event-category':
        for i in range(len(categories)):
            if i == len(categories)-1:
                options.append({
                    "text": {
                        "type": "plain_text",
                        "text": categories[i]
                    },
                    "value": "value-" + str(i)
                })
                break
            options.append({
              "text": {
                "type": "plain_text",
                "text": categories[i]
              },
              "value": "value-" + str(i)
            },)

    elif action == 'event-edit':
        keys = list(cal)
        for i in range(len(keys)):
            event = keys[i]

            start_date = cal[event][1]
            end_date = cal[event][2]
            name = event[0]

            if i == len(cal)-1:
                options.append({
                    "text": {
                        "type": "plain_text",
                        "text": name + "; " + start_date.strftime("%A %B %-d %Y %-I:%M - ")
                                + end_date.strftime("%A %B %-d %Y %-I:%M")
                    },
                    "value": "value-" + name
                })
                break
            options.append({
                "text": {
                    "type": "plain_text",
                    "text": name + "; " + start_date.strftime("%A %B %-d %Y %-I:%M - ")
                            + end_date.strftime("%A %B %-d %Y %-I:%M")
                },
                "value": "value-" + name
            },)

    resp = {"options": options}
    return make_response(resp, 200)


if __name__ == "__main__":
    app.run(port=8080)
