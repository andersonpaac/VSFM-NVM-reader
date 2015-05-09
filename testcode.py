import axis.functions as rotate
import os

index=26
fname = "../../assets/00000000.jpg"
x0=1830
y0=1992
x1=2041
y1=2062
x2=1773
y2=1941
fname1 = "../../assets/00000173.jpg"
fname2 = "../../assets/00000001.jpg"
def main():
    #os.mkdir("../../compiled/"+str(index))
    #rotate.mark_on_picture(fname,x0,y0,"../../assets/"+fname[-10:-4]+"_out.png")
    #rotate.mark_on_picture(fname1,x1,y1,"../../assets/"+fname1[-10:-4]+"_out.png")
    #rotate.mark_on_picture(fname2,x2,y2,"../../assets/"+fname2[-10:-4]+"_out.png")
    print rotate.axis_rotate((10.08,22.84,8.96),"z",16)
    print rotate.axis_rotate((13.046,23.199,9.460),"z",16)
    s0 = (14.910,20.409,10.167)
    s1 = (11.234,18.725,9.779)
    '''
    diffs =[]
    for i in xrange(0,100):
        a,b,c = rotate.axis_rotate(s0,"z",-i)
        d , e , f = rotate.axis_rotate(s1,"z",-i)
        diffs.append(abs(b-e))
    
    print min(diffs),diffs.index(min(diffs))
    '''
    print rotate.axis_rotate((20.981,4.276,14.768),"z",-25)
    print rotate.axis_rotate((14.046,19.739,10.116),"z",-25)
main()

