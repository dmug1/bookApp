from flask import Flask, render_template, url_for, request
#from retrieveAPI import *

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        task_content = request.form['book']
    else:
        return render_template("bookapp.html")

if __name__ == "__main__":
    app.run(debug=True)