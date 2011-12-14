#! /usr/bin/env python

import urllib
import re
from sys import argv

def getSequenceDiagram( text, outputFile, fmt, style = 'default' ):
    request = {}
    request["message"] = text
    request["style"] = style
    request["apiVersion"] = "1"
    request["format"] = fmt

    url = urllib.urlencode(request)

    f = urllib.urlopen("http://www.websequencediagrams.com/", url)
    line = f.readline()
    f.close()

    expr = re.compile("(\?(img|pdf|png|svg)=[a-zA-Z0-9]+)")
    m = expr.search(line)

    if m == None:
        print "Invalid response from server."
        return False

    urllib.urlretrieve("http://www.websequencediagrams.com/" + m.group(0),
            outputFile )
    return True


style = "qsd"
fmt = argv[1]
text = open(argv[2],'r').read()
pngFile = argv[3]

getSequenceDiagram(text, pngFile, fmt, style)
