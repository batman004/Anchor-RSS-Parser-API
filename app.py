from flask import Flask,jsonify,request
from flask_cors import CORS,cross_origin
import feedparser
from markupsafe import escape
import os
import re

app=Flask(__name__)
CORS(app)
# app.config['SECRET_KEY']=ENV['SECRET_KEY']


titles=[] # will contain the title 
descs=[] # will contain the description each item
links=[] # corresponding links will be stored here
dates=[] # each item's date will be stored in a particluar format

    
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


# for getting correct links
def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

#creating embed url 
def create_embed_link(pod_url):
    end=pod_url.partition('/episodes')
    final = end[0]+'/embed' +end[1] + end[2]
    return final



@app.route('/') #default root route
@cross_origin()
def home():
    result={"message":"Welcome to the unofficial anchor.fm API built to test endpoints"}

    return jsonify(result)



@app.route('/path/<path:rss_url>')
@cross_origin()
def index(rss_url):

    rss=rss_url

    parser= feedparser.parse(rss)
    

    for i in range (len(parser.entries)):

        title=parser.entries[i].title # parse the title field 
        titles.append(title)
        
        date=parser.entries[i].published[5:16] # parse the date field
        dates.append(date)
        
        link=parser.entries[i].link # parse the link field  
        flink=create_embed_link(link)
        links.append(flink)
        
        desc=parser.entries[i].description # parse the description field  
        clean=cleanhtml(desc)
        f=" ".join(clean.split())
        descs.append(f)

    linksss=unique(links)

    #getting content in correct order before saving

    linksss.reverse()
    titles.reverse()
    descs.reverse()
    dates.reverse()


    len1=len(linksss)

    #storing data of each podcast in results
    results=[]

    for i in range(len1):
        result={"episode":i ,"iframelink":linksss[i],"title":titles[i],"description":descs[i],"date_of_publishing":dates[i]}
        results.append(result)
    # print(results)
    return jsonify(results)

if __name__=='__main__':
    app.run(debug=False) 
