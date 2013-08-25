import urllib2

resp=urllib2.urlopen("http://celestrak.com/NORAD/elements/resource.txt")
tledata=resp.read()
f=open("tleupdate.txt",'w')
f.write(tledata)
f.close
