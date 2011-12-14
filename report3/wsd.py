#! /usr/bin/env python

from urllib import urlopen, urlencode, urlretrieve
import re
from sys import argv, exit

def getSequenceDiagram( text, outputFile, style = 'default' ):
    request = {}
    request["message"] = text
    request["style"] = style
    request["apiVersion"] = "1"

    url = urlencode(request)

    f = urlopen("http://www.websequencediagrams.com/", url)
    line = f.readline()
    f.close()

    expr = re.compile("(\?(img|pdf|png|svg)=[a-zA-Z0-9]+)")
    m = expr.search(line)

    if m == None:
        print "Invalid response from server."
        return False

    urlretrieve("http://www.websequencediagrams.com/" + m.group(0),
            outputFile )
    return True

if len(argv) != 3:
	print "usage: wst.py <input.wsd> <output.{pdf,svg,png}>"
	exit(2)

style = "qsd"
text = open(argv[1],'r').read()
pngFile = argv[2]

if getSequenceDiagram(text, pngFile, style):
	exit(0)
else:
	exit(-1)
