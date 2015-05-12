import argparser.parser as arg
import axis.functions as kris
import structures.Point as classes
import math
import numpy as np
import glob


golden={0: {0: [True], 1: [False], 2: [False], 3: [True], 4: [False], 5: [False], 6: [True], 8: [False], 9: [False], 10: [False], 18: [False], -2: [True], -30: [False], -29: [True], -28: [True], -21: [False], -20: [False], -19: [False], -17: [False], -15: [True], -14: [False], -11: [False], -9: [False], -7: [False], -6: [False], -5: [True], -4: [True], -3: [True], -1: [True]}, 1: {0: [True], 1: [True], 2: [True], 3: [False], -31: [False], 9: [False], 10: [False], -21: [False], -20: [False], -13: [False], -12: [False], -1: [True], -9: [False], -7: [False], -6: [False], -5: [False], -4: [True], -3: [True], -2: [True]}, 2: {0: [True], -31: [False], 2: [True], 10: [False], 9: [False], -22: [False], -21: [False], -20: [False], -14: [False], -10: [False], -9: [False], -8: [False], -7: [False], -6: [False], -5: [False], -4: [True], -3: [True], -2: [True]}, 3: {27: [False], 26: [False], 9: [False], -22: [False], -21: [False], 10: [True], -14: [False], -12: [False], -10: [False], -9: [False], -8: [False], -7: [False], -6: [False], -5: [False], -4: [True], -3: [True], -2: [True]}, 4: {11: [True], 37: [False], 10: [True], -23: [False], -22: [False], -21: [False], -15: [False], 26: [False], -9: [False], -8: [False], -7: [False], -6: [False], -5: [False], -4: [True], -3: [True], -2: [True]}, 5: {27: [False], -24: [False], -23: [False], -22: [False], -21: [False], 20: [True], -11: [False], -10: [False], -9: [False], -8: [False], -7: [False], -6: [False], -5: [True], -4: [True], -3: [True], -2: [True]}, 6: {0: [True], -31: [False], 35: [False], 36: [False], -23: [False], 10: [True], -1: [True], 27: [True], -22: [False], -29: [True], 20: [True], -11: [False], -10: [False], -7: [False], -6: [False], -5: [True], -4: [True], -3: [True], -2: [True]}, 7: {18: [False], 19: [True], 23: [True], 24: [True], 36: [True], -1: [True], -29: [False], -28: [False], -24: [False], -23: [False], -22: [False], -21: [False], -11: [False], -10: [False], -9: [False], -8: [False], -7: [False], -6: [False], -5: [False], -4: [True], -3: [True], -2: [True]}, 8: {18: [True], 19: [False], 20: [False], 21: [False], 22: [False], 23: [False], 25: [True], 26: [True], 34: [True], 35: [True], 36: [False], 38: [True], -1: [True], -26: [False], -24: [False], -23: [False], -22: [False], -20: [False], -12: [False], -11: [False], -10: [False], -9: [False], -8: [False], -7: [False], -6: [False], -5: [False], -4: [False], -3: [True], -2: [True]}, 9: {10: [False], 17: [True], 18: [True], 19: [False], 20: [False], 21: [False], 22: [False], 23: [False], 24: [False], 30: [True], 35: [True], 36: [False], 37: [True], -25: [False], -24: [False], -23: [False], -22: [False], -17: [False], -13: [False], -11: [False], -10: [False], -9: [False], -8: [False], -7: [False], -4: [False]}, 10: {11: [False], 18: [True], 19: [False], 20: [False], 21: [False], 22: [False], 23: [False], 24: [True], 30: [False], 36: [True], 37: [True], -29: [False], -26: [False], -25: [False], -24: [False], -23: [False], -22: [False], -13: [False], -10: [False], -9: [False], -8: [False], -6: [False], -5: [False], -4: [False], -2: [True]}, 11: {11: [False], 12: [False], 16: [True], 18: [True], 19: [True], 20: [False], 21: [False], 22: [False], 23: [False], 34: [False], 35: [False], 36: [False], -25: [False], -24: [False], -23: [False], -13: [False], -12: [False], -11: [False], -10: [False], -9: [False], -8: [False], -7: [False], -6: [False], -5: [False], -4: [False], -1: [True]}, 12: {0: [True], 12: [False], 18: [True], 19: [False], 20: [False], 21: [False], 22: [False], 23: [False], 31: [True], 33: [False], 34: [True], 35: [False], 38: [True], -26: [False], -25: [False], -24: [False], -23: [False], -20: [False], -19: [False], -13: [False], -12: [False], -11: [False], -10: [False], -9: [False], -6: [False], -5: [False], -4: [False], -2: [True]}, 13: {0: [True], 14: [False], 18: [True], 19: [True], 20: [True], 21: [False], 33: [False], 37: [False], -27: [False], -26: [False], -25: [False], -24: [False], -23: [False], -12: [False], -11: [False], -10: [False], -9: [True], -8: [True], -7: [True], -6: [False], -5: [False], -4: [False], -3: [False]}, 14: {33: [False], 35: [True], 37: [False], -26: [False], -11: [False], -24: [False], -18: [False], 18: [True], 19: [True], 20: [True], 21: [True], -10: [False], -9: [False], -12: [False], -6: [False], -5: [True], -4: [False], -2: [True], -7: [True]}, 15: {0: [True], 15: [True], 19: [True], 20: [True], 21: [True], 22: [False], 31: [False], 34: [False], -28: [False], -27: [False], -26: [False], -24: [False], -13: [False], -12: [False], -11: [False], -10: [True], -8: [True], -7: [True], -5: [True], -4: [True], -3: [True], -2: [True]}, 16: {4: [False], 5: [False], 7: [False], 13: [True], 19: [True], 20: [True], 21: [True], 23: [True], -2: [True], -29: [False], -27: [False], -26: [False], -25: [False], -13: [False], -12: [True], -11: [True], -10: [False], -9: [True], -8: [True], -7: [True], -6: [True], -5: [True], -4: [True], -3: [True], -1: [False]}, 17: {0: [False], 3: [True], 4: [False], 5: [False], 6: [False], -2: [False], 11: [True], 15: [True], 22: [True], 23: [False], 24: [False], 25: [False], 31: [False], 34: [False], 35: [False], 36: [False], -27: [False], -26: [False], -25: [False], -15: [False], -14: [False], -13: [False], -12: [False], -11: [True], -10: [True], -9: [True], -8: [True], -7: [True], -5: [True], -4: [True], -3: [True], -1: [False]}, 18: {0: [False], 3: [True], 4: [False], 5: [False], 6: [False], -2: [True], 10: [True], 12: [True], 15: [True], 19: [True], 21: [True], 25: [False], 32: [True], -30: [False], -27: [False], -26: [False], -25: [False], -17: [False], -16: [False], -15: [False], -14: [False], -13: [False], -12: [False], -11: [True], -10: [True], -9: [True], -8: [True], -7: [True], -6: [True], -5: [True], -4: [True], -3: [True], -1: [False]}, 19: {0: [False], -30: [False], 3: [True], 4: [True], 5: [False], 7: [False], 9: [True], 11: [True], 13: [True], 20: [True], 33: [False], 34: [True], 35: [False], -28: [False], -27: [False], -21: [False], -20: [False], -19: [False], -18: [False], -17: [False], -16: [False], -15: [False], -14: [False], -13: [False], -12: [False], -11: [True], -10: [True], -9: [True], -8: [True], -7: [True], -4: [True], -3: [True]}, 20: {0: [False], 3: [True], 5: [False], 6: [False], 7: [True], 9: [True], 10: [True], 12: [True], 20: [True], 21: [True], 22: [False], 26: [False], -30: [False], -27: [False], -26: [False], -24: [False], -23: [False], -22: [False], -21: [False], -19: [False], -18: [False], -17: [False], -16: [False], -14: [False], -13: [False], -11: [True], -10: [True], -9: [True], -8: [True], -7: [True], -3: [True]}, 21: {0: [False], 1: [False], 2: [False], 5: [True], 6: [True], 9: [False], 12: [True], 20: [True], 21: [True], -30: [False], -28: [False], -27: [False], -24: [False], -23: [False], -18: [False], -15: [False], -14: [False], -13: [True], -11: [True], -10: [True], -9: [True], -8: [True], -7: [True], -1: [False]}, 22: {0: [False], 1: [False], 2: [False], 3: [False], 4: [False], 5: [True], 6: [True], 8: [False], 9: [False], -19: [False], 14: [True], -17: [False], -16: [False], -24: [False], 23: [True], -8: [True], -28: [False], -1: [False]}, 23: {32: [False], 34: [False], 3: [False], 4: [False], 5: [True], 7: [False], 8: [False], 9: [False], 10: [False], -25: [False], -20: [False], 13: [True], 35: [False], 25: [False], 26: [False], -1: [False], -29: [False]}, 24: {19: [True], 34: [False], 35: [False], 4: [False], 5: [False], 7: [False], 8: [False], 9: [False], 10: [False], 11: [False], 12: [False], 3: [False], 20: [True], -8: [True], 25: [False], 36: [False]}, 25: {0: [False], 1: [False], -30: [True], 35: [False], 36: [True], -25: [False], 8: [False], 9: [False], 10: [False], 19: [True], 20: [False], 21: [False], 22: [False], -9: [False], -8: [False], -7: [False], -1: [False]}, 26: {35: [False], -17: [False], 19: [False], 20: [False], 21: [False], 22: [False], -29: [False]}, 27: {35: [False], -26: [False], 18: [False], 19: [False], 20: [False], 21: [False]}, 28: {3: [False], 4: [False], 5: [False], 6: [False], 18: [False], 19: [False], -29: [False], 34: [False], 35: [False], -23: [False], -21: [False], -20: [False]}, 29: {0: [False], 1: [False], 2: [False], 3: [False], 4: [False], 5: [False], 6: [False], 7: [False], -20: [False], 17: [False], 18: [False], 19: [False], -11: [False], -9: [False], -13: [False], 35: [False], 21: [False]}, 30: {0: [False], 2: [False], 3: [False], 6: [False], 7: [False], 18: [False], 19: [False], 33: [False], -29: [False], -20: [False], -1: [False]}, 31: {0: [False], 1: [False], 2: [False], 4: [False], 6: [False], 11: [True], 28: [False], 34: [False], 35: [False], -2: [False], -1: [False]}, 32: {0: [True], 1: [False], -1: [False], 7: [False], 8: [False], 9: [False], 11: [False], -4: [False], -3: [False], -2: [False]}, 33: {0: [False], 1: [False], 7: [False], 8: [False], 10: [False], 11: [False], 12: [False], -29: [False], 33: [False], 34: [False], 35: [False]}, 34: {0: [False], 7: [False], 8: [False], 9: [False], 19: [False], 20: [True], 30: [False], 34: [True], 35: [False], 36: [True], -2: [False]}, 35: {1: [False], 34: [False], 19: [False], 36: [True], 31: [False], 18: [False], 30: [False], 29: [False]}, 36: {0: [False], 1: [False], 2: [False], 3: [False], 4: [False], 17: [False], 18: [False], 20: [False], 29: [False], 30: [False], 31: [False], 34: [False], 35: [False]}, 37: {0: [False], 17: [False], 34: [False], 19: [False], 30: [False], 10: [False], 29: [False], -1: [False]}, 38: {-30: [False], 15: [False], 16: [False], 17: [False], 18: [False], 19: [False]}, 39: {17: [False], 18: [False], 19: [False], 20: [False], 15: [False]}, 40: {16: [False], 17: [False], 18: [False], 35: [False], -27: [False], -26: [False], -25: [False], -24: [False], 15: [True]}, 41: {16: [False], 17: [False], 18: [False], 20: [False], 30: [False], 34: [False], 35: [False], -27: [False], -13: [False], -12: [False], -11: [False], -10: [False], -8: [False], -6: [False]}, 42: {16: [False], 33: [False], 34: [False], 28: [False], 31: [False]}, 43: {16: [False], 17: [False], 18: [False], 30: [False], 24: [False]}, 44: {16: [False], 17: [False], 19: [False], 13: [True]}, 45: {17: [False], 26: [False]}, 46: {19: [False]}, 49: {25: [False]}, 51: {26: [False]}, 56: {20: [False]}, 57: {19: [False]}, 58: {27: [False]}, -1: {0: [False], 1: [False], 2: [False], 3: [False], 7: [True], 9: [False], 10: [False], -20: [False], -19: [False], -16: [False], 20: [False], -2: [True], -9: [False], -8: [False], -6: [True], -5: [True], -4: [True], -3: [True], -1: [True]}, -17: {7: [True]}, -15: {5: [False]}, -11: {-6: [False]}, -10: {2: [True], -6: [False], -5: [False], -4: [True], -3: [False], -1: [False]}, -9: {0: [False], -2: [False], -5: [False], -4: [False], -3: [False], -1: [False]}, -8: {0: [True], 1: [True], 2: [True], -3: [False], -2: [True]}, -7: {0: [True], 1: [True], 2: [False], 3: [False], 4: [False], -3: [False], -4: [False], -19: [False], -1: [False], -13: [False]}, -6: {0: [True], 1: [True], 2: [True], 3: [False], 4: [False], 8: [True], 16: [False], -21: [False], -20: [False], -19: [False], -2: [False], -4: [False], -1: [True]}, -5: {0: [True], 1: [True], 2: [True], 3: [True], 14: [False], -19: [False], -1: [False], -9: [False], -6: [False], -4: [False], -3: [True], -2: [True]}, -4: {0: [True], 1: [True], 2: [False], 7: [False], -30: [False], -20: [False], -19: [False], -2: [True], -9: [False], -6: [False], -3: [True], -1: [True]}, -3: {0: [True], 1: [False], 2: [False], 3: [False], 4: [False], -20: [False], 13: [False], 14: [False], -19: [False], -2: [True], -10: [False], -6: [False], -5: [True], -4: [True], -3: [True], -1: [True]}, -2: {0: [True], 1: [False], 2: [False], 3: [False], -2: [True], -20: [False], 13: [False], -18: [False], -19: [False], 21: [False], -10: [False], -8: [False], -5: [True], -4: [True], -3: [True], -1: [True], -11: [False]}}

outf=""
fname =""
threshold_freq = 0
width = 4000
height = 3000
aggression = 8  #0=conservative(less spots) , 1=less conservative , 2= less agression , 3....8=Very aggressive (more spots)
contextualthresh = 2
rights = []
wrongs = []
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
    global golden
    space.validateboxes()
    bools = {}
    validkeys = space.validkeys
    for i in xrange(len(validkeys)):
        if validkeys[i][0] in bools:
            x = validkeys[i][0]
            y = validkeys[i][1]
            if validkeys[i][1] in bools[validkeys[i][0]]:

                bools[validkeys[i][0]][validkeys[i][1]].append(canLand(space.boxes[validkeys[i][0]][validkeys[i][1]],space,x,y))
                #if bools[validkeys[i][0]][validkeys[i][1]] == [False]:
               #     print validkeys[i][0],validkeys[i][1]
            else:
                bools[validkeys[i][0]][validkeys[i][1]] = [canLand(space.boxes[validkeys[i][0]][validkeys[i][1]], space , validkeys[i][0] , validkeys[i][1])]
                #if bools[validkeys[i][0]][validkeys[i][1]] == [False]:
                 #   print validkeys[i][0],validkeys[i][1]

        elif validkeys[i][0] not in bools:
            bools[validkeys[i][0]] = {}
            bools[validkeys[i][0]][validkeys[i][1]] = [canLand(space.boxes[validkeys[i][0]][validkeys[i][1]] ,space , validkeys[i][0] , validkeys[i][1])]
            #if bools[validkeys[i][0]][validkeys[i][1]] == [False]:
             #   print validkeys[i][0],validkeys[i][1]
    metrics(bools,space)

def metrics(bools,space):
    correct=0.0
    errors = 0.0
    trueland=0.0
    global golden , contextualthresh , rights
    landspot = 0
    for each in bools:
        for every in bools[each]:
            if bools[each][every] == [True]:
                landspot = landspot+1.0
            if bools[each][every] == [True] and golden[each][every]==[True]:
                #drawfrombox(each,every,space,"true",str(each)+"_"+str(every))
                trueland = trueland+1.0
            if bools[each][every]!=golden[each][every] and bools[each][every]==[True]:
                errors=errors+1.0


            else:
                correct = correct+1.0
    '''
    print "Error percentage is "+str(float(errors/(errors+correct))*100)
    print "Found " +str(landspot)+" Landing Spots"
    #print "Wrong false is "+str(wrongfalse*100/errors)
    #print "Wrong True is "+str(wrongtrue*100/errors)
    '''
    print "\n--------------"+str(contextualthresh)
    if errors+trueland!=0:
        print "Wrong True is "+str(errors*100/(errors+trueland))+"%"
        print "Correct landing spots are " +str(trueland*100/(errors+trueland))+"%"
    else:
        print "Correct landing spots are 0 %"
    print "Found "+str(landspot)+" Landings"
    print "\n--------------"
    #print rights
    #print wrongs


#One time training
def readfx(bools):
    print bools[-4][-6]
    true_data = glob.glob("../true_fx/*")
    for each in true_data:
        x , y = int(each.split("_")[-3]),int(each.split("_")[-2])
        bools[x][y] = [False]

    false_data = glob.glob("../false_fx/*")
    for each in false_data:
        x , y = int(each.split("_")[-3]),int(each.split("_")[-2])
        bools[x][y] = [True]

    print dict(bools)



#Draws by default the 0th point -> 3 images
def drawfrombox(X,Y,space,truth="",target=""):
    feature(space.boxes[X][Y][0][3].features , truth , target=target)

def canLand(pointarray,space,x,y):        #pointarray is an array of arrays.
    zs = []
    for each in pointarray:
        zs.append(each[2])


    a =  model_standard_deviation_2(zs,space,x,y)
    #if a==True:
    #    print x,y
    return a


#Standard deviation with NVM
def model_standard_deviation_2(zarray,space,x,y):
    global aggression , golden , rights , wrongs
    rt_thr = 8 - aggression
    THR_STD = 2
    arr = []


    if min(zarray) > space.getfloor():
        rt0 = 0
        if y+1 in space.boxes[x]:
            rt1 ,g= canstand(space.boxes[x][y+1],space,np.std(np.array(zarray)))
            rt0 = rt0 + rt1
            arr.append(g)
        if y-1 in space.boxes[x]:
            rt2,g = canstand(space.boxes[x][y-1],space,np.std(np.array(zarray)))
            rt0=rt0+ rt2
            arr.append(g)

        if x+1 in space.boxes[x] and y in space.boxes[x+1]:
            rt3,g = canstand(space.boxes[x+1][y],space,np.std(np.array(zarray)))
            rt0 = rt0+ rt3
            arr.append(g)

        if x+1 in space.boxes and y+1 in space.boxes[x+1]:
            rt4,g = canstand(space.boxes[x+1][y+1],space,np.std(np.array(zarray)))
            rt0=rt0+rt4
            arr.append(g)

        if x+1 in space.boxes and y-1 in space.boxes[x+1]:
            rt5 ,g  = canstand(space.boxes[x+1][y-1],space,np.std(np.array(zarray)))
            rt0 = rt0 + rt5
            arr.append(g)

        if x-1 in space.boxes and y-1 in space.boxes[x-1]:
            rt6 ,g= canstand(space.boxes[x-1][y-1],space,np.std(np.array(zarray)))
            rt0 = rt0 + rt6
            arr.append(g)
        if x-1 in space.boxes and y in space.boxes[x-1]:
            rt7,g = canstand(space.boxes[x-1][y],space,np.std(np.array(zarray)))
            rt0 = rt0 + rt7
            arr.append(g)

        if x-1 in space.boxes and y+1 in space.boxes[x-1]:
            rt8,g = canstand(space.boxes[x-1][y+1],space,np.std(np.array(zarray)))
            rt0=rt0 + rt8
            arr.append(g)

        #print rt0
        if rt0>=rt_thr and np.mean(np.array(arr))<space.getfloor()+contextualthresh:
            if golden[x][y]==[True]:
                rights.append(arr)
            if golden[x][y]==[False]:
                wrongs.append(arr)
            return True
        else:
            return False


    else:
        return False

def canstand(pointarray,space,stddev):        #pointarray is an array of arrays.
    zs = []
    for each in pointarray:
        zs.append(each[2])
    return only_standard(zs,space,stddev)

def only_standard(zarray,space,stddev):
    THR_STD = 2
    global contextualthresh

    if min(zarray) > space.getfloor():
        return 1 , np.median(np.array(zarray))

    else:
        return -999,np.median(np.array(zarray))

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
    global fname,outf,contextualthresh
    parser = arg.args()
    fname = parser.parse_args().filename
    outf = parser.parse_args().out
    if parser.parse_args().thresh != "":
        contextualthresh = float(parser.parse_args().thresh)
    if fname == "":
        print "Please provide input filename with the -f"
        exit(-1)
    getfile()
main()



'''

Standard Deviation model:
    pointed out rooftops , high elevation buildings , pointed out walls , pointed out right next to
    Z                       z                           z
'''

