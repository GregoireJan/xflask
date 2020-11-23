from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from modeler.modeler import Modeler

app = Flask(__name__)
api = Api(app)

class Predict(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        x = data['x']
        m = Modeler()
        prediction = m.predict(x)
        return jsonify({
            "Input": x,
            "y": prediction
        })

api.add_resource(Predict, "/predict")

if __name__ == "__main__":
    ## Uncomment for flask only (no docker container)
    # app.run(debug=True)
    ## Comment out for flask only (no docker container)
    app.run(host="0.0.0.0", port=8080)