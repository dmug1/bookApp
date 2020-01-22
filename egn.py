from flask import Flask, render_template, url_for, request, redirect
from retrieveAPI import *

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    bookInfo = ""
    if request.method == "POST":
        task_content = request.form['book']
        bookInfo =  getBookInfo(task_content)      
        return render_template("bookapp.html", bookInfo=bookInfo)
    else:
        return render_template("bookapp.html", bookInfo=bookInfo)

if __name__ == "__main__":
    app.run(debug=True)