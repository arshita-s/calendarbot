"""
Arshita Sandhiparthi

Main
"""
import logging
import os
import slack
import event
from flask import abort, Flask, jsonify, request

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


def main():
    # slack_token = os.environ["SLACK_BOT_TOKEN"]

    slack_token = 'xoxb-1101498483268-1105954847428-uwiOHt0WpJ42LjEXRHnZf5bf'
    client = slack.WebClient(token=slack_token)
    rtm_client = slack.RTMClient(token=slack_token, connect_method='rtm.start')

    botID = None
    users = client.api_call("users.list").get('members')
    for user in users:
        if user.get('name') == 'calendarbot':
            botID = user.get('id')
            break

    response = client.chat_postMessage(channel="general", text="Hello, this is your " + get_mention(botID) + ". :calendar:")
    rtm_client.start()


def get_mention(user):
    return '<@{user}>'.format(user=user)


# Slash commands

@app.route('/event', methods=['POST'])
def event():
    if not is_request_valid(request):
        abort(400)

    return jsonify(
        response_type='in_channel',
        text="Would you like to create an event?",
    )


def is_request_valid(request):
    is_token_valid = request.form['token'] == 'lhbdgYshgpvXAtiqQ733M55e'
    is_team_id_valid = request.form['team_id'] == 'U013H4UD0MN'

    return is_token_valid and is_team_id_valid


if __name__ == "__main__":
    main()
