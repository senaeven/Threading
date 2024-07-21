import requests
import threading

def get_crypto_data():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code == 200:
        return response.json()

crypto_response = get_crypto_data()
user_input = input("Enter you crypto currency:")
for crypto in crypto_response:
    if crypto["currency"] == user_input:
        print(crypto["price"])
        break

#print(response.status_code)
#time.time o anki zamanını alır.