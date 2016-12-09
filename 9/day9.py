import re

def main():
    inputfile = open("input")
    inputdata = inputfile.read()
    inputfile.close()


    regex = re.compile("(\d+x\d+)", re.UNICODE)
    data = regex.findall(inputdata)

    goodData = []

    for crypt in data: 
    	cryptdata = re.findall('\d+', crypt)
    	goodData.append([cryptdata[0], cryptdata[1]])


    cryptString = inputdata
    decryptString = ""
    while goodData != []:
        p1 = goodData[0]
        str =  "(" + p1[0] + "x" + p1[1] + ")"
	    #Get startpos of string
        pos = cryptString.find("(" + p1[0] + "x" + p1[1] + ")")

        startRepData = pos+3 + len(p1[0]) + len(p1[1])
        repData = cryptString[startRepData : startRepData+int(p1[0])]
        print repData

        for x in range(0, int(p1[1])):
            #repeat string
            decryptString += repData


	    #get no of data points in string
	    #print regex.findall(repData)
        noPoints = len(regex.findall(repData)) + 1
        print noPoints
        goodData = goodData[noPoints:]
        print goodData

    print len(decryptString)


if __name__ == "__main__":
    main()