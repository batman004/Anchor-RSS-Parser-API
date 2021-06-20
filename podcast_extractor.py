from flask import Flask,jsonify,request
from flask_cors import CORS,cross_origin
import feedparser
import lxml.html
import lxml.html.clean
import os
import re

app=Flask(__name__)
CORS(app)
app.config["SECRET_KEY"]=os.environ['SECRET_KEY']

# rss_url= 'https://anchor.fm/s/3c55a5f0/podcast/rss'
# rss_url='https://anchor.fm/s/27fb166c/podcast/rss'
rss_url='https://anchor.fm/s/91b81a0/podcast/rss'

titles=[]
descs=[]
links=[]
dates=[]

    
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


@app.route('/')
@cross_origin()
def index():



    parser= feedparser.parse(rss_url)
    

    for i in range (len(parser.entries)):

        title=parser.entries[i].title

        titles.append(title)
        date=parser.entries[i].published[5:16]
        cnt=0
        dates.append(date)
        link=parser.entries[i].link
        flink=create_embed_link(link)
        links.append(flink)
        desc=parser.entries[i].description
        clean=cleanhtml(desc)
        f=" ".join(clean.split())
        descs.append(f)


    # https://anchor.fm/oijpcr/embed/episodes/OIJPCR-Dialogue-Part-1-e10i67m
    # sample href link = f'https://anchor.fm/{name}/embed/episodes/{title}-{id}'
    # for podcast author title with more than one word, we need to put '-' between each word. ex : DSC VIT becomes dsc-vit, OIJPCR becomes oijpcr
    # for title put '-' between each word. OIJPCR Dialogue Part 1  becomes OIJPCR-Dialogue-Part-1'
    # add id at the end : OIJPCR-Dialogue-Part-1-e10i67m'



    
    linksss=unique(links)

#getting content in correct order

    linksss.reverse()
    titles.reverse()
    descs.reverse()
    dates.reverse()


    len1=len(linksss)

#storing data of each podcast
    results=[]

    for i in range(len1):
        result={"episode":i ,"iframelink":linksss[i],"title":titles[i],"description":descs[i],"date_of_publishing":dates[i]}
        results.append(result)
    # print(results)
    return jsonify(results)

if __name__=='__main__':
    app.run(debug=False) 
