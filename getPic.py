import os
import re
import requests

f = open('src.txt', 'r')
html = f.read()
f.close()

pic_url = re.findall('src="(http.*?)"', html, re.S)
for i in pic_url:
    print "now downloading:" + i
    pic = requests.get(i)
    (filepath,tempfilename) = os.path.split(i)
    (shotname,extension) = os.path.splitext(tempfilename)
    fp = open('pic/' + shotname + extension, 'wb')
    fp.write(pic.content)
    fp.close()