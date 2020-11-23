class Person:

    def __init__(name, address):
        self.__name = name
        self.__address = address
    
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def setAddress(self):
        self.__address = address

    def toString(self):
        return f"{self.__name}({self.__address})"

class Student(Person):

    def __init__(self, name, address, numCourses=0, courses=[], grades=[]):
        self.__numCourses = numCourses
        self.__courses = courses
        self.__grades = grades
        super().__init__(name, address)

    def addCourseGrade(self, course, grade):
        self.__courses.append(course)
        self.__grades.append(grade)

    def printGrades(self):
        print(self.__grades)

    def getAverageGrade(self):
        return (sum(self.__grades)/len(self.__grades))

    def toString(self):
        return f"Student: {self.__name}({self.__address})"

class Teacher(Person):
    def __init__(self, name, address, numCourses=0, courses = []):
        self.__numCourses = numCourses
        self.__courses = courses
        super().__init__(name, address)

    def addCourse(self, course):
        for i in self.__courses:
            if course in self.__courses:
                return False
            else:
                self.__courses.append(course)

    def removeCourse(self, course):
        if course in self.__courses:
            self.__courses.remove(course)
        else:
            return False

    def toString(self):
        return f"Teacher: {self.__name}({self.__address})"


