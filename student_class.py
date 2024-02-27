class Student():
    '''define to to ver'''
    roll = ""
    gpa = ""

    def valu_add(self, r, g):
        '''in this function use to added to velu'''
        self.roll = r
        self.gpa = g

    def display(self):
        '''display the valu'''
        print(f"Roll is:{self.roll}, gpa:{self.gpa}")


    
#create a object in student class
python = Student()
python.valu_add(1, 5.6)
python.display()

#create another object in student class
javascript = Student()
javascript.valu_add(2, 3.4)
javascript.display()



