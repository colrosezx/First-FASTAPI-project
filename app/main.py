from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()



@app.get('/students/{course}')
def get_all_students(course: Optional[int] = None, major: Optional[str] = None, enrollment_year: Optional[int] = 2018):
    students = json_to_dict_list(path_to_json)

    filtered_students = []
  

    for student in students:
        if student['course'] == course:
            filtered_students.append(student)

    if major:
        filtered_students = [student for student in filtered_students if student['major'].lower() == major.lower()]

    if enrollment_year:
        filtered_students = [student for student in filtered_students if student['enrollment_year'] == enrollment_year]

    return filtered_students


@app.get("/students")
def get_all_students():
    return json_to_dict_list(path_to_json)


@app.get('/')
def hello_page():
    return {'message': 'Привет, хабр!'}

