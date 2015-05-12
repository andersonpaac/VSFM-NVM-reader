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
