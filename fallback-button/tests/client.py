from typing import Any, Text, Dict, List
import uuid
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class Client:
    def __init__(self, action):
        self.action = action

    def invoke_message(self, message, slots=None):
        if not slots:
            slots = {}

        dispatcher = CollectingDispatcher()

        tracker = Tracker(
            sender_id=str(uuid.uuid4()),
            slots=slots,
            latest_message=message,
            events=[],
            paused=False,
            followup_action=None,
            active_loop={},
            latest_action_name=None
        )

        domain = {}

        slots = self.action.run(dispatcher=dispatcher, tracker=tracker, domain=domain)
        return dispatcher.messages[0], slots