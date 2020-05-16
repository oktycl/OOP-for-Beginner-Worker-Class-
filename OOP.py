

""""Object Oriented For BEGINNER."""



"""firstly we should class because object is in classes"""

""" class name_of_class("parameter"):
    
        we should add common properties of class thiss area 
       
        
 """
  #"this function is construction function,so it run firstly"
 # "we use SELF,because it means your object,for example
  
 #we use these classes ,we will create objects.      
        
class worker: 
    #"my all worker class,it include manager,engineer,and chief"

    def __init__(self,name,surname,salary):        
        self.name=name                  
        self.surname=surname
        self.salary=salary
    def status(self):
         print(self.name)
         print(self.surname)
         print(self.salary)

class engineer(worker):       #we can add some properties,so overwriting.(add which graduation year )
    
    def __init__(self,name,surname,salary,year):
        super().__init__(name,surname,salary)  #youn can not again same init values with SUPER funtion
        #super function take values in worker class
        self.year=year 
    
    def status(self):    
     super().status()
     print(self.year) #aded new properties
     print("I check slab reinforcements")

class manager(worker):
    
    def __init__(self,name,surname,salary,experience):
        super().__init__(name,surname,salary) #again use super function,we got rid of writing again.:)
        self.experience=experience #overwrite
        
    def status(self):
        super().status()
        print(self.experience)
        print("I check workers on the site.")

class chief(worker):
    
    def __init__(self,name,surname,salary):
        super().__init__(name,surname,salary)
        #"we can not use overwrite.
        
    def status(self):
        super().status()
        print("I will not go to site.")
        
        
        
#"we add some person in class"

man=manager("OKTAY","YÜCEEL",12000,5) #new person
man.status()
print()       
eng=engineer("KAZIM","KAZIM",4500,2016) #New person
eng.status() 
print()
chief=chief("BERAT","ALİ",7500) #New person
chief.status()    
       