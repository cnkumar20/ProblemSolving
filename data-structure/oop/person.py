class Person:
    def __init__(self,name="",age="",dob="",ethnic=""):
        self.name=name
        self.age=age
        self.dob=dob
        self.ethnic=ethnic
    def toString(self):
        print(self.name)
        print(self.age)
        print(self.dob)
        print(self.ethnic)
if __name__=="__main__":
    person = Person(name="Nandiesh",age=30,dob="06/04/1988",ethnic="Indian")
    person.toString()
