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

# Now use unique_student_data in your API route
@app.route('/api')
def get_marks():
    names = request.args.getlist('name')
    marks = []

    if not names:  # No names provided, return all data as a list of marks
        all_marks = [student['marks'] for student in unique_student_data]
        return jsonify(all_marks)
    else:
        for name in names:
            mark_found = False
            for student in unique_student_data:  # Use unique_student_data here
                if student.get('name') == name:
                    marks.append(student.get('marks'))
                    mark_found = True
                    break  # Exit inner loop once name is found
            if not mark_found:
                marks.append(0)  # Add 0 if the name is not found

        return jsonify(marks)
