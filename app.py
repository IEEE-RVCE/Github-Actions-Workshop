from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    attendees = ['A', 'B', 'C']
    return {'Attendees': attendees}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
