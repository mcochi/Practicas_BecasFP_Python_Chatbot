# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

import pymongo

class ValidateNombreForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_nombre_form"

    def validate_tos(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if(slot_value.lower() == 'yes'):
            return {"tos": True}
        else: 
            if(slot_value.lower()=='no'):
                return {"tos": False}
            else:
                dispatcher.utter_message(text="Sorry, but I didn't understand, can you please repeat the anwser (yes or no)?")
                return {"tos": None}

    def validate_feel_tired(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if(slot_value.lower() == 'yes'):
            return {"feel_tired": True}
        else: 
            if(slot_value.lower()=='no'):
                return {"feel_tired": False}
            else:
                dispatcher.utter_message(text="Sorry, but I didn't understand, can you please repeat the anwser (yes or no)?")
                return {"feel_tired": None}

    def validate_aches_pains(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if(slot_value.lower() == 'yes'):
            return {"aches_pains": True}
        else: 
            if(slot_value.lower()=='no'):
                return {"aches_pains": False}
            else:
                dispatcher.utter_message(text="Sorry, but I didn't understand, can you please repeat the anwser (yes or no)?")
                return {"aches_pains": None}

    
    def validate_sore_throat(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if(slot_value.lower() == 'yes'):
            return {"sore_throat": True}
        else: 
            if(slot_value.lower()=='no'):
                return {"sore_throat": False}
            else:
                dispatcher.utter_message(text="Sorry, but I didn't understand, can you please repeat the anwser (yes or no)?")
                return {"sore_throat": None}

class ActionInsertMongo(Action):
    def name(self) -> Text:
        return "action_insert_mongo"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        
        dispatcher.utter_message(text='Storing Data')
        name = tracker.get_slot('name')
        tos = tracker.get_slot('tos')
        feel_tired = tracker.get_slot('feel_tired')
        aches_pains = tracker.get_slot('aches_pains')
        sore_throat = tracker.get_slot('sore_throat')

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]
        mydict = { "tos": tos, "feel_tired": feel_tired, "sore_throat": sore_throat, "name": name}
        x = mycol.insert_one(mydict)
