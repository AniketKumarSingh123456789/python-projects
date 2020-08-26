import urllib,urllib2
url = "https://api.msg91.com/api/sendhttp.php"
values = {
    'authkey':"281817ABV1LRzJt5d0a30e2",
    'mobiles':"+917992389665",
    'message':"This message is sent by python",
    'sender':"SOCKET",
    'route':"4",
}
postdata = urllib.urlencode(values)
req = urllib2.Request(url,postdata)
response = urllib2.urlopen(req)
output = response.read()
print output