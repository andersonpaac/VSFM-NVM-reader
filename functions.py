#input: (x,y,z,axis,theta)
#output: (x,y,z) rotated
#theta must be in radians
#axis must be "x", "y", or "z"

import math


def axis_rotate((x,y,z),axis,theta):
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    if axis == "x" or axis == "X":
        #rotate around x axis
        x_hat = 
    elif axis == "y" or axis == "Y":
        #rotate around y axis
    elif axis == "z" or axis == "Z":
        #rotate around z axis
            
    else:
        print "Please specify axis"
        return (None,None,None)
