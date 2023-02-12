# CS 361 Microservice: Translator Program

<h3>How to request Data:</h3>

First the client must connect to the server socket. This can be done with the following code:

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5545")

Once the client has connected, they can request a translation by sending the server a json object with properties lang 
for language to translate to, and text for the text to translate. The server then receives this data and translates the 
text into the selected language. An example would be:

dictionary = {"lang": "French", "text": "Hi how are you?"}
print("Original text: " + dictionary.get("text"))
json_object = json.dumps(dictionary)
socket.send_json(json_object)

<h3>How to receive Data:</h3> 

Once the client has sent a request by sending the json object containing language and text to the server, the server 
will send back a response as a json object with one property, "text". The value will be the translated text. The code
on the client side to receive this text will be: 

result = socket.recv_json()

