class My_class():
    '''define tow variables'''
    name = ''
    color = ''


    def __init__(self, nam, clr):
        self.name = nam
        self.color = clr

    def disply(self):
        '''disply the output this function'''
        print(f"Name: {self.name}\nColor: {self.color}")


#Createa a object
create_object = My_class("Nerov","Black and white")

#call the disply method
create_object.disply()



    