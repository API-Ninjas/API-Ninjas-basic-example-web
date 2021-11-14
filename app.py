from flask import Flask, render_template
import requests

# Define API URL.
TRIVIA_URL = 'https://api.api-ninjas.com/v1/trivia'

# Initialize Flask.
app = Flask(__name__)

# Define routing.
@app.route('/')
def index():
    # Make API Call - make sure to use a valid API key.
    resp = requests.get(TRIVIA_URL, headers={'X-Api-Key': 'YOUR API KEY'}).json()
    # Get first trivia result since the API returns a list of results.
    trivia = resp[0]
    # Render HTML using the trivia question and answer.
    return render_template('index.html', question=trivia['question'], answer=trivia['answer'])

# Run the Flask app (127.0.0.1:5000 by default).
app.run()
