import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
#import os
#os.environ['HTTP_PROXY'] = 'http://yourproxy.server.com'

doc = parse(u)
for pt in doc.findall('.//pt'):
    print(pt.text)