
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error='Page not found'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error='Internal server error'), 500

if __name__ == "__main__":
    app.run(debug=True)
