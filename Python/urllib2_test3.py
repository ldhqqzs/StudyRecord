from urllib2 import Request, urlopen, URLError, HTTPError

req = Request('http://www.anotherhome.net/testurl')

try:
    response = urlopen(req)

except HTTPError, e:
    print "The server couldn't fulfill the request."
    print 'Error code:', e.code

except URLError, e:
    print 'We failed to reach a server'
    print 'Reason:', e.reason

else:
    print 'No exception was raised.'