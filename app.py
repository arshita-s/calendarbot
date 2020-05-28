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
counter = 0
selected_event = int()

SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_VERIFY = os.environ.get('SLACK_VERIFY')
SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')
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
    bot_id = 'U0133U2QXCL'
    client.chat_postMessage(channel="general",
                            text="Hello, this is your " + get_mention(bot_id) + ". :calendar:")


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
    global chan, selected_event, counter

    not_12 = {'AM': 0, 'PM': 12}
    yes_12 = {'AM': -12, 'PM': 0}
    msg_action = json.loads(request.form["payload"])

    # Button press
    if msg_action.get('type') == "block_actions":

        # Make new event button press, opens modal
        if msg_action.get("actions")[0]['action_id'] == 'event':
            chan = msg_action.get("container")['channel_id']
            t_id = msg_action["trigger_id"]
            client.views_open(
                trigger_id=t_id,
                view=blocks.make_new_event_modal
            )
            # Deletes original message
            resp = {
                "delete_original": True
            }
            response_url = ub.unquote(msg_action.get('response_url'))
            requests.post(response_url, headers={"content-type": "application/json"}, data=json.dumps(resp))

        # Make new category button press, opens modal
        elif msg_action.get("actions")[0]['action_id'] == 'category':
            chan = msg_action.get("container")['channel_id']
            t_id = msg_action["trigger_id"]
            client.views_open(
                trigger_id=t_id,
                view=blocks.make_new_cat_modal
            )
            # Deletes original message
            resp = {
                "delete_original": True
            }
            response_url = ub.unquote(msg_action.get('response_url'))
            requests.post(response_url, headers={"content-type": "application/json"}, data=json.dumps(resp))

        # Edit event button press, opens modal
        elif msg_action.get("actions")[0]['action_id'] == 'edit':
            chan = msg_action.get("container")['channel_id']
            t_id = msg_action["trigger_id"]
            client.views_open(
                trigger_id=t_id,
                view=blocks.edit_event_modal
            )
            # Deletes original message
            resp = {
                "delete_original": True
            }
            response_url = ub.unquote(msg_action.get('response_url'))
            requests.post(response_url, headers={"content-type": "application/json"}, data=json.dumps(resp))

        elif msg_action.get('actions')[0]['action_id'] == 'remind':
            chan = msg_action.get("container")['channel_id']
            t_id = msg_action["trigger_id"]
            client.views_open(
                trigger_id=t_id,
                view=blocks.reminder_modal
            )
            resp = {
                "delete_original": True
            }
            response_url = ub.unquote(msg_action.get('response_url'))
            requests.post(response_url, headers={"content-type": "application/json"}, data=json.dumps(resp))

    # Modal submission
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
            try:
                start_hour = int(values['start-hour']['start-hour-set']['value'])
            except ValueError:
                response = {
                    "response_action": "errors",
                    "errors": {
                        "start-hour": "Invalid value"
                    }
                }
                return response
            if start_hour not in range(1, 13):
                response = {
                    "response_action": "errors",
                    "errors": {
                        "start-hour": "Invalid value"
                    }
                }
                return response
            try:
                start_minute = int(values['start-minute']['start-minute-set']['value'])
            except ValueError:
                response = {
                    "response_action": "errors",
                    "errors": {
                        "start-minute": "Invalid value"
                    }
                }
                return response
            if start_minute not in range(0, 60):
                response = {
                    "response_action": "errors",
                    "errors": {
                        "start-minute": "Invalid value"
                    }
                }
                return response
            try:
                end_hour = int(values['end-hour']['end-hour-set']['value'])
            except ValueError:
                response = {
                    "response_action": "errors",
                    "errors": {
                        "end-hour": "Invalid value"
                    }
                }
                return response
            if end_hour not in range(1, 13):
                response = {
                    "response_action": "errors",
                    "errors": {
                        "end-hour": "Invalid value"
                    }
                }
                return response
            try:
                end_minute = int(values['end-minute']['end-minute-set']['value'])
            except ValueError:
                response = {
                    "response_action": "errors",
                    "errors": {
                        "end-minute": "Invalid value"
                    }
                }
                return response
            if end_minute not in range(0, 60):
                response = {
                    "response_action": "errors",
                    "errors": {
                        "end-minute": "Invalid value"
                    }
                }
                return response
            startdatestr = values['set-date-start']['start-date-set']['selected_date']
            enddatestr = values['set-date-end']['end-date-set']['selected_date']
            start_am_pm = values['start-am-pm']['start-am-pm-set']['selected_option']['value']
            end_am_pm = values['end-am-pm']['end-am-pm-set']['selected_option']['value']
            start_date = datetime.datetime.strptime(startdatestr, '%Y-%m-%d')
            end_date = datetime.datetime.strptime(enddatestr, '%Y-%m-%d')
            if start_hour == 12:
                start_hour += yes_12[start_am_pm]
            else:
                start_hour += not_12[start_am_pm]
            if end_hour == 12:
                end_hour += yes_12[end_am_pm]
            else:
                end_hour += not_12[end_am_pm]
            start_date = start_date.replace(hour=start_hour, minute=start_minute)
            end_date = end_date.replace(hour=end_hour, minute=end_minute)
            day_difference = end_date - start_date
            print(day_difference)
            if day_difference.days < 0:
                response = {
                    "response_action": "errors",
                    "errors": {
                        "set-date-end": "The event must end after it starts."
                    }
                }
                return response
            user_id = msg_action.get('user')['id']
            if event_description and event_category:
                cal[counter] = (user_id, event_name, start_date, end_date, event_description, event_category)
            elif event_category:
                cal[counter] = (user_id, event_name, start_date, end_date, None, event_category)
            elif event_description:
                cal[counter] = (user_id, event_name, start_date, end_date, event_description, None)
            else:
                cal[counter] = (user_id, event_name, start_date, end_date, None, None)
            counter += 1

            client.chat_postMessage(
                channel='general',
                text=get_mention(user_id)
                     + " has created an event, "
                     + event_name
                     + start_date.strftime(", from %A %B %-d, %Y at %-I:%M %p to ")
                     + end_date.strftime("%A %B %-d, %Y at %-I:%M %p.")
            )
            print(cal)

        # After submission of new category, save the result in 'categories'
        elif msg_action.get("view")['callback_id'] == 'make-new-cat':
            name = msg_action.get('view')['state']['values']['name']['name-set']['value']
            categories.append(name)

        # When user submits event to edit, push a new view asking what to edit in that event
        elif msg_action.get("view")['callback_id'] == 'edit-an-event':
            key = msg_action.get('view')['state']['values']['edit']['event-edit']['selected_option']['value']
            print(msg_action)
            selected_event = int(key)
            print(selected_event)
            # Push new view to modal
            resp = {
                "response_action": "push",
                "view": blocks.edit_ask
            }
            return resp

        # Pushes modal based on what the user wants to edit
        elif msg_action.get("view")['callback_id'] == 'edit-prompt':
            values = msg_action.get("view")['state']['values']
            resp = {}
            to_edit = values['prompt-edit']['prompt']['selected_option']['text']['text']

            if to_edit == 'Event Name':
                resp = {
                    "response_action": "push",
                    "view": blocks.event_name
                }
            elif to_edit == 'Start Time':
                resp = {
                    "response_action": "push",
                    "view": blocks.start_time
                }
            elif to_edit == 'End Time':
                resp = {
                    "response_action": "push",
                    "view": blocks.end_time
                }
            elif to_edit == "Start Date":
                resp = {
                    "response_action": "push",
                    "view": blocks.edit_ask
                }
            elif to_edit == "End Date":
                resp = {
                    "response_action": "push",
                    "view": blocks.edit_ask
                }
            elif to_edit == "Category":
                resp = {
                    "response_action": "push",
                    "view": blocks.edit_ask
                }
            elif to_edit == "Description":
                resp = {
                    "response_action": "push",
                    "view": blocks.edit_ask
                }

            return resp

        # Changes the name based on what the user has entered
        elif msg_action.get('view')['callback_id'] == 'edit-name':
            print(msg_action)
            event = cal.get(selected_event)

            if event is None:
                return

            n_user = msg_action['user']['id']  # user id of the person who changed the event

            # all else stays the same except for the new event name

            user_id = event[0]
            orig = event[1]
            name = msg_action['view']['state']['values']['name']['name-set']['value']
            start_date = event[2]
            end_date = event[3]
            event_description = event[4]
            event_category = event[5]

            if 'selected_option' in msg_action['view']['state']['values']['notify']['notify-chan']:
                notify = 0
            else:
                notify = None

            if notify is not None:
                cal[selected_event] = (user_id, name, start_date, end_date, event_description, event_category)
                client.chat_postMessage(
                    channel=chan,
                    text=get_mention(n_user)
                         + " has changed the name of event, " + orig + ", to "
                         + name
                         + start_date.strftime(". It occurs from %A %B %-d, %Y at %-I:%M %p to ")
                         + end_date.strftime("%A %B %-d, %Y at %-I:%M %p.")
                )

        elif msg_action.get('view')['callback_id'] == 'reminder':
            print(msg_action.get('view')['state']['values'])
            key = msg_action.get('view')['state']['values']['edit']['event-reminder']['selected_option']['value']
            selected_event = int(key)
            resp = {
                "response_action": "push",
                "view": blocks.set_reminder_modal
            }
            return resp

    return make_response("", 200)


# Prompts user when @ed
@slack_events_adapter.on('app_mention')
def ask(payload):
    event = payload.get('event', {})
    user_id = event.get("user")
    cid = event.get('channel')
    client.chat_postMessage(channel=cid, text="What can I do for you, " + get_mention(user_id) + "?")


# External source to populate select menus and such based on prior user activity
@app.route('/options-load-endpoint', methods=['POST'])
def populate():
    pay = json.loads(request.form["payload"])
    action = pay.get("action_id")
    options = []

    # Populate categories
    if action == 'event-category':
        for i in range(len(categories)):
            if i == len(categories) - 1:
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
            }, )

    # Populate events to edit
    elif action == 'event-edit':
        keys = list(cal)
        for i in range(len(keys)):
            event = keys[i]

            name = cal[event][1]
            start_date = cal[event][2]
            end_date = cal[event][3]

            if i == len(cal) - 1:
                options.append({
                    "text": {
                        "type": "plain_text",
                        "text": name + "; " + start_date.strftime("%A %B %-d %Y %-I:%M - ")
                                + end_date.strftime("%A %B %-d %Y %-I:%M")
                    },
                    "value": str(keys[i])
                })
                break
            options.append({
                "text": {
                    "type": "plain_text",
                    "text": name + "; " + start_date.strftime("%A %B %-d %Y %-I:%M - ")
                            + end_date.strftime("%A %B %-d %Y %-I:%M")
                },
                "value": str(keys[i])
            }, )

    elif action == 'event-reminder':
        keys = list(cal)
        for i in range(len(keys)):
            event = keys[i]

            if i == len(cal) - 1:
                options.append({
                    "text": {
                        "type": "plain_text",
                        "text": cal[event][1]
                    },
                    "value": str(keys[i])
                })
                break
            options.append({
                "text": {
                    "type": "plain_text",
                    "text": cal[event][1]
                },
                "value": str(keys[i])
            }, )

    # Respond with list of options
    resp = {"options": options}
    return make_response(resp, 200)


if __name__ == "__main__":
    app.run(port=8080)
