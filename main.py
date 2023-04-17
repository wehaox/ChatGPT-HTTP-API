import json
from revChatGPT.V1 import Chatbot
from flask import Flask, jsonify, request

server = Flask(__name__)


with open("config.json", "r") as f:
    config = json.load(f)

# init chatbot
chatbot = Chatbot(config['auth'])

def send_gpt(message, cid, pid):
    if message == 'hi' and cid == None:  
        chatbot.reset_chat()
    result = ""

    for data in chatbot.ask(
        message, conversation_id=cid, parent_id=pid
    ):
        result = data
    return result


class Data:
    def __init__(self, code, data, err):
        self.code = code
        self.data = data
        self.err = err


@server.route(config['path'], methods=['POST'])
def get_request_json():
    if request.method == 'POST':
        mess = Data(200, "null", "null")
        getData = request.get_json()
        print("======================================")
        print("接到请求:", getData)

        if len(getData) != 4:
            mess.err = "bad data"
            jsonString = json.dumps(mess.__dict__)
            return jsonString, {"Content-Type": "application/json"}
        else:
            user = getData[3]
            msg = getData[0]
            cid = getData[1]
            pid = getData[2]
            # res = "test"
            if user == 'getSeesions':
                res = send_gpt("hi", None, None)
                print(res)
                mess.data = res
                jsonString = json.dumps(mess.__dict__)
            else:
                res = send_gpt(msg, cid, pid)
                mess.data = res
                jsonString = json.dumps(mess.__dict__)

            return jsonString, {"Content-Type": "application/json"}

@server.errorhandler(Exception)
def handle_error(e):
    return jsonify({'code':'500','data':'null','err': str(e)}), 200

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=config['port'])