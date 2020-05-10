"""
Here are all of the blocks, views, modals, dialogs, etc.

"""

import datetime

current_date = str(datetime.datetime.now())[:10]

make_new_event_button = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "What would you like to do?"
        }
    },
    {
        "type": "actions",
        "block_id": "msg_new_event",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Make New Event",
                    "emoji": True
                },
                "value": "new_event"
            }
        ]
    }
]

make_new_event_modal = {
    "type": "modal",
    "callback_id": "make-new-event",
    "title": {
        "type": "plain_text",
        "text": "Create a New Event"
    },
    "submit": {
        "type": "plain_text",
        "text": "Submit"
    },
    "close": {
        "type": "plain_text",
        "text": "Cancel"
    },
    "blocks": [
        {
            "type": "input",
            "block_id": "name",
            "element": {
                "type": "plain_text_input",
                "action_id": "name-set"
            },
            "label": {
                "type": "plain_text",
                "text": "Event Name"
            }
        },
        {
            "type": "input",
            "block_id": "set-date",
            "element": {
                "type": "datepicker",
                "initial_date": current_date,
                "action_id": "date-set",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select a Date",
                    "emoji": True
                }
            },
            "label": {
                "type": "plain_text",
                "text": "Set Date",
                "emoji": True
            }

        },
        {
            "type": "input",
            "block_id": "description",
            "element": {
                "type": "plain_text_input",
                "multiline": True,
                "action_id": "description-set"
            },
            "label": {
                "type": "plain_text",
                "text": "Event Description"
            },
            "optional": True
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Select a Start Time*"
            }
        },
        {
            "type": "input",
            "block_id": "start-hour",
            "element": {
                "type": "plain_text_input",
                "action_id": "start-hour-set",
                "max_length": 2
            },
            "label": {
                "type": "plain_text",
                "text": "Start Hour"
            }
        },
        {
            "type": "input",
            "block_id": "start-minute",
            "element": {
                "type": "plain_text_input",
                "action_id": "start-minute-set",
                "max_length": 2
            },
            "label": {
                "type": "plain_text",
                "text": "Start Minute"
            }
        },
        {
            "type": "section",
            "block_id": "start-am-pm",
            "text": {
                "type": "mrkdwn",
                "text": " "
            },
            "accessory": {
                "type": "radio_buttons",
                "action_id": "s-am-pm",
                "initial_option": {
                    "value": "option 1",
                    "text": {
                        "type": "plain_text",
                        "text": "AM"
                    }
                },
                "options": [
                    {
                        "value": "option 1",
                        "text": {
                            "type": "plain_text",
                            "text": "AM"
                        }
                    },
                    {
                        "value": "option 2",
                        "text": {
                            "type": "plain_text",
                            "text": "PM"
                        }
                    }
                ]
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Select an End Time*"
            }
        },
        {
            "type": "input",
            "block_id": "end-hour",
            "element": {
                "type": "plain_text_input",
                "action_id": "end-hour-set",
                "max_length": 2
            },
            "label": {
                "type": "plain_text",
                "text": "End Hour"
            }
        },
        {
            "type": "input",
            "block_id": "end-minute",
            "element": {
                "type": "plain_text_input",
                "action_id": "end-minute-set",
                "max_length": 2
            },
            "label": {
                "type": "plain_text",
                "text": "End Minute"
            }
        },
        {
            "type": "section",
            "block_id": "end-am-pm",
            "text": {
                "type": "mrkdwn",
                "text": " "
            },
            "accessory": {
                "type": "radio_buttons",
                "action_id": "e-am-pm",
                "initial_option": {
                    "value": "option 1",
                    "text": {
                        "type": "plain_text",
                        "text": "AM"
                    }
                },
                "options": [
                    {
                        "value": "option 1",
                        "text": {
                            "type": "plain_text",
                            "text": "AM"
                        }
                    },
                    {
                        "value": "option 2",
                        "text": {
                            "type": "plain_text",
                            "text": "PM"
                        }
                    }
                ]
            }
        }
    ]
}
