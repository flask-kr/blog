import os
import urllib, urllib2, re
from bs4 import BeautifulSoup

url = "http://webtoon.daum.net/webtoon/view/mimelasplendens"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

imgs = soup.findAll("img")
title = soup.find_all("script", text=re.compile('data1.push'))

#print imgs
print "title : ", title[1]


full_url = []
name = []

#for t in title:
#    if title[

for image in imgs:
    if image["src"].lower().startswith("http://i1.cartoon.daumcdn.net"):
        image_url = image["src"]
        image_name = image["src"].split("/")[-1]
        # print image_name
        joinurl = "".join(image_url)
        joinname = "".join(image_name)

        full_url.append(joinurl)
        name.append(joinname)
        # imgurl = image["src"]
        # urllib.urlretrieve(image["src"], os.path.basename(imgurl))
# print full_url
# print name
# make_image = zip(name, full_url)
#print make_image

# print make_image
# num =1
# for n, v in make_image:
# #    print n
#     res = urllib2.urlopen(v)
#     file = open("/home/ubuntu/blog/blog/gethtml/image/" + str(num) +".jpg" , 'wb')
#     file.write(res.read())
#     file.close()
#     num += 1

# for img in imgs:
#     print img.split("imgurl=")[1]
