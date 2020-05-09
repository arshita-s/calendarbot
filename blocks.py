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
            "type": "section",
            "block_id": "start-hour",
            "text": {
                "type": "mrkdwn",
                "text": "Pick an Hour"
            },
            "accessory": {
                "type": "static_select",
                "action_id": "hour-start",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Hour",
                    "emoji": True
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "1",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "2",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "3",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "4",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "5",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "6",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "7",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "8",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "9",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "10",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "11",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "12",
                            "emoji": True
                        },
                        "value": "value-2"
                    }
                ]
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Pick a Minute"
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Minute",
                    "emoji": True
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "0",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "1",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "2",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "3",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "4",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "5",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "6",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "7",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "8",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "9",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "10",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "11",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "12",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "13",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "14",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "15",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "16",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "17",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "18",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "19",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "20",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "21",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "22",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "23",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "24",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "25",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "26",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "27",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "28",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "29",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "30",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "31",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "32",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "33",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "34",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "35",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "36",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "37",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "38",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "39",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "40",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "41",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "42",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "43",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "44",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "45",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "46",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "47",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "48",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "49",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "50",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "51",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "52",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "53",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "54",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "55",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "56",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "57",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "58",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "59",
                            "emoji": True
                        },
                        "value": "value-1"
                    }
                ]
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
                    "text": {
                        "type": "plain_text",
                        "text": "AM"
                    },
                    "value": "option 1",
                    "description": {
                        "type": "plain_text",
                        "text": "ante merideim"
                    }
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "AM"
                        },
                        "value": "option 1",
                        "description": {
                            "type": "plain_text",
                            "text": "ante merideim"
                        }
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PM"
                        },
                        "value": "option 2",
                        "description": {
                            "type": "plain_text",
                            "text": "post merideim"
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
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Pick an Hour"
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Hour",
                    "emoji": True
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "1",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "2",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "3",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "4",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "5",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "6",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "7",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "8",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "9",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "10",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "11",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "12",
                            "emoji": True
                        },
                        "value": "value-2"
                    }
                ]
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Pick a Minute"
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Minute",
                    "emoji": True
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "0",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "1",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "2",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "3",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "4",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "5",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "6",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "7",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "8",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "9",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "10",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "11",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "12",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "13",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "14",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "15",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "16",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "17",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "18",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "19",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "20",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "21",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "22",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "23",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "24",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "25",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "26",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "27",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "28",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "29",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "30",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "31",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "32",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "33",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "34",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "35",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "36",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "37",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "38",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "39",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "40",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "41",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "42",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "43",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "44",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "45",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "46",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "47",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "48",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "49",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "50",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "51",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "52",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "53",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "54",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "55",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "56",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "57",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "58",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "59",
                            "emoji": True
                        },
                        "value": "value-1"
                    }
                ]
            }
        },
        {
            "type": "section",
            "block_id":"end-am-pm",
            "text": {
                "type": "mrkdwn",
                "text": " "
            },
            "accessory": {
                "type": "radio_buttons",
                "action_id":"e-am-pm",
                "initial_option": {
                    "text": {
                        "type": "plain_text",
                        "text": "AM"
                    },
                    "value": "option 1",
                    "description": {
                        "type": "plain_text",
                        "text": "ante merideim"
                    }
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "AM"
                        },
                        "value": "option 1",
                        "description": {
                            "type": "plain_text",
                            "text": "ante merideim"
                        }
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PM"
                        },
                        "value": "option 2",
                        "description": {
                            "type": "plain_text",
                            "text": "post merideim"
                        }
                    }
                ]
            }
        }
    ]
}
