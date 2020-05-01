"""
Arshita Sandhiparthi

Main
"""

import logging
import os
from slack import WebClient
import event

logging.basicConfig(level=logging.DEBUG)


def main():
    # slack_token = os.environ["SLACK_BOT_TOKEN"]

    slack_token = 'xoxb-1101498483268-1119164442736-5Bf1uHbCNZR7ClG82pqrIUXn'
    client = WebClient(token=slack_token)

    response = client.chat_postMessage(channel="general", text="Hello, this is your @Calendarbot. :calendar:")


if __name__ == "__main__":
    main()
