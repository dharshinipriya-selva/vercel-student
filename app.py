from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('q-vercel-python.json', 'r') as f:
    student_data = json.load(f)

@app.route('/api')
def get_marks():
    names = request.args.getlist('name')

    if not names:  # No names provided, return all data
        return jsonify({"marks": student_data})

    else:  # Names provided, return marks for those names
        marks = []  # Initialize marks as a list
        for name in names:
            mark_found = False
            for student in student_data:
                if student.get('name') == name:  # Use .get() to handle missing names
                    marks.append(student.get('marks'))  # Add the mark to the list
                    mark_found = True
                    break  # Exit inner loop once name is found
            if not mark_found:
                marks.append(0)  # Add 0 if the name is not found

        return jsonify(marks)  # Return the list of marks
