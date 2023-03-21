# <==== Importing Dependencies ====>

import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

# <==== Code starts here ====>

# class course:
#     def __init__(self, name, url):
#         self.name = name
#         self.url = url

courses_list = pickle.load(open('./courses.pkl', 'rb'))
similarity = pickle.load(open('./similarity.pkl', 'rb'))


def recommend(course):
    index = courses_list[courses_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    course_names = []
    course_urls = []
    cos_similarity = []
    for i in distances[1:7]:
        course_name = courses_list.iloc[i[0]].course_name
        print(courses_list.iloc[i[0]])
        course_url = courses_list.iloc[i[0]]['Course URL']
        course_names.append(course_name)
        course_urls.append(course_url)
        cos_similarity = [i[0] for i in distances[1:7]]
        # recommended_course_names.append(course(course_name, course_url))

    recommended_courses = pd.DataFrame({
        "name": course_names,
        "url": course_urls,
        "cos_similarity": cos_similarity
    })
    return recommended_courses


st.markdown(
    f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
    unsafe_allow_html=True
)
st.markdown("<h2 style='text-align: center; color: blue;'>Placement Course Recommendation System</h2>",
            unsafe_allow_html=True)
st.markdown(
    "<h4 style='text-align: center; color: black;'>Find similar courses from a dataset of over 3,000 courses from Coursera!</h4>",
    unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Web App created by  Your Name</h4>", unsafe_allow_html=True)

course_list = courses_list['course_name'].values
selected_course = st.selectbox(
    "Type or select a course you like :",
    courses_list
)

if st.button('Show Recommended Courses'):
    st.write("Recommended Courses based on your interests are :")
    recommended_course_names = recommend(selected_course)
    st.table(recommended_course_names)
    # st.text(recommended_course_names[0].name)
    # st.text(recommended_course_names[1])
    # st.text(recommended_course_names[2])
    # st.text(recommended_course_names[3])
    # st.text(recommended_course_names[4])
    # st.text(recommended_course_names[5])
    # st.text(" ")
    st.markdown(
        "<h6 style='text-align: center; color: red;'>Copyright reserved by Coursera and Respective Course Owners</h6>",
        unsafe_allow_html=True)

# <==== Code ends here ====>
