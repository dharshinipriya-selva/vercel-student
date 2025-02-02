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
    marks = []

    def find_mark(name):
        for student in student_data:
            if student.get('name').strip() == name.strip():
                return student.get('marks')
        return 0  # Return 0 if name is not found

    if names:
        for name in names:
            mark = find_mark(name)
            marks.append(mark)

    return jsonify({"marks": marks})
if __name__ == '__main__':
    app.run(debug=True)
