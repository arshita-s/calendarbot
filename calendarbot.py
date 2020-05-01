from slack import WebClient
from slack.errors import SlackApiError
import os
from slack import logging

logging.basicConfig(level=logging.DEBUG)

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

try:
  response = client.chat_postMessage(
    channel="general",
    text="Hello."
  )
except SlackApiError as e:
  # You will get a SlackApiError if "ok" is False
  assert e.response["error"]

