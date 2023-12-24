"""

@Author: Omkar Bhise

@Date: 2023-12-07 03:00:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-07 03:30:00

@Title :  Logging Basic

"""
"""
loggi
import logging
logging.debug("hi I am here ")
logging.info("your looking some one ")
logging.warning("this is warning for you ")
logging.error("Your error is make trouble ")
logging.critical("seriously are his is critical ")


"""
"""
basicConfig()
commnly used parameter 
1 level : the root logger will be set to the specified severity level.
2. filename : the specified in the finename 
3. filemode : If file name is given , the file is opened in this mode 
              The default is a, Which means append mode , w : Write mode 
4. format : this is the format of the log message .

"""
# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This will get logged ")

# import logging
#
# logging.basicConfig(filename="app.log", filemode='w', format='%(name)s - %(levelname)s %(message)s')
# logging.warning('This will get logged to file ')


# Formatting the output
# import logging
# logging.basicConfig(format = '%(process)d - %(levelname)s - %(message)s')
# logging.warning('This is warning ')


# we are adding time and date
# import logging
# logging.basicConfig(format='%(asctime)s - %(message)s', level = logging.INFO)
# logging.info('Admin logged in ')


import logging
log_format = '{lineno}  {name}  '
logging.basicConfig(filename='base_log.log',level=logging.DEBUG,filemode='w',style='{')
"""
Logging levels 
1 DEBUG : Detailed information, typically of interest only when diagnosing problem .
2. INFO : Conformation that the things are working as expected 
3. WARNING : An indication that something unexpected happened, or indicative of some problem 
             in the near future (e.g. 'diskspace low'). The software is still working as expected.
             
4. ERROR : Due to a more serious problem, the software has not been able to perform some function.
5. CRITICAL : A serious error, indicating that the program itself may be unable to continue running .
"""



"""
import logging


logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')


def addition(a,b):
    return a+b


def multiplication(a,b):
    return a*b


def division(a,b):
    return a/b


def substraction(a,b):
    return a-b


num1 = 10
num2 = 5
add_res = addition(num1,num2)
logging.debug(f"addition of {num1} and {num2} is {add_res}")
mul_res = multiplication(num1,num2)
logging.debug(f"Multiplication of {num1} and {num2} is {mul_res}")
div_res = division(num1,num2)
logging.debug(f"Division of {num1} and {num2} is {div_res}")
sub_res = substraction(num1,num2)
logging.debug(f"Subtraction of {num1} and {num2} is {sub_res}")

"""