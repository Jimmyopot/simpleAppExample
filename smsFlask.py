from flask import Flask, render_template, request

import base64
import json
import requests
    
    
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():

    api_key       = ""
    api_secret    = ""
        
    # Get Bearer  
    token = api_key + api_secret

    message_bytes = token.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    bearer = base64_bytes.decode('ascii')

        
    # Handle data and send to API enpoint
    post_dict = {
        'unique_ref': '',
        'clientId': '', 
        'dlrEndpoint': '',
        'productId': '',
        'msisdn':  '',
        'message': '',
    }

    data = json.dumps(post_dict) # converts data to json

    url = 'https://api.cemanet.co.ke:8445/Cemanet/api/CemanetBulkApi'  # set url  
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + bearer} # set headers

    r = requests.get(url=url, data=data, headers=headers) # make the request to the API endpoint
    my_data = r.json() # converts the request into json format

    print(my_data) # makes the request and prints to terminal

    
if __name__ == '__main__':
    app.run(debug=True)
    





