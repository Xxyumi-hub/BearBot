import os
import tensorflow as tf
from tensorflow import keras
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from PIL import Image
import requests
from io import BytesIO
import numpy as np
import pprint
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

pp = pprint.PrettyPrinter(indent=4)
class ActionTest(Action):
    def __init__(self):
        self.class_names = ['grizzly bear', 'panda bear', 'polar bear', 'sun bear']
        self.model = tf.keras.models.load_model('/Users/cr33d/smart_bot/bot/actions/bearopedia.h5')
    def name(self):
        return 'action_predict_image'
    def run(self, dispatcher, tracker, domain):
        url = tracker.current_state()['events'][-1]['text']
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((159, 159))
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = self.model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        print("This image most likely belongs to {} with a {:.2f} percent confidence.".format(self.class_names[np.argmax(score)], 100 * np.max(score)))
        dispatcher.utter_message(text = f'This image most likely belongs to {self.class_names[np.argmax(score)]} with a {100 * np.max(score):.2f} percent confidence.')