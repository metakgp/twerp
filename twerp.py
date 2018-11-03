import pywikibot
from pywikibot import pagegenerators
import time
import re
import os
path = os.path.abspath(os.path.dirname(__file__))

from course_details import getDeptList,getCourseData,getCoursesDeptWise
from time_table_to_wiki_table import getTimeTable

def updateCourseTimeTable(data):
    #print(data)
    timetable = getTimeTable(data)
    if len(timetable) != 0:
        print (timetable)
    #return


def course_details():
    departments = getDeptList()
    for department in departments:
        print('Updating time table for courses from the department : ' + department['name'])
        courses = getCoursesDeptWise(department['code'])
        for course in courses:
            print(course['code'] + ' : ' + course['name'])
            updateCourseTimeTable( getCourseData(course) )

            #print(courseData)
            time.sleep(0.5)            


def main():
    course_details()    

if __name__ == '__main__':
    main()