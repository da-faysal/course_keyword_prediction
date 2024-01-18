# from flask import *
# import json
import pandas as pd
import streamlit as st



# app = Flask(__name__)

# @app.route("/course/", methods=["GET"])
# def predict():
#     model = pd.read_pickle("LogisticRegressionModel.pickle")
#     course = str(request.args.get("course"))
#     prediction = model.predict([course])[0]
#     dataset = {"course_name":f"{course}", "predicted_category":f"{prediction}"}
#     return json.dumps(dataset)


st.markdown("<h4 style='text-align:center; color:chocolate;'>Course Keyword Prediction Page</h4>", unsafe_allow_html=True)
course_name = st.text_input("Enter a course name")
if course_name:
    model = pd.read_pickle("LogisticRegressionModel.pickle")
    pred = model.predict([course_name])
    st.markdown("Prediction Table:")
    st.write(pd.DataFrame({
        "course_name":course_name,
        "prediction":pred[0]
    }, index=[0]))
else:
    st.error("Please enter a course name")
    st.stop()