import logging
logging.basicConfig(level=logging.DEBUG)
import ssl
import os
from slack import WebClient
from slack.errors import SlackApiError

slack_token = 'xoxb-1101498483268-1119164442736-5Bf1uHbCNZR7ClG82pqrIUXn'
client = WebClient(token=slack_token)

try:
  response = client.chat_postMessage(
    channel="general",
    text="Hello, this is @Calendarbot"
  )
except SlackApiError as e:
  # You will get a SlackApiError if "ok" is False
  assert e.response["error"]