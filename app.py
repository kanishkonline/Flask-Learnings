from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HOME PAGE"

@app.route("/user/<int:id>")
def users(id):
    return f"User ID: {id} THIS IS INTEGER CONVERTOR"

@app.route("/price/<float:amount>")
def price(amount):
    return f"PRICE IS : {amount} -- THIS IS FLOAT CONVERTOR"

@app.route("/who/<string:anything>")
def who(anything):
    return f"WHO IS : {anything} -- THIS IS STRING CONVERTOR"

@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str(user_id)

if __name__ == "__main__":
    app.run(debug=True)