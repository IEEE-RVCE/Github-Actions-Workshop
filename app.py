from flask import Flask

app = Flask(__name__)


# A simple endpoint that returns the list of attendees 
@app.route('/')
def index():
    attendees = ['A', 'B', 'C', 'D'
    return {'Attendees': attendees}


if __name__ == "__main__":
    # Runs on port 5000 by default
    app.run(debug=True, host='0.0.0.0')
