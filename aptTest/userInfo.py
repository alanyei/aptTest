class userInfo:
    def __init__(self, name="Test", sex="Male", age=18):
        "Initial the user information"
        self.name = name;
        self.sex = sex;
        self.age = age;

    def getUserInfo(self):
        print("Name: %s" % self.name);
        print("Sex : %s" % self.sex);
        print("Age : %d years old" % self.age);

    def getUserName(self):
        return self.name;

    def getUserSex(self):
        return self.sex;

    def getUserAge(self):
        return self.age;

#user1 = userInfo("Alan", "Male", 34);
#user1.listUserInfo();
