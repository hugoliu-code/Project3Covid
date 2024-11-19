from flask import Flask
import json
import random

app = Flask(__name__)

@app.route('/')
def lucky_number():
    # Testing
    return json.dumps({"lucky_number": random.randrange(0,10)})

@app.route('/get_percentile')
def get_percentile():
    # takes in 2 values: county and state

    # returns a float 0-1 representing percentile
    # to be implemented
    return

if __name__ == '__main__':
    app.run(debug=True)