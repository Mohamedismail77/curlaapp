from flask import Flask,request
import pycurl
import io
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/',methods=['POST'])
def getSocialLinks():
    requestedLink = request.form['link']
    return {"data":getLinks(requestedLink)}


def getLinks(link):
    buffer = io.BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, link)
    c.setopt(pycurl.SSL_VERIFYPEER, True)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.VERBOSE, 1)
    c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201")
    c.setopt(c.WRITEFUNCTION, buffer.write)
    c.perform()
    c.close()

    body = buffer.getvalue().decode('UTF-8')
    # Body is a string in some encoding.
    # In Python 2, we can print it without knowing what the encoding is.
    soup = BeautifulSoup(body,'html.parser')
    
    links = soup.find_all('a')

    social = ['facebook.com','fb.com','twitter.com','instagram.com','youtube.com']
    result = []
    for pattern in social:
        for link in links:
            print(link.get('href'))
            href = link.get('href')
            search = href.find(pattern)
            if search != -1:
                #print(href)
                #print(href,file=open("links.txt","a"))
                result.append(href)
    return result
