# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import spacy
nlp = spacy.load("xx_sent_ud_sm")
# This is a simple example for a custom action which utters "Hello World!"

 from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
 class ActionHelloWorld(Action):
#
     def name(self) -> Text:
        return "action_talk_to_skalbe"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link="https://www.liepaja.lv/uzzini-kur-var-versties-pec-palidzibas-lai-atgutu-emocionalo-mieru/"
        # dispatcher.utter_message(text="Hello World!")
        print("Link: ",tracker.get_slot('LINK'))
        text=tracker.latest_message['text']
        print(text)
        dispatcher.utter_template("utter_talk_to_skalbe",tracker,link=Link)
        return []