from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HOME PAGE"

@app.route("/users")
def users():
    return "THIS IS USERS PAGE"

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/student/<name>/<course>")
def student(name,course):
    return f"{name} is learning {course}"

if __name__ == "__main__":
    app.run(debug=True)