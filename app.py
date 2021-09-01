from flask import Flask
from flask_restful import Api, Resource, reqparse
import pickle
import numpy as np
import pandas as pd
import os

APP = Flask(__name__)
API = Api(APP)


model = pickle.load(open('model_train', 'rb'))
data_prep= pickle.load(open("data_transformer", 'rb'))
processed_data = pd.read_csv("defaults_selected.csv")
data_prep.fit(processed_data)

class Predict(Resource):

    @staticmethod
    def post():
        # args = request.json

        instance = reqparse.RequestParser()
        instance.add_argument('Credit')
        instance.add_argument('Gender')
        instance.add_argument('Education')
        instance.add_argument('Marital') # Number of Children (0-5)
        instance.add_argument('Age')     # Yes = 1 or No = 0
        instance.add_argument('Default')   # Options: 1,2,3 or 4
        args = instance.parse_args()       # creates dict

        input_df = pd.DataFrame([args])
        x = data_prep.transform(input_df)

        out = {'Prediction': np.where(model.predict([x[0,0:-1]]) > 0.5, "Yes", "No")[0], 'x_new':args}

        return out, 200

API.add_resource(Predict, '/predict')

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    APP.run(threaded=True, host='0.0.0.0', port=port)
