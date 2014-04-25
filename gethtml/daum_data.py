# -*- coding:utf-8 -*-
import requests
import os
import json
import urllib, urllib2, re
from bs4 import BeautifulSoup


url = "http://webtoon.daum.net/webtoon/view/mimelasplendens"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)
main_title_image = soup.find("div", {"class" : "wrap_image"}).find('img')['src']


############ daum data #############

### refined_data
### 0: title_image_url 
### 1:chapter 
### 2:detail_url 
### 3:date 
### 4:main_title 
### 5:main_title_image
### 6:identify_no

daum_data = soup.find_all("script", text=re.compile('data1.push'))
main_title = soup.find("title").contents
temp_1 = []
temp_2 =[]
refined_data = []
data = []
for item in daum_data:
	for line in item.text.split('data1.push'):
		if line.startswith('({img'):
			data.append(line) 

del data[-1]
for list in range(len(data)):
	comp = data[list].split(",")
	for i in range(len(comp)):
		temp_1.append(comp[i].split("\""))
		temp_2.append(temp_1[i][1])
	refined_data.append(temp_2)
	temp_1 = []
	temp_2 = []

for item in refined_data:
	del item[5:9]
	del item[2]
	item.append(main_title[0])
	item.append(main_title_image)
	identify_no = item[2].split("/")[-1]
	item.append(identify_no)

daum_url = "http://webtoon.daum.net"
for i in range(len(refined_data)):
	refined_data[i][2] = daum_url + refined_data[i][2]


########### Get & Save detail_image_url ##############
# detail_url = refined_data[0][2]
# img_headers = {
# 	"Host": "webtoon.daum.net",
# 	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0",
# 	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
# 	"Accept-Laguage": "ko-kr,ko;q=0.8,en-us;q=0.5,en;q=0.3",
# 	"Accept-Encoding": "gzip, deflate",
# 	"charset": "utf-8",
# 	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
# 	"Referer": detail_url,
# 	"Content-length": "0",
# 	"Cookie": "WEBTOON_VIEW=MTAuMTA%3D; TIARA=rUyhKvuQti6BIOHC-WjC4jJC4zbEEVwoD9e3r5-KlpJIphm1GMKzKL1gT-rk2YtnuIiljLKXkEZsS8ep7a3-lA00; VOTE=MTAuMTA%3D",
# 	"Connection": "keep-alive",
# 	"Pragma": "no-cache",
# 	"Cache-Control": "max-age=0"
# }

# for d in refined_data: 
# 	d_num = 1
# 	detail_path = "/home/jacks/blog/blog/web/static/images/daum/detail/" + d[1]
# 	if not os.path.exists(detail_path):
# 		os.makedirs(detail_path)
# 		r = requests.post("http://webtoon.daum.net/webtoon/viewer_images.js?webtoon_episode_id="+d[6], headers=img_headers)
# 		detail_data = json.loads(r.text)

# 		for img in detail_data['images']:
# 			print detail_data['episodeTitle']
# 			detail_name = detail_data['episodeTitle'] + "_" + str(d_num)
# 			d_num	+= 1
# 			try:
# 				res = urllib2.urlopen(img['url'])
# 				d_file = open(detail_path + "/" + detail_name +".jpg" , 'wb')
# 				d_file.write(res.read())
# 				d_file.close()
# 			except urllib2.HTTPError as e:
# 				print "HTTP error: %d" % e.code
# 			except urllib2.URLError as e:
# 				print "Network error: %s" % e.reason.args[1]
# 	d_num = 0

########## Save title_image ########
# title_path = "/home/jacks/blog/blog/web/static/images/daum/title"
# if not os.path.exists(title_path):
# 	os.makedirs(title_path)

# for v in refined_data:
# 	title_name = "title_" + v[1]
# 	try:
# 	res = urllib2.urlopen(v[0])
# 	t_file = open(title_path + "/" + title_name +".jpg" , 'wb')
# 	t_file.write(res.read())
# 	t_file.close()
# 	except urllib2.HTTPError as e:
# 		print "HTTP error: %d" % e.code
# 	except urllib2.URLError as e:
# 		print "Network error: %s" % e.reason.args[1]