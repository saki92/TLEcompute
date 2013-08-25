import datetime
import ephem

tle=[]
with open('tledata.txt') as l:
	for line in l:
		tle.append(line)
#print tle[1]


gs=ephem.Observer()
gs.lat=13.064103
gs.lon=80.218753

while True:
#	gs.date=datetime.datetime.now()+datetime.timedelta(0,700)
	gs.date=datetime.datetime.now()
	sat=ephem.readtle(tle[0],tle[1],tle[2])
	sat.compute(gs)
	print sat.az, sat.alt


