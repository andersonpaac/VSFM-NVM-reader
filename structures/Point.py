import axis.functions as kris
WIDTH = 4000
HEIGHT = 3000
class Point:
	AXIS = "z"
	THETA = -25
	THR_FREQ = 0        #Threshold Frequency
	FREQUENCY = 6		#index for frequency

        def __init__(self,data="",x=0,y=0,z=0):
		if x!=0:
			self.x , self.y , self.z = kris.axis_rotate((x,y,z),self.AXIS,self.THETA)
		
		else:
			analyze = data.rstrip().split(" ")
			if int(analyze[self.FREQUENCY]) > self.THR_FREQ:
					x , y ,z  = float(analyze[0]) , float(analyze[1]) , float(analyze[2])
					self.x , self.y , self.z = kris.axis_rotate((x,y,z),self.AXIS,self.THETA)
					self.features = [] 		#Array of SIFTFeatures
					i = 7
					for every in xrange(int(analyze[self.FREQUENCY])):
						self.features.append(SIFTFeature(analyze[i:i+4]))
						i = i+4
        def __str__(self):
            return str({"X":self.x,"Y":self.y,"Z":self.z,"Images":self.features})

class SIFTFeature:

    def __init__(self,data):
		self.index = int(data[0])
		self.feature = int(data[1])
		self.x = float(data[2]) + WIDTH/2
		self.y = float(data[3]) + HEIGHT/2

