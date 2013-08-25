import datetime
import ephem

tle=[]
x=0
with open('tleupdate.txt') as l:
	for i,n in enumerate(l):
		if x==0:
			if 'SRMSAT' in n:
				tle.append(n)
				x=i
		else:
			tle.append(n)
		if len(tle)==3:
			break

#print tle[0], tle[1], tle[2]

gs=ephem.Observer()
gs.lat=13.064103
gs.lon=80.218753

while True:
#	gs.date=datetime.datetime.now()+datetime.timedelta(0,700)
	gs.date=datetime.datetime.now()
	sat=ephem.readtle(tle[0],tle[1],tle[2])
	sat.compute(gs)
	print sat.az, sat.alt


