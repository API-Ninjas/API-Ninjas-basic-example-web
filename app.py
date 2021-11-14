from flask import Flask, render_template
import requests


TRIVIA_URL = 'https://api.api-ninjas.com/v1/trivia'

app = Flask(__name__)

@app.route('/')
def index():
    resp = requests.get(TRIVIA_URL, headers={'X-Api-Key': 'YOUR API KEY'}).json()
    trivia = resp[0]
    return render_template('index.html', question=trivia['question'], answer=trivia['answer'])

app.run()