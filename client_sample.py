# Author: Brenda Levy
# GitHub username: bqujiada
# Date: 2/8/23 
# Description:
import zmq
import json


dictionary = {"lang": "French", "text": "Hi Clem I love you"}
print("Original text: " + dictionary.get("text"))
json_object = json.dumps(dictionary)
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5545")
socket.send_json(json_object)

stat_update = socket.recv_string()
print("Translation: " + stat_update)
