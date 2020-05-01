import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack import WebClient
from slack.errors import SlackApiError

#slack_token = os.environ["SLACK_BOT_TOKEN"]
#Random added change to test deployment

slack_token = 'xoxb-1101498483268-1119164442736-5Bf1uHbCNZR7ClG82pqrIUXn'
client = WebClient(token=slack_token)

try:
  response = client.chat_postMessage(
    channel="general",
    text="Hello, this is your @Calendarbot"
  )
except SlackApiError as e:
  assert e.response["error"]