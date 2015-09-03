import serial


class GpsModule (object):
	def __init__(self, port = '/dev/ttyUSB1', baudrate = 9600, time = 1):
		self.baudrate = baudrate
		self.timeout = time
		self.port = port
		self.open=serial.Serial(self.port, self.baudrate, timeout=self.timeout)
		
	def getGPS (self):
		line = self.open.readline()
		while line[4]!='G': #it has to be $GPGGA
			line = self.open.readline()
		if line[4]=='G':
			line = line.split(",")
			lati = line[2]
			longi = line[4]
		latitude=float(lati)
		longitude=float(longi)		
		return [latitude, longitude] #should probably add hemisphere info

	def getOGI (self): #over ground information
		line = self.open.readline()
		while line[3]!='R': #it has to be $GPRMC
			line = self.open.readline()
		if line[3]=='R':
			line=line.split(",")
			sog=line[7]
			cog=line[8]
		speedog=float(sog)		
		courseog=float(cog)		
		return [speedog, courseog] 

	def getAzimuth (self): 
		line = self.open.readline()
		while line[5]!='V':
			line = self.open.readline()
		if line[5]=='V':
				line=line.split(",")
				numbers=line[1]
				numbers = int(numbers)
				line = self.open.readline()

		i=0
		azim=[]
		azimuth=[]
		
		while i<numbers:
			while (line[5]!='V') or (line[9]!=str(i+1)): #it has to be $GPGSV
				line = self.open.readline()
			if line[5]=='V' and line[9]==str(i+1):
				line = line.split(",")
				azim.append(line[6])
				azimuth.append(int(azim[i]))
				line = self.open.readline()
				i=i+1				
		return azimuth


