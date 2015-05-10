__author__ = 'asc-mbp'
import argparser.parser as arg
import axis.functions as kris
import structures.Point as classes
import math
import numpy as np
outf=""
fname =""
threshold_freq = 0
width = 4000
height = 3000
def getfile():
    global fname
    fd = open(fname)
    data = fd.readlines()
    fd.close()
    parse(data)

def parse(data):
    numcams = int(data[2])
    numpoints = int(data[numcams+4])
    data = data[numcams+5:numpoints+numcams+5]
    featured = classes.Space()
    for each in data:
        featured.addtospace(each)
    findoptimal(featured)

def findoptimal(space):
    space.validateboxes()
    bools = {}
    validkeys = space.validkeys
    #for each in space.validkeys:
        #bools[each[0]]={}
        #bools[each[0]][each[1]] = canLand(space.boxes[each[0]][each[1]])

    #print space.boxes[validkeys[0][0]][validkeys[0][1]]
    for i in xrange(len(validkeys)):
        if validkeys[i][0] in bools:
            if validkeys[i][1] in bools[validkeys[i][0]]:
                bools[validkeys[i][0]][validkeys[i][1]].append(canLand(space.boxes[validkeys[i][0]][validkeys[i][1]]))
                #if bools[validkeys[i][0]][validkeys[i][1]] == [False]:
               #     print validkeys[i][0],validkeys[i][1]
            else:
                bools[validkeys[i][0]][validkeys[i][1]] = [canLand(space.boxes[validkeys[i][0]][validkeys[i][1]])]
                #if bools[validkeys[i][0]][validkeys[i][1]] == [False]:
                 #   print validkeys[i][0],validkeys[i][1]

        elif validkeys[i][0] not in bools:
            bools[validkeys[i][0]] = {}
            bools[validkeys[i][0]][validkeys[i][1]] = [canLand(space.boxes[validkeys[i][0]][validkeys[i][1]])]
            #if bools[validkeys[i][0]][validkeys[i][1]] == [False]:
             #   print validkeys[i][0],validkeys[i][1]



    #print kris.axis_rotate((0,-1,0),"z",25)

    for each in bools.keys():
        for every in bools[each].keys():
            if bools[each][every] == [True]:
                drawfrombox(each,every,space,"true",str(each)+"_"+str(every))
            else:
                drawfrombox(each,every,space,"false",str(each)+"_"+str(every))

    #print bools


#Draws by default the 0th point -> 3 images
def drawfrombox(X,Y,space,truth="",target=""):
    feature( space.boxes[X][Y][0][3].features , truth , target=target)

def canLand(pointarray):        #pointarray is an array of arrays.
    zs = []
    for each in pointarray:
        zs.append(each[2])
    return model_standard_deviation(zs)



def model_standard_deviation(zarray):
    THR_STD = 2
    if np.std(np.array(zarray)) < THR_STD:
        return True
    else:
        return False



# 3 images
def feature(SIFTFeatures,truth,target):
    path = "../assets/"
    ded = min(1,len(SIFTFeatures))
    for i in xrange(ded):
        picmid = str(SIFTFeatures[i].index).zfill(8)+".jpg"
        kris.mark_on_picture(path+picmid , SIFTFeatures[i].x , SIFTFeatures[i].y,truth,target)
        print "Wrote to  :"+picmid + " truth"


def calibrate(featured):
    X={}        #indices which have the floor (key is floor)
    Y={}
    Z={}
    i=0
    for each in featured:
        divs = each.split(" ")
        key_x = int(math.floor(float(divs[0])))
        key_y = int(math.floor(float(divs[1])))
        key_z = int(math.floor(float(divs[2])))
        if key_x in X:
            X[key_x].append(i)
        else:
            X[key_x]=[i]
        i = i+1
    N_X_Y = {}
    N_X_Z = {}
    #print X.keys()
    for each in X.keys():   #returns 0 , 1 , 2 ,3
        points = X[each]
        for i in xrange(len(points)):       #i=0,1,2,3
            divs = featured[points[i]].split(" ")
            key_y = int(math.floor(float(divs[1])))
            key_z = int(math.floor(float(divs[2])))
            #torem = points.remove(points[i])
            #print points
            for every in points:
                if every>=0:
                    divn = featured[every].split(" ")
                    key_cy = int(math.floor(float(divn[1])))
                    key_cz = int(math.floor(float(divs[2])))
                    if abs(key_cy-key_y)<1.5 and key_cy!=key_y: #and abs(key_cz-key_z)>2:
                        if each in N_X_Y:
                            N_X_Y[each].append(every)
                        else:
                            N_X_Y[each]=[every]
                    if abs(key_cz-key_z)<1.5 and key_cz!=key_z:
                        if each in N_X_Z:
                            N_X_Z[each].append(every)
                        else:
                            N_X_Z[each]=[every]


            #points.append(torem)


    jj=1
    print N_X_Y[jj]
    print "\n"
    print featured[N_X_Y[jj][0]]
    print "\n"
    print featured[N_X_Y[jj][1]]

def writeto(locations):
    global outf
    a = open(outf,"wb")
    a.write(str(locations))
    a.close()


def main():
    global fname,outf
    parser = arg.args()
    fname = parser.parse_args().filename
    outf = parser.parse_args().out
    if fname == "":
        print "Please provide input filename with the -f"
        exit(-1)
    getfile()
main()



'''
Standard Deviation model:
    pointed out rooftops , high elevation buildings , pointed out walls

'''