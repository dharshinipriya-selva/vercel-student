from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('q-vercel-python.json', 'r') as f:
    student_data = json.load(f)

# Deduplicate the student_data (keep only the first occurrence of each name)
unique_student_data = []
seen_names = set()
for student in student_data:
    if student['name'] not in seen_names:
        unique_student_data.append(student)
        seen_names.add(student['name'])

@app.route('/api')
def get_marks():
    name1 = request.args.get('name1')  # Get the value of name1 from url.
    name2 = request.args.get('name2')  # Get the value of name2 from url.

    marks = []

    if name1:
        mark1 = 0  # Default mark if not found
        for student in unique_student_data:
            if student.get('name') == name1:
                mark1 = student.get('marks')
                break
        marks.append(mark1)

    if name2:
        mark2 = 0  # Default mark if not found
        for student in unique_student_data:
            if student.get('name') == name2:
                mark2 = student.get('marks')
                break
        marks.append(mark2)

    return jsonify(marks)  # Return marks as a list
