import requests

    # Requête GET
response = requests.get('http://127.0.0.1:5000/communes')
print(response.text)

    # Requête POST
data = {"ville": "Goma", "nom": "Goma"}
response = requests.post('http://127.0.0.1:5000/communes', json=data)
print(response.text)
    