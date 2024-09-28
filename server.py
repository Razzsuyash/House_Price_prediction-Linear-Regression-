from flask import Flask, request, jsonify
import util  # Assuming util contains get_location_names and get_estimated_price

app = Flask(__name__)

# Root endpoint for the homepage or a welcome message
@app.route('/')
def home():
    return "<h1>Welcome to the Home Price Prediction API</h1>"

# Endpoint to get location names
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Endpoint to predict home price
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)
