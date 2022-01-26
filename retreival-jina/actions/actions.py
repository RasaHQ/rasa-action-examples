import httpx 
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests as rq

class ActionSuggestRecipe(Action):

    def name(self) -> Text:
        return "action_suggest_recipe"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        async with httpx.AsyncClient() as client:
            resp = await client.post("http://localhost:12345/search", json={"data": [{"mime_type": "text/plain", "text": tracker.latest_message['text']}]})
        
        dispatcher.utter_message(text="I found these recipes:")
        matches = resp.json()['data']['docs'][0]['matches']
        for m in matches[:5]:
            dispatcher.utter_message(text=f"- {m['text']}")

        return []
