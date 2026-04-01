from flask import Flask, render_template, request

app = Flask(__name__)

# Store students
students = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    course = request.form['course']

    # Save student
    students.append({'name': name, 'age': age, 'course': course})

    # Count total students
    total = len(students)

    # Count course-wise
    course_count = {}
    for s in students:
        c = s['course']
        course_count[c] = course_count.get(c, 0) + 1

    return render_template('result.html',
                           name=name,
                           age=age,
                           course=course,
                           total=total,
                           course_count=course_count)

if __name__ == '__main__':
    app.run(debug=True)