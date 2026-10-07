from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HOME PAGE"

@app.route("/about")
def about():
    return "ABOUT PAGE"

@app.route("/contact")
def contact():
    return "CONTACT US"

if __name__ == "__main__":
    app.run(debug=True)