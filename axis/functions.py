#input: (x,y,z,axis,theta)
#output: (x,y,z) rotated
#theta must be in radians
#axis must be "x", "y", or "z"

import math


def axis_rotate((x,y,z),axis,theta,radians=0):
    if radians==0:
        theta = math.radians(theta)
    axis = axis.upper()
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    (x_hat, y_hat, z_hat) = (-1,-1,-1)
    if axis == "X":
        #rotate around x axis
        y_hat = (y*cos_t)-(z*sin_t)
        z_hat = (y*sin_t)+(z*cos_t)
        x_hat = x        
        
    elif axis == "Y":
        #rotate around y axis
        z_hat = (z*cos_t)-(x*sin_t)
        x_hat = (z*sin_t)+(x*cos_t)
        y_hat = y
        
    elif axis == "Z":
        #rotate around z axis
        x_hat = (x*cos_t)-(y*sin_t)
        y_hat = (x*sin_t)+(y*cos_t)
        z_hat = z
            
    else:
        print "Please specify axis"
        return -1
    return (x_hat,y_hat,z_hat)
