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

    if not names:  # No names provided, return all data (if needed)
        return jsonify({"marks": student_data})

    else:  # Names provided, return marks for those names
        marks = {}
        for name in names:
            found = False
            for student in student_data:
                if student['name'] == name:
                    marks[name] = student['marks']
                    found = True
                    break
            if not found:
                marks[name] = "Mark for " + name + " not found"

        # Extract only the values (marks) and return them as a list
        marks_list = list(marks.values())  # Convert the dictionary values to a list
        return jsonify(marks_list)  # Return the list of marks
