import os
import urllib, urllib2, re
from bs4 import BeautifulSoup

url = "http://webtoon.daum.net/webtoon/viewer/24400"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

imgs = soup.findAll("img")

full_url = []
name = []

for image in imgs:
    if image["data-src"].lower().startswith("http://i1.cartoon.daumcdn.net"):
        image_url = image["data-src"]
        image_name = image["data-src"].split("/")[-1]
        # print image_name
        joinurl = "".join(image_url)
        joinname = "".join(image_name)

        full_url.append(joinurl)
        name.append(joinname)
        # imgurl = image["src"]
        # urllib.urlretrieve(image["src"], os.path.basename(imgurl))
# print full_url
# print name
make_image = zip(name, full_url)

# print make_image

for n, v in make_image:
    print n
    res = urllib2.urlopen(v)
    file = open("image/" + n +".jpg" , 'wb')
    file.write(res.read())
    file.close()

# for img in imgs:
#     print img.split("imgurl=")[1]