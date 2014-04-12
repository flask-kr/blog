# -*- coding: cp949 -*-
 
import re, sys, urllib2
 
# get img url in html
def recompile(html):
    exp_title = re.compile(r'<img.+?src="(http://thumb\.comic\.naver\.net/webtoon/335885/thumbnail/(.+?\.(jpg|png|gif)))".*?>')
    title_image = exp_title.findall(html)

    return title_image

# main
def extract_images():
    html = f.read()
    f.close()

    imgs = recompile(html)

    if len(imgs) == 0:
        print >> sys.stderr, "No images!"
        return imgs

    for img in imgs:
        print "here0"
        print img[0] # full link
        print "here1"
        print img[1] # file name
        print "here2"
        print img[2] # extension
 
    return imgs
