"""
Arshita Sandhiparthi

Events Handling
"""

from slack import RTMClient


@RTMClient.run_on(event="message")
def msg_handler(**payload):
    data = payload['data']
    web_client = payload['web_client']


