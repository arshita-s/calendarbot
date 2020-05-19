"""
Here are all of the blocks, views, modals, etc.

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
            },
            {
                "type": "button",
                "action_id": "remind",
                "text": {
                    "type": "plain_text",
                    "text": "Remind Me of an Event",
                    "emoji": True
                },
                "value": "remind_user"
            }
        ]
    }
]

event_name = {
    "type": "modal",
    "callback_id": "edit-name",
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
        }
    ]
}

start_time = {
    "type": "modal",
    "callback_id": "edit-start-time",
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
                "action_id": "start-am-pm-set",
                "type": "static_select",
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "AM",
                            "emoji": True
                        },
                        "value": "AM"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PM",
                            "emoji": True
                        },
                        "value": "PM"
                    }
                ]
            },
            "label": {
                "type": "plain_text",
                "text": "Time of day",
                "emoji": True
            }
        }
    ]
}

end_time = {
    "type": "modal",
    "callback_id": "edit-end-time",
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
                "action_id": "start-am-pm-set",
                "type": "static_select",
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "AM",
                            "emoji": True
                        },
                        "value": "AM"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PM",
                            "emoji": True
                        },
                        "value": "PM"
                    }
                ]
            },
            "label": {
                "type": "plain_text",
                "text": "Time of day",
                "emoji": True
            }
        }
    ]
}

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
            "block_id": "prompt-edit",
            "element": {
                "action_id": "prompt",
                "type": "static_select",
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
            },
            "label": {
                "type": "plain_text",
                "text": "What would you like to edit?",
                "emoji": True
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
                "action_id": "start-am-pm-set",
                "type": "static_select",
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "AM",
                            "emoji": True
                        },
                        "value": "AM"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PM",
                            "emoji": True
                        },
                        "value": "PM"
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
                "action_id": "end-am-pm-set",
                "type": "static_select",
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "AM",
                            "emoji": True
                        },
                        "value": "AM"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PM",
                            "emoji": True
                        },
                        "value": "PM"
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

reminder_modal = {
    "type": "modal",
    "callback_id": "reminder",
    "title": {
        "type": "plain_text",
        "text": "Set a Reminder",
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
                "action_id": "event-reminder",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select an Event",
                    "emoji": True
                },
                "min_query_length": 0
            },
            "label": {
                "type": "plain_text",
                "text": "Reminder",
                "emoji": True
            },
            "optional": False
        }
    ]
}

set_reminder_modal = {
    "type": "modal",
    "callback_id": "set-reminder-time",
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
            "block_id": "remind-date-start",
            "element": {
                "type": "datepicker",
                "initial_date": current_date,
                "action_id": "remind-date-set",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select a Date",
                    "emoji": True
                }
            },
            "label": {
                "type": "plain_text",
                "text": "Set Reminder Date",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Select a Reminder Time*"
            }
        },
        {
            "type": "input",
            "block_id": "remind-hour",
            "element": {
                "type": "plain_text_input",
                "action_id": "remind-hour-set",
                "max_length": 2
            },
            "label": {
                "type": "plain_text",
                "text": "Reminder Hour"
            }
        },
        {
            "type": "input",
            "block_id": "remind-minute",
            "element": {
                "type": "plain_text_input",
                "action_id": "remind-minute-set",
                "max_length": 2
            },
            "label": {
                "type": "plain_text",
                "text": "Reminder Minute"
            }
        },
        {
            "type": "input",
            "block_id": "remind-am-pm",
            "element": {
                "action_id": "remind-am-pm-set",
                "type": "static_select",
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "AM",
                            "emoji": True
                        },
                        "value": "AM"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "PM",
                            "emoji": True
                        },
                        "value": "PM"
                    }
                ]
            },
            "label": {
                "type": "plain_text",
                "text": "Time of day",
                "emoji": True
            }
        },
    ]

}