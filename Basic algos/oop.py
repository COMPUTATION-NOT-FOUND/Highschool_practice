
class employee:
    def __init__(self,name,staffno):
        self.__name=name
        self.__staffno=staffno
        self.__fulltimestaff=True
    def showdetails(self):
        print("employee name" , self.__name)
        print("empployee number" , self.__staffno)
class partTime(employee):
    def __init__(self,name,staffno):
        super().__init__(name,staffno)
        self.__fulltimestaff=False
        self.__hoursworked=0
    def gethoursworked (self):
        return(self.__hoursworked)
class fullTime(employee):
    def __init__(self,name,staffno):
        employee.__init__(self,name,staffno)
        self.__fulltimestaff = True
        self.yearlysalary =0
    def getyralysalary(self):
        return(self.__yearlysalary)
permanentstaff=fullTime("eric jones",72)
permanentstaff.showdetails()
temporarystaff=partTime("alice hue",1017)
temporarystaff.showdetails()



