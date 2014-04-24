# -*- coding:utf-8 -*-
import os
import urllib, urllib2, re
from bs4 import BeautifulSoup

url = "http://webtoon.daum.net/webtoon/view/mimelasplendens"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

imgs = soup.findAll("img")


############ main_title ##############
# main_title = soup.find("title").contents

############# daum data #############

## refined_data
## 0: title_image_url 1:chapter 3:detail_url 4:date

# daum_data = soup.find_all("script", text=re.compile('data1.push'))
# temp_1 = []
# temp_2 =[]
# refined_data = []
# data = []
# for item in daum_data:
# 	for line in item.text.split('data1.push'):
# 		if line.startswith('({img'):
# 			data.append(line) 

# del data[-1]
# for list in range(len(data)):
# 	comp = data[list].split(",")
# 	for i in range(len(comp)):
# 		temp_1.append(comp[i].split("\""))
# 		temp_2.append(temp_1[i][1])
# 	refined_data.append(temp_2)
# 	temp_1 = []
# 	temp_2 = []

# for item in refined_data:
# 	print item
# 	print '-'*40

######## big title image ########

# full_url = []
# name = []
# for image in imgs:
#     if image["src"].lower().startswith("http://i1.cartoon.daumcdn.net"):
#         image_url = image["src"]
#         image_name = image["src"].split("/")[-1]
#         joinurl = "".join(image_url)
#         joinname = "".join(image_name)

#         full_url.append(joinurl)
#         name.append(joinname)
#         # imgurl = image["src"]
#         # urllib.urlretrieve(image["src"], os.path.basename(imgurl))

# make_image = zip(name, full_url)

# num =1
# for n, v in make_image:

#     res = urllib2.urlopen(v)
#     file = open("/home/ubuntu/blog/blog/gethtml/image/" + str(num) +".jpg" , 'wb')
#     file.write(res.read())
#     file.close()
#     num += 1

# for img in imgs:
#     print img.split("imgurl=")[1]
