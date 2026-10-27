from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    first_name = "Kanishk"
    last_name = "Singh"
    course = "Flask"
    city = "Delhi"
    course_price = 1000
    future_courses = [
        "Linux",
        "SQL",
        "Django",
        "FaSt API"
    ]
    return render_template("index.html",
                           first_name = first_name,
                           last_name = last_name,
                           course = course,
                           city = city,
                           course_price = course_price,
                           future_courses = future_courses)

if __name__ == "__main__":
    app.run(debug=True)