import json

class questions:
    def __init__(self, filename="question.json"):
        with open(filename) as f:
                self.data = json.load(f);

    def getQuestionNum(self):
        return len(self.data["questions"]);

    def getQuestion(self, index):
        print("Q%d. %s" % (index+1, self.data["questions"][index]["questionDesc"]));
        print("    a. %s" % self.data["questions"][index]["selectionA"]);
        print("    b. %s" % self.data["questions"][index]["selectionB"]);

    def getReportArray(self):
        return self.data["questions"];

    def setAnswer(self, index):
        ans = input("Input your answer: ");
        while ans != "a" and ans != "b":
            ans = input("Data invalid, please your answer again(a or b): ");

        self.data["questions"][index]["answer"] = ans;

    def getAnswer(self, index):
        print("(%d) %s" % (index+1, self.data["questions"][index]["answer"]));

    
