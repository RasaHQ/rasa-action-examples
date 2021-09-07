from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCustomFallback(Action):

    def name(self) -> Text:
        return "action_custom_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        intents = [i for i in tracker.current_state()['latest_message']['intent_ranking'] if i['name'] != 'nlu_fallback']
        allowed_intents = ["new_order", "what_happened", "inform"]
        message = {
            "new_order": "Do you want to place a new order?",
            "what_happened": "Do you want to ask about a previous order?",
            "inform": "Would you like more information about stroopwafels?"
        }
        buttons = [{'payload': i['name'], 'title': message[i['name']]} for i in intents[:3] if i['name'] in allowed_intents]
        dispatcher.utter_message(
            text="It wasn't 100% clear what you meant. Could you speficy/rephrase?",
            buttons=buttons
        )
        return []
