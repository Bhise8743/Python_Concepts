"""

@Author: Omkar Bhise

@Date: 2023-12-07 03:00:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-07 03:30:00

@Title :  Logging In the employee

"""


import logging

logging.basicConfig(filename="employee.log",level=logging.INFO,
                    format='%(levelname)s:%(message)s')
class Employee:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

        logging.info(f'Create Employee: {self.full_name()}  and Email : {self.email()}')

    def full_name(self):
        return f"{self.fname} {self.lname}"

    def email(self):
        return f"{self.lname}{self.fname}@gmail.com"


e1 = Employee("Omakr" ,"Bhise")
e2 = Employee("sham","Raut")
e3 = Employee("Rameshwar", "Joshi")