"""
Here are all of the blocks, views, modals, dialogs, etc.

"""

import datetime

current_date = str(datetime.datetime.now())[:10]

event_buttons = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "What would you like to do?"
        }
    },
    {
        "type": "actions",
        "block_id": "msg_new_buttons",
        "elements": [
            {
                "type": "button",
                "action_id": "event",
                "text": {
                    "type": "plain_text",
                    "text": "Make New Event",
                    "emoji": True
                },
                "value": "new_event"
            },
            {
                "type": "button",
                "action_id": "category",
                "text": {
                    "type": "plain_text",
                    "text": "Make New Category",
                    "emoji": True
                },
                "value": "new_category"
            },
            {
                "type": "button",
                "action_id": "edit",
                "text": {
                    "type": "plain_text",
                    "text": "Edit Event",
                    "emoji": True
                },
                "value": "edit_event"
            }
        ]
    }
]

edit_event_modal = {
    "type": "modal",
    "callback_id": "edit-an-event",
    "title": {
        "type": "plain_text",
        "text": "Edit an Event",
        "emoji": True
    },
    "submit": {
        "type": "plain_text",
        "text": "Submit",
        "emoji": True
    },
    "close": {
        "type": "plain_text",
        "text": "Cancel",
        "emoji": True
    },
    "blocks": [
        {
            "type": "input",
            "block_id": "edit",
            "element": {
                "type": "external_select",
                "action_id": "event-edit",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select an Event to Edit",
                    "emoji": True
                },
                "min_query_length": 0
            },
            "label": {
                "type": "plain_text",
                "text": "Event",
                "emoji": True
            },
            "optional": False
        }
    ]
}

make_new_cat_modal = {
    "type": "modal",
    "callback_id": "make-new-cat",
    "title": {
        "type": "plain_text",
        "text": "Create New Category",
        "emoji": True
    },
    "submit": {
        "type": "plain_text",
        "text": "Submit",
        "emoji": True
    },
    "close": {
        "type": "plain_text",
        "text": "Cancel",
        "emoji": True
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
                "text": "Enter Category Name",
                "emoji": True
            }
        }
    ]
}

edit_ask = {
    "type": "modal",
    "callback_id": "edit-prompt",
    "title": {
        "type": "plain_text",
        "text": "Edit",
        "emoji": True
    },
    "submit": {
        "type": "plain_text",
        "text": "Submit",
        "emoji": True
    },
    "close": {
        "type": "plain_text",
        "text": "Cancel",
        "emoji": True
    },
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "What would you like to edit?"
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select an item",
                    "emoji": True
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Event Name",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Start Time",
                            "emoji": True
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "End Time",
                            "emoji": True
                        },
                        "value": "value-2"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Start Date",
                            "emoji": True
                        },
                        "value": "value-3"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "End Date",
                            "emoji": True
                        },
                        "value": "value-4"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Description",
                            "emoji": True
                        },
                        "value": "value-5"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Category",
                            "emoji": True
                        },
                        "value": "value-6"
                    }
                ]
            }
        }
    ]
}

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
            "block_id": "set-date-start",
            "element": {
                "type": "datepicker",
                "initial_date": current_date,
                "action_id": "start-date-set",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select a Date",
                    "emoji": True
                }
            },
            "label": {
                "type": "plain_text",
                "text": "Set Start Date",
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
            "type": "input",
            "block_id": "start-am-pm",
            "element": {
                "type": "static_select",
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "AM",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PM",
                            "emoji": True
                        },
                        "value": "value-1"
                    }
                ]
            },
            "label": {
                "type": "plain_text",
                "text": "Time of day",
                "emoji": True
            }
        },
        {
            "type": "input",
            "block_id": "set-date-end",
            "element": {
                "type": "datepicker",
                "initial_date": current_date,
                "action_id": "end-date-set",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select a Date",
                    "emoji": True
                }
            },
            "label": {
                "type": "plain_text",
                "text": "Set End Date",
                "emoji": True
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
            "type": "input",
            "block_id": "end-am-pm",
            "element": {
                "type": "static_select",
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "AM",
                            "emoji": True
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PM",
                            "emoji": True
                        },
                        "value": "value-1"
                    }
                ]
            },
            "label": {
                "type": "plain_text",
                "text": "Time of day",
                "emoji": True
            }
        },
        {
            "type": "input",
            "block_id": "category",
            "element": {
                "type": "external_select",
                "action_id": "event-category",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select an Event Category",
                    "emoji": True
                },
                "min_query_length": 0
            },
            "label": {
                "type": "plain_text",
                "text": "Event Category",
                "emoji": True
            },
            "optional": True
        }
    ]
}
