#from aptTest import userInfo
#import string
import aptTest.userInfo
import aptTest.question
import aptTest.analsys

'''
print("Please input your information below(ex: name, sex, and age):");
userName = input("Name:");
userSex = input("Sex(Male or Female):");
userAge = int(input("Age(Number only):"));

user = aptTest.userInfo.userInfo(userName,userSex, userAge);
'''

user = aptTest.userInfo.userInfo();
questions = aptTest.question.questions("question.json");
analsys = aptTest.analsys.analsys("result.json");
#user.getUserInfo();

print("qnum:%d" % questions.getQuestionNum());

# list questions and collect the user input
for i in range(0, questions.getQuestionNum()):
    questions.getQuestion(i);
    questions.setAnswer(i);

# list all result
'''
for j in range(0, questions.getQuestionNum()):
    questions.getAnswer(j);
'''

result = analsys.aptAlgo(questions.getReportArray());
print("Your test result is: %s" % result);
#analsys.getCountResult();
analsys.getFinalResult(result);

# Below code is for local result test
'''
analsys = aptTest.analsys.analsys("result.json");
analsys.getFinalResult(["I","S","T","P"]);
'''
