from datetime import date

class Student:

    def __init__(self,stu_id,name,dob,classification):
        self.__id = stu_id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = None
        self.__register = None
    
    def calc_age(self):
        today = date.today()
        # year = today.year
        x = self.__dob.split('/')
        x_year = int(x[-1])
        self.__age = today.year - x_year

        # self.age = int(dob_list[-1]) - year
    
    def calc_register(self):
        if self.__classification == "senior":
            self.__register = "4/1 thru 4/3"
        elif self.__classification == "junior":
            self.__register = "4/4 thru 4/6"
        elif self.__classification == "sophomore":
            self.__register = "4/7 thru 4/9"    
        elif self.__classification == "freshmen":
            self.__register = "4/10 thru 4/12"
        else:
            self.__register = 'classification not found'

    def get_age(self):
        return self.__age
    
    def get_register(self):
        return self.__register