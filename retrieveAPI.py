#python search and retrieve

import urllib.request
import json
import textwrap
import sys

def getBookInfo(bookSearch):
    bookSearch = bookSearch.replace(" ","%20")
    urlContainer = "https://www.googleapis.com/books/v1/volumes?q=" + bookSearch
    print(urlContainer)
    try:
        with urllib.request.urlopen(urlContainer) as f:
            text = f.read()
            decodedtext = text.decode('utf-8')
            print(textwrap.fill(decodedtext, width=50))
    except Exception as ec:
        print("Connection error, could not reach Google API: %s" %str(ec))
       

    obj = json.loads(decodedtext)
    print(obj['items'][0]['searchInfo']['textSnippet'])
    return(obj['items'][0]['searchInfo']['textSnippet'])