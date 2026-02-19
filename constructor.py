class employee:
    language = "python"
    salary = 1200000

    def_init_(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning")

    
    harry = employee("Harry",1300000,"Java script")
    print(harry.name,harry.salary,harry.language)
        