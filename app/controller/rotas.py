from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "<h1>Olá!</h1>" 