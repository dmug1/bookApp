#python search and retrieve

import urllib.request
import json
import textwrap
#from flask import Flask
#from flask import request

bookSearch = ""

#have to learn flask first!
#@app.route('/searchForBook', methods=['POST'])
#def searchForBook():
#    if request.method == "POST":
#        bookSearch = request.form['book']
#    else:
#        bookSearch = 'Invalid book'

bookSearch = input("qual livro?")
#with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1408865262") as f:
bookSearch = bookSearch.replace(" ","%20")

urlContainer = "https://www.googleapis.com/books/v1/volumes?q=" + bookSearch

print(urlContainer)

#with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=harry%20potter") as f:
with urllib.request.urlopen(urlContainer) as f:
    text = f.read()
    decodedtext = text.decode('utf-8')
    print(textwrap.fill(decodedtext, width=50))

print()

obj = json.loads(decodedtext)
print(obj['items'][0]['searchInfo']['textSnippet'])