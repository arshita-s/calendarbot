"""
Arshita Sandhiparthi

Main
"""
import logging
import os
import slack
from flask import Flask, request, make_response, jsonify
from slackeventsapi import SlackEventAdapter
import json
import blocks
import calendar
import datetime

events = list()
cal = {}
categories = ["Default"]

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
    print(user)
    client.chat_postEphemeral(
        channel='general',
        blocks=blocks.event_buttons,
        user=user,
        text='',
    )
    return ''


# Real time events

# Handles button clicks

chan = 'general'


@app.route('/slack/actions', methods=['POST'])
def action_handler():
    global chan
    msg_action = json.loads(request.form["payload"])
    print(msg_action)
    # Make new event button press
    if msg_action.get("type") == "block_actions" and (msg_action.get("actions")[0]['action_id'] == 'event'):
        m_ts = msg_action.get('container')['message_ts']
        chan = msg_action.get("container")['channel_id']
        client.views_open(
            trigger_id=msg_action["trigger_id"],
            view=blocks.make_new_event_modal
        )
        response = jsonify({
            'response_type': 'ephemeral',
            'text': '',
            'replace_original': 'true',
            'delete_original': 'true'
        })
        return make_response(response, 200)
    # After submission of created event, save the details
    elif msg_action.get("type") == "view_submission" and msg_action.get("view")['callback_id'] == 'make-new-event':
        print(msg_action)
        events.append(msg_action.get('view')['state']['values']['set-date']['date-set']['selected_date'])
        event_name = msg_action.get('view')['state']['values']['name']['name-set']['value']
        try:
            event_description = msg_action.get('view')['state']['values']['description']['description-set']['value']
        except KeyError:
            event_description = None
        try:
            event_category = msg_action.get('view')['state']['values']['category']['event-category']['selected_option']['text']['text']
        except KeyError:
            event_category = None
        start_hour = int(msg_action.get('view')['state']['values']['start-hour']['start-hour-set']['value'])
        start_minute = int(msg_action.get('view')['state']['values']['start-minute']['start-minute-set']['value'])
        # start_ampm = msg_action.get('view')['state']['values']
        end_hour = int(msg_action.get('view')['state']['values']['end-hour']['end-hour-set']['value'])
        end_minute = int(msg_action.get('view')['state']['values']['end-minute']['end-minute-set']['value'])
        datestr = msg_action.get('view')['state']['values']['set-date']['date-set']['selected_date']
        start_date = datetime.datetime.strptime(datestr, '%Y-%m-%d').replace(hour=start_hour, minute=start_minute)
        weekday = calendar.day_name[start_date.weekday()]
        d = start_date.day
        y = start_date.year
        m = calendar.month_name[start_date.month]
        end_date = datetime.datetime.strptime(datestr, '%Y-%m-%d').replace(hour=end_hour, minute=end_minute)
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
            text=get_mention(
                user_id) + " has created an event, " + event_name + ", on " + weekday + " " + m + " " + str(
                d) + ", " + str(y) + " from " + str(start_date.hour) + ":" + str(start_date.minute) + " until " + str(
                end_date.hour) + ":" + str(end_date.minute)
        )
        print(cal)
    # Make new category button press
    elif msg_action.get("type") == "block_actions" and (msg_action.get("actions")[0]['action_id'] == 'category'):
        m_ts = msg_action.get('container')['message_ts']
        chan = msg_action.get("container")['channel_id']
        client.views_open(
            trigger_id=msg_action["trigger_id"],
            view=blocks.make_new_cat_modal
        )
        client.chat_postMessage(
            channel=chan,
            response_type='ephemeral',
            replace_original=True,
            text="Creating new category..."
        )
    # After submission of new category, save the result in 'categories'
    elif msg_action.get("type") == "view_submission" and msg_action.get("view")['callback_id'] == 'make-new-cat':
        name = msg_action.get('view')['state']['values']['name']['name-set']['value']
        categories.append(name)
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
    options = []
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

    cats = {"options": options}

    return make_response(cats, 200)


if __name__ == "__main__":
    app.run(port=8080)
