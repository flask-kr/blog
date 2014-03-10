# -*- coding: cp949 -*-
 
import re, sys, urllib2
 
# get img url in html
def recompile(html):
    # exp_value = re.compile(r'<img.+?src="(http://imgcomic\.naver\.net/webtoon/[0-9]+/[0-9]+/(.+?\.(jpg|png|gif)))".*?>')
    # exp_title = re.compile(r'<img.+?src="(http://thumb\.comic\.naver\.net/webtoon/[0-9]+/thumbnail/(.+?\.(jpg|png|gif)))".*?>')

    #compile title
    exp_title = re.compile(r'<img.+?src="(http://thumb\.comic\.naver\.net/webtoon/335885/thumbnail/(.+?\.(jpg|png|gif)))".*?>')
    #compile value
    title_image = exp_title.findall(html)
    # value_image = exp_value.findall(html)

    return title_image

# main
def extract_images():
    # url = { 
    #     'denma' : ['http://comic.naver.com/webtoon/detail.nhn?titleId=119874', 
    #             'http://comic.naver.com/webtoon/detail.nhn?titleId=119874&no=656'],
    #     'gaus' : ['http://comic.naver.com/webtoon/detail.nhn?titleId=335885', 
    #             'http://comic.naver.com/webtoon/detail.nhn?titleId=335885&seq=656'],
    # }

    # for k,v in url.iteritems():
    #     value += [v]
    # #path is list[0] = title, list[1] = view
    # path =  [[row[i] for row in value] for i in range(len(url.keys()))]

    # image = []

    # for v in len(path)
    #     f = urllib2.urlopen(path[type_value][v])
    #     html = f.read()
    #     f.close()

    #     title, value = recompile(html)
    #     image_path += imgs[0]

    f = urllib2.urlopen('http://comic.naver.com/webtoon/detail.nhn?titleId=335885')
    html = f.read()
    f.close()

    imgs = recompile(html)
    # image_path += imgs[0]

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
