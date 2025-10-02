from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from sentence_transformers import SentenceTransformer
import faiss


class ActionRetrieveFAQ(Action):
    def name(self):
        return "action_retrieve_faq"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        user_msg = tracker.latest_message.get("text")

        # Example: FAISS retrieval placeholder
        response = f"Retrieved FAQ answer for: '{user_msg}'"

        dispatcher.utter_message(text=response)
        return []
