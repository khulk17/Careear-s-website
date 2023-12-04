from flask import Flask,render_template

app=Flask(__name__)

JOBS=[
    {
        "id":1,
        "title":'Data Analyst',
        "Location":"Bengaluru,India",
        "Salary":"Rs :10,00,000"
    },
    {
        "id":2,
        "title":'Data Scientist',
        "Location":"Delhi,India",
        "Salary":"Rs: 10,50,000"
    },
    {
        "id":3,
        "title":'Frontend Devloper',
        "Location":"Bengaluru,India",
        "Salary":"Rs: 12,00,000"
    },
    {
        "id":4,
        "title":'Backend Developer',
        "Location":"San Fransisco,USA",
        "Salary":"$120,000"
    },
]

@app.route('/')
def hello_world():
    return render_template("home.html",jobs=JOBS)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)