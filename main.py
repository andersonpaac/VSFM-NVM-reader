import argparser.parser as arg

fname =""
threshold_freq = 10

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
    featured =[]
    locations = []
    for each in data:
        analyze = each.rstrip().split(" ")
        if analyze[6]>threshold_freq:
            featured.append(each)
            locations.append({})
            locations[-1]["Index"]=analyze[7]
            locations[-1]["X"]=analyze[9]
            locations[-1]["Y"]=analyze[10]
    print len(featured)
    print locations[0]


def main():
    global fname
    parser = arg.args()
    fname = parser.parse_args().filename
    if fname == "":
        print "Please provide input filename with the -f"
        exit(-1)
    getfile()
main()
