import math
import numpy as np

#input a(x,y,z), b(x,y,z) (2points) tuple values (array) in the area specified
#output:(boolean) can land or not
def determine(point_array):
    #finds the decline between two points in 3d space. returns angle of decline in degrees
    
    def incline((x1,y1,z1),(x2,y2,z2)):
    	flag = 0
        if z2 > z1 :
            numerator = z2 - z1
            flag = 0
        else:
        	numerator = z1 - z2
        	flag = 1
        denominator = ((x2-x1)**2 + (y2-y1)**2)**2
        theta = math.atan(numerator/denominator)
        return (math.degrees(theta),flag)

    def median(arr):
    	arr = sorted(arr)
    	if len(arr) < 1:
    		return -1
    	elif len(arr)%2 == 1:
    		return arr[len(arr)/2]
    	else:
    		return arr[(len(arr)/2)-1]

    #median of the points would give you a central height
    x_vals = []
    y_vals = []
    z_vals = []

    for each in point_array:
    	x_vals.append(point_array[0])
    	x_vals.append(point_array[1])
    	z_vals.append(point_array[2])
    central = median(z_vals)
    central_index = z_vals.index(central)

    #compare each point with the central point
    incline_data = []

    for each in point_array:
    	incline_data.append(incline(point_array[central_index],each))

    print incline_data

    #best fit line for xz
    best_fit_xz = np.polyfit(x_vals, z_vals, 1, full=True)
    slope_xz = best_fit_xz[0][0]

    #best fit line for yz        
	best_fit_yz = np.polyfit(y_vals, z_vals, 1, full=True)
    slope_yz = best_fit_yz[0][0]
    