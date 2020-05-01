"""
Arshita Sandhiparthi

Events Handling
"""

from slack import RTMClient

@RTMClient.run_on(event="message")
def event(**payload):
    data = payload['data']
    web_client = payload['web_client']
    if "/cal" in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']
        web_client.chat_postMessage(channel=channel_id, thread=thread_ts, text="Would you like to create an event, <@{user}>?")
    slack_token = 'xoxb-1101498483268-1119164442736-5Bf1uHbCNZR7ClG82pqrIUXn'
    rtm_client = RTMClient(token=slack_token)
    rtm_client.start()