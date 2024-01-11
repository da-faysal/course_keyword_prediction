from flask import *
import json
import pandas as pd



app = Flask(__name__)

@app.route("/course/", methods=["GET"])
def predict():
    model = pd.read_pickle("LogisticRegressionModel.pickle")
    course = str(request.args.get("course"))
    prediction = model.predict([course])[0]
    dataset = {"course_name":f"{course}", "predicted_category":f"{prediction}"}
    return json.dumps(dataset)