import json
from lunr import lunr
from lunr.index import Index

from clumper import Clumper
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

recipes = Clumper.read_jsonl("static/recipes.jsonl").collect()

class ActionSuggestRecipe(Action):

    def name(self) -> Text:
        return "action_suggest_recipe"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        db = {d['uid']: d for d in recipes}
        with open("static/index.json", "r") as f:
            idx = Index.load(json.loads(f.read()))
        matches = idx.search(tracker.latest_message['text'])

        if len(matches) == 0:
            dispatcher.utter_message(text="Sorry, I couldn't find any recipes.")
            return []
        dispatcher.utter_message(text="These recipes might be interesting.")
        for match in matches[:5]:
            item = db[match['ref']]
            dispatcher.utter_message(f" - {item['name']}")
        return []
