import urllib2
import sys
import json
import gzip
from StringIO import StringIO

template = """	<a href="http://security.stackexchange.com/users/53583/limbenjamin" title="Security.SE">
      <div style="border:1px solid black;padding:0.2em;display:inline-block;">
        <i class="fa fa-shield fa-lg"></i> Security.SE<br />
        <b>{rep}</b><br />
        <i style="font-size:0.8em;color:goldenrod;width:inherit;" class="fa fa-circle fa-lg"></i> {gold} 
		<i style="font-size:0.8em;color:silver;width:inherit;" class="fa fa-circle fa-lg"></i> {silver} 
		<i style="font-size:0.8em;color:brown;width:inherit;" class="fa fa-circle fa-lg"></i> {bronze} 
      </div>
	</a>
""" 
req = urllib2.Request("http://api.stackexchange.com/2.2/users/3728754/associated")
req.add_header('Accept-encoding', 'gzip')
resp = urllib2.urlopen(req)
if resp.info().get('Content-Encoding') == 'gzip':
    buf = StringIO( resp.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
else:
  data = resp.read()
jsondata = json.loads(data)
f = open('flair.html', 'w')
context = {
 "rep": jsondata["items"][4]["reputation"], 
 "gold": jsondata["items"][4]["badge_counts"]["gold"],
 "silver": jsondata["items"][4]["badge_counts"]["silver"],
 "bronze" : jsondata["items"][4]["badge_counts"]["bronze"]
 }
f.write(template.format(**context))
