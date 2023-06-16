from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Define the /encrypt route
@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    message = data['message']

    # Encrypt the message
    encrypted_message = cipher_suite.encrypt(message.encode())

    return jsonify({'encrypted_message': encrypted_message.decode()})

# Define the /decrypt route
@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    encrypted_message = data['encrypted_message']

    # Decrypt the message
    decrypted_message = cipher_suite.decrypt(encrypted_message.encode())

    return jsonify({'decrypted_message': decrypted_message.decode()})

if __name__ == '__main__':
    app.run()

