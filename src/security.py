
import ssl
from flask import Flask, request

app = Flask(__name__)

# SSL context for HTTPS
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('path/to/cert.pem', 'path/to/key.pem')

@app.route('/secure_endpoint', methods=['GET', 'POST'])
def secure_endpoint():
    # Only allow HTTPS requests
    if request.is_secure:
        return "Secure Endpoint. Your data is safe."
    else:
        return "Insecure access denied", 403

if __name__ == '__main__':
    app.run(ssl_context=context)
