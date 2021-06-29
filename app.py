from flask import Flask,jsonify,request
from flask_cors import CORS,cross_origin
import feedparser
import lxml.html
import lxml.html.clean

app=Flask(__name__)
#CORS(app)
app.config["SECRET_KEY"]="thisisasecretkeylezgo"

rss_url= 'https://anchor.fm/s/3c55a5f0/podcast/rss'

titles=[]
descs=[]
links=[]
dates=[]
    
@app.route('/')
@cross_origin()
def index():

    def cleanhtml(html):
        doc = lxml.html.fromstring(html)
        cleaner = lxml.html.clean.Cleaner(style=True)
        doc = cleaner.clean_html(doc)
        text = doc.text_content()
        return text

#for getting correct links
    def unique(sequence):
        seen = set()
        return [x for x in sequence if not (x in seen or seen.add(x))]



    parser= feedparser.parse(rss_url)
    
    for entry in parser.entries:
    
        title=entry.title
        titles.append(title)
        date=entry.published[5:16]
        dates.append(date)
        
        #generating iframe src

        src=entry.links[0].href
        indices = [0,25,len(src)]
        parts = [src[i:j] for i,j in zip(indices, indices[1:]+[None])]
        iframe_src=parts[0]+"/embed"+parts[1]
        links.append(iframe_src)
        desc=cleanhtml(entry.content[0].value)
        descs.append(desc)

    
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
        result={"episode":i ,"iframelink":linksss[i],"title":titles[i],"description":(descs[i]),"date_of_publishing":dates[i]}
        results.append(result)
        
    return jsonify(results)

if __name__=='__main__':
    app.run(debug=True) 
