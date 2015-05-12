import axis.functions as kris
import math
import numpy as np

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

class Space:
    BOXSIZE = 1         #How big is each box
    VALID_SIZE = 2      #Number of points needed for each box to be valid
    boxes = {}
    validkeys = []
    invalidkeys = []
    def __init__(self):
        self.z = []
        self.space = []     #Array of point

    def addtospace(self,data):
        self.space.append(Point(data))
        self.z.append(self.space[-1].z)
        self.addtobox()
        self.printed=0

    # (-1 , 1) belong to "0"
    def addtobox(self):
        x = int(self.space[-1].x)
        y = int(self.space[-1].y)
        x_box = x / self.BOXSIZE
        y_box = y / self.BOXSIZE
        if x_box not in self.boxes:
            self.boxes[x_box] = {}
            self.boxes[x_box][y_box] = [[self.space[-1].x,self.space[-1].y,self.space[-1].z,self.space[-1]]]

        if x_box in self.boxes:
            if y_box not in self.boxes[x_box]:
                self.boxes[x_box][y_box] = [[self.space[-1].x,self.space[-1].y,self.space[-1].z,self.space[-1]]]
            else:
                self.boxes[x_box][y_box].append([self.space[-1].x,self.space[-1].y,self.space[-1].z,self.space[-1]])

    def validateboxes(self):
        for each in self.boxes.keys():
            for every in self.boxes[each].keys():
                if len(self.boxes[each][every]) > self.VALID_SIZE:
                    self.validkeys.append([each,every])
                else:
                    self.invalidkeys.append([each,every])

    def getfloor(self):
        if self.printed==0:
            print  "median is",np.median(np.array(self.z))
            self.printed=1
        return np.median(np.array(self.z))


    def printboxes(self):
        print self.boxes






#Constant altitude
#Variant boxes
#HDOP - Altitude , satkey