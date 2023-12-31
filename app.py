from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data analyst',
  'location': 'Toronto, Canada',
  'salary': '$60,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Ottawa, Canada',
  'salary': '$70,000'
}, {
  'id': 3,
  'title': 'Front-end Engineer',
  'location': 'Remote',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'London, Canada',
  'salary': '$180,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jobbit')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
