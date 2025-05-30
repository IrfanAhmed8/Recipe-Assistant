import json
import requests
 
def api_response(query,cuisine):
   
    api_key='a41cdc65e2e74365bbf23fcd0079dedf'
    api_url=f'https://api.spoonacular.com/recipes/complexSearch?&apiKey={api_key}&query={query}&cuisine={cuisine}'
    response_from_server=requests.get(api_url)
    return response_from_server.json()
