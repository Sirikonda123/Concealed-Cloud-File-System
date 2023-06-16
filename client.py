# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 09:38:38 2023

@author: Admin
"""

import requests

# Define the server URL
import requests

# Define the server URL
SERVER_URL = 'http://127.0.0.1:5000'

def encrypt_message(message):
    # Send a POST request to the server to encrypt the message
    url = f'{SERVER_URL}/encrypt'
    response = requests.post(url, json={'message': message})
    
    if response.status_code == 200:
        encrypted_data = response.json()
        return encrypted_data['encrypted_message']
    else:
        print(f'Error: {response.status_code} - {response.text}')
        return None

def decrypt_message(encrypted_message):
    # Send a POST request to the server to decrypt the message
    url = f'{SERVER_URL}/decrypt'
    response = requests.post(url, json={'encrypted_message': encrypted_message})
    
    if response.status_code == 200:
        decrypted_data = response.json()
        return decrypted_data['decrypted_message']
    else:
        print(f'Error: {response.status_code} - {response.text}')
        return None

# Example usage
message = 'Hello, Dark Cloud!'
encrypted_message = encrypt_message(message)
if encrypted_message:
    print(f'Encrypted Message: {encrypted_message}')

    decrypted_message = decrypt_message(encrypted_message)
    if decrypted_message:
        print(f'Decrypted Message: {decrypted_message}')
