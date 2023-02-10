# Author: Brenda Levy
# GitHub username: bqujiada
# Date: 2/8/23 
# Description: translator microservice

import deepl
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5545")

auth_key = "daa3f4d8-0bb7-0fb2-4f7d-21f9e4acc196:fx"
translator = deepl.Translator(auth_key)

languages = {"French": "FR", "German": "DE", "Spanish": "ES", "Danish": 'DA', "Italian": "IT"}

while True:
    dictionary = socket.recv_json()
    content = dictionary.get("text")
    selected_lang = dictionary.get("lang")
    abrev = languages.get(selected_lang)
    result = translator.translate_text(content, target_lang=abrev)
    print("translation to " + selected_lang + ":")
    print(result.text)
    socket.send_json({'text': result.text})
