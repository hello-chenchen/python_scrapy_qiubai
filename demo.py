#encoding: UTF-8
#a python demo
import urllib
import datetime
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?<h2>(.*?)</h2>.*?content">\n\n(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            timeStamp = float(item[2])
            # float(timeStamp)
            dateArray = datetime.datetime.fromtimestamp(timeStamp)
            otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
            #print item[0],item[1],otherStyleTime,item[4],item[5]
            print "\n\n作者:%s\n内容:%s时间:%s\n赞:%s\n评论:%s\t"%(item[0],item[1],otherStyleTime,item[4],item[5])
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason