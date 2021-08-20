import pandas as pd
from flask import request, jsonify, Blueprint
import pickle

# Create Flask Blueprint
prediction_api = Blueprint('prediction_api', __name__)


# Load model
model = pickle.load(open('model/model.pkl', 'rb'))


@prediction_api.route('/predict', methods=['POST'])
def predict():
    # Request json data
    data = pd.DataFrame(request.json)

    # Check that number of variables is 25
    if data.shape[1] == 25:
        # Make prediction
        prediction = model.predict(data)
        # Create labels based on predictions (assuming threshold of 0.5)
        label = [1 if i >= 0.5 else 0 for i in prediction]
        # Return the required result
        return jsonify({'Probability': list(prediction), 'Label': list(label), 'Variables': list(data.columns)})
    else:
        return "Number of variables != 25"
