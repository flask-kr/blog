# -*- coding:utf-8 -*-
import os
import urllib, urllib2, re
from bs4 import BeautifulSoup

url = "http://webtoon.daum.net/webtoon/view/mimelasplendens"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

imgs = soup.findAll("img")
title = soup.find_all("script", text=re.compile('data1.push'))

#print imgs
#print "title : ", title
list_title = []
for item in title:
	for line in item.text.split('data1.push'):
		# print line
		# print '-'* 40
		if line.startswith('({img'):
			list_title.append(line) 

del list_title[-1]
# for l in list_title:
# 	print l
# 	print '='*40

comp = list_title[0].split(",")
a = []
b =[]
c = []
# for c in comp:
# 	print c
# 	print '='*40

for i in range(len(comp)):
	a.append(comp[i].split("\""))
	# print comp[i].split("\"")
	print a[i][1]
	print '='*40
	b.append(a[i][1])

print b
# print a
# print b
# print c




#print "list_title : ",list_title

	#raw_input()
# print type(title)

# title_split = title[0].split('data1.push')

# print title_split








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
