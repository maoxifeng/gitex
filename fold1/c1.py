# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 21:40:46 2017

@author: xun
"""




class Person(object):
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print 'Hello, world! I am %s.'%self.name
    def gree(self):
        print 'Hello, world! I am %s.'% self.getName()    

		
class Student1(object):
    count = 0
    books = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
    pass

class Student2():
    count = 0
    books = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
    pass

class Student3:
    count = 0
    books = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
    pass

#%%
#Student.books.extend(["python", "javascript"])  
#print "Student book list: %s" %Student.books    
## class can add class attribute after class defination
#Student.hobbies = ["reading", "jogging", "swimming"]
#print "Student hobby list: %s" %Student.hobbies    
#print dir(Student)






