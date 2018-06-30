import json

class analsys:
    def __init__(self, filename="result.json"):
        self.introversion = 0;
        self.extroversion = 0;

        self.sensing = 0;
        self.intuition = 0;

        self.thinking = 0;
        self.feeling = 0;

        self.judging = 0;
        self.perceiving = 0;

        self.ret = [];

        with open(filename) as f:
                self.data = json.load(f);

    def aptAlgo(self, reportArray):
        totalNum = len(reportArray);
        for index in range(0, len(reportArray)):
            i = reportArray[index]["index"];
            ans = reportArray[index]["answer"];

            # introverstion counter
            if ( i == "2" and ans == "a" ) or \
                ( i == "6" and ans == "a" ) or \
                ( i == "11" and ans == "a" ) or \
                ( i == "15" and ans == "b" ) or \
                ( i == "19" and ans == "b" ) or \
                ( i == "22" and ans == "a" ) or \
                ( i == "27" and ans == "b" ) or \
                ( i == "32" and ans == "b" ):
                self.introversion += 1;
            elif ( i == "2" and ans == "b" ) or \
                ( i == "6" and ans == "b" ) or \
                ( i == "11" and ans == "b" ) or \
                ( i == "15" and ans == "a" ) or \
                ( i == "19" and ans == "a" ) or \
                ( i == "22" and ans == "b" ) or \
                ( i == "27" and ans == "a" ) or \
                ( i == "32" and ans == "a" ):
                self.extroversion += 1;
            elif ( i == "1" and ans == "b" ) or \
                ( i == "10" and ans == "b" ) or \
                ( i == "13" and ans == "a" ) or \
                ( i == "16" and ans == "a" ) or \
                ( i == "17" and ans == "a" ) or \
                ( i == "21" and ans == "a" ) or \
                ( i == "28" and ans == "b" ) or \
                ( i == "30" and ans == "b" ):
                self.sensing += 1;
            elif ( i == "1" and ans == "a" ) or \
                ( i == "10" and ans == "a" ) or \
                ( i == "13" and ans == "b" ) or \
                ( i == "16" and ans == "b" ) or \
                ( i == "17" and ans == "b" ) or \
                ( i == "21" and ans == "b" ) or \
                ( i == "28" and ans == "a" ) or \
                ( i == "30" and ans == "a" ):
                self.intuition += 1;
            elif ( i == "3" and ans == "a" ) or \
                ( i == "5" and ans == "a" ) or \
                ( i == "12" and ans == "a" ) or \
                ( i == "14" and ans == "b" ) or \
                ( i == "20" and ans == "a" ) or \
                ( i == "24" and ans == "b" ) or \
                ( i == "25" and ans == "a" ) or \
                ( i == "29" and ans == "b" ):
                self.thinking += 1;
            elif ( i == "3" and ans == "b" ) or \
                ( i == "5" and ans == "b" ) or \
                ( i == "12" and ans == "b" ) or \
                ( i == "14" and ans == "a" ) or \
                ( i == "20" and ans == "b" ) or \
                ( i == "24" and ans == "a" ) or \
                ( i == "25" and ans == "b" ) or \
                ( i == "29" and ans == "a" ):
                self.feeling += 1;
            elif ( i == "4" and ans == "a" ) or \
                ( i == "7" and ans == "a" ) or \
                ( i == "8" and ans == "b" ) or \
                ( i == "9" and ans == "a" ) or \
                ( i == "18" and ans == "b" ) or \
                ( i == "23" and ans == "b" ) or \
                ( i == "26" and ans == "a" ) or \
                ( i == "31" and ans == "a" ):
                self.judging += 1;
            else:
                self.perceiving +=1;
        #print(totalNum);


        if self.introversion > self.extroversion:
            self.ret.append("I");
        elif self.introversion < self.extroversion:
            self.ret.append("E");
        else:
            if reportArray[index]["index"] == "11" and reportArray[index]["answer"] == "a":
                self.ret.append("E");
            else:
                self.ret.append("I");

        if self.sensing > self.intuition:
            self.ret.append("S");
        elif self.sensing < self.intuition:
            self.ret.append("N");
        else:
            if reportArray[index]["index"] == "16" and reportArray[index]["answer"] == "a":
                self.ret.append("N");
            else:
                self.ret.append("S");

        if self.thinking > self.feeling:
            self.ret.append("T");
        elif self.thinking < self.feeling:
            self.ret.append("F");
        else:
            if reportArray[index]["index"] == "24" and reportArray[index]["answer"] == "b":
                self.ret.append("F");
            else:
                self.ret.append("T");

        if self.judging > self.perceiving:
            self.ret.append("J");
        elif self.judging < self.perceiving:
            self.ret.append("P");
        else:
            if reportArray[index]["index"] == "23" and reportArray[index]["answer"] == "b":
                self.ret.append("P");
            else:
                self.ret.append("J");

        return self.ret;

    def getCountResult(self):
        print("(I)introversion: %d" % self.introversion);
        print("(E)extroversion: %d" % self.extroversion);

        print("(S)sensing: %d" % self.sensing);
        print("(N)intuition: %d" % self.intuition);

        print("(T)thinking: %d" % self.thinking);
        print("(F)feeling: %d" % self.feeling);

        print("(J)judging: %d" % self.judging);
        print("(P)perceiving: %d" % self.perceiving);

    def getFinalResult(self, result):
        # print left, top, right, bottom description
        for leftKey in self.data["resultType"]["leftPresPos"]:
            if leftKey["abbreviation"] == result[0]:
                print("%s\n%s\n" % (leftKey["type"], leftKey["description"]));
                
        for rightKey in self.data["resultType"]["rightPresPos"]:
            if rightKey["abbreviation"] == result[3]:
                print("%s\n%s\n" % (rightKey["type"], rightKey["description"]));
                
        for topKey in self.data["resultType"]["topPresPos"]:
            if topKey["abbreviation"] == result[1]:
                print("%s\n%s\n" % (topKey["type"], topKey["description"]));

        for bottomKey in self.data["resultType"]["bottomPresPos"]:
            if bottomKey["abbreviation"] == result[2]:
                print("%s\n%s\n" % (bottomKey["type"], bottomKey["description"]));

        # convert result list to String
        resultStr = ''.join(result);

        # search the key title and print the description from resultList
        for checkMatch in self.data["resultList"]:
            if resultStr == checkMatch["title"]:
                print("%s\n%s\n" % (checkMatch["title"], checkMatch["description"]));
                break;

