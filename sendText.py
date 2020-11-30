import base64
import json
import requests
    

api_key       = "JBC8ZW9QKRDH3S41"
api_secret    = "49c2a14f7ae5e48bdd3d3f37ca7669e47e803a69fa5b96972a9fa236682ffbca"
    
# Get Bearer  
token = api_key + api_secret

message_bytes = token.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
bearer = base64_bytes.decode('ascii')

    
# Handle data and send to API enpoint
post_dict = {
    'unique_ref': '13478',
    'clientId': '35', 
    'dlrEndpoint': 'http://144.91.72.35:8080/Cemanet/SendSMSEndpointServlet',
    'productId': '38',
    'msisdn':  '254724021814',
    'message': 'THIS IS API TEST',
}

data = json.dumps(post_dict) # converts data to json

url = 'https://api.cemanet.co.ke:8445/Cemanet/api/CemanetBulkApi'  # set url  
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + bearer} # set headers

r = requests.get(url=url, data=data, headers=headers) # make the request to the API endpoint
my_data = r.json() # converts the request into json format

print(my_data) # makes the request and prints to terminal

    
    





