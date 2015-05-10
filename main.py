import argparser.parser as arg
import axis.functions as kris
import structures.Point as classes
import math

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
    locations = []
    #a=0
    for each in data:
        featured.addtospace(each)

    z_cpy = featured.z
    z_cpy.sort()
    #print z_cpy[len(z_cpy)/2]
    #print z_cpy
    print featured.boxes[-17][-7]
    featured.validateboxes()
    print featured.boxes.keys()

def feature(loc):
    path = "../assets/"
    for i in xrange(3):
        picmid = str(loc["Index"][i]).zfill(8)+".jpg"
        kris.mark_on_picture(path+picmid,loc["X"][i],loc["Y"][i])
    

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
