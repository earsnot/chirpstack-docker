import json
import requests
from datetime import datetime

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
api = 'http://localhost:8080/api/'
s = requests.Session()

def get_jwt():
    data = '{"password": "admin", "email": "admin"}'
    response = requests.post(api+'internal/login', headers=headers, data=data)
    response_data = json.loads(response.content)
    print(response_data)
    if(response_data.get('jwt')):
        headers['Authorization'] = response_data.get('jwt')
        print('logged in')
        return True
    else:
        print('login failed')
        return False

def get_gateway():
    get_app = s.get(api+'gateways?limit=1', headers=headers)
    return json.loads(get_app.content)
    
def get_network_server():
    limit = 'limit=1'
    get_app = s.get(api+'network-servers?'+limit, headers=headers)
    response_data = json.loads(get_app.content)
    print(response_data)

def set_network_server():
    data = "chirpstack-network-server:8000"
    response = requests.post(api+"network-servers", headers=headers, data=data)

def delete_network_server(server_id):
    request = f"network-servers/{server_id}"
    response = requests.delete(api+request, headers=headers)



def main():
    get_jwt()
    get_network_server()
    gw = get_gateway()
    
    print(get_gateway())
if __name__ == '__main__':
    main()
    