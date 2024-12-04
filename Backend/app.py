from flask import Flask, request, jsonify
from flask_cors import CORS
from DataClean import get_data
import json
import random

app = Flask(__name__)
CORS(app)

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

@app.route('/get_percentile_test', methods=['POST'])
def get_percentile_test():
    request_data = request.get_json()
    data = get_data()
    data.sort(key = lambda x: x[2])

    data_length = len(data)
    n = data_length-1
    while(n >= 0):
        if(data[n][1].lower() == request_data.get("state").lower() and data[n][0].lower() == request_data.get("county").lower() + " county"):
            return jsonify({
                "percentile": n/data_length,
                "position": n,
                "total" : data_length,
                "merge_time" : 1,
                "heap_time" : 1
            }), 200
        n-=1
    
    return jsonify({"error" : "County and State not found"}), 422
    
if __name__ == '__main__':
    app.run(debug=True)