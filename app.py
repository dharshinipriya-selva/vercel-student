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
        return jsonify({"marks": student_data})  # Returns the list of dictionaries

    else:  # Names provided, return marks for those names
        marks = {}
        for name in names:
            found = False  # Flag to check if name was found
            for student in student_data:  # Iterate through the list of students
                if student['name'] == name:  # Check if the name matches
                    marks[name] = student['marks']  # Add marks to the dictionary
                    found = True
                    break  # Exit inner loop once name is found
            if not found:
                marks[name] = "Mark for " + name + " not found"  # Name not found

        return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)