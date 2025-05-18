# app.py - Simplified startup
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return "Token Aggregator Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
