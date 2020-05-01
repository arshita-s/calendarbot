"""
Arshita Sandhiparthi

Main
"""
import logging
import os
import slack

logging.basicConfig(level=logging.DEBUG)


def main():
    # slack_token = os.environ["SLACK_BOT_TOKEN"]

    slack_token = 'xoxb-1101498483268-1105954847428-uwiOHt0WpJ42LjEXRHnZf5bf'
    client = slack.WebClient(token=slack_token)
    rtm_client = slack.RTMClient(token=slack_token, connect_method='rtm.start')
    response = client.chat_postMessage(channel="general", text="Hello, this is your @Calendarbot. :calendar:")
    rtm_client.start()


@slack.RTMClient.run_on(event="message")
def event(**payload):
    data = payload['data']
    web_client = payload['web_client']
    if "event" in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']
        web_client.chat_postMessage(channel=channel_id, thread=thread_ts, text="Would you like to create an event, <@{user}>?")

if __name__ == "__main__":
    main()
