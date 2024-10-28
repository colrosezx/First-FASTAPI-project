import requests


# def get_all_students():
#     url = "http://127.0.0.1:8000/students"
#     response = requests.get(url)
#     return response.json()

import requests


def select_students_with_id(student_id: int):
    url = 'http://127.0.0.1:8000/students'
    response = requests.get(url)
    students = response.json()

    for student in students:
        if student.get("student_id") == student_id:
            return student             

    
def get_info_about_student(student):
    if student:
        print(student.get('first_name'))
        print(student.get('last_name'))
        print(student.get('email'))
    else:
        print('Студент не найден')


student = select_students_with_id(9)

print(get_info_about_student(student))