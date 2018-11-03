import requests
import time
#from twerp import twerpUpdate

def getDept():
    r = requests.get('https://hercules-10496.herokuapp.com/api/v1/department/info/all')
    #departments = {}
    departments = r.json()
    return departments

def getCoursesDeptWise(deptCode):
    r = requests.get('https://hercules-10496.herokuapp.com/api/v1/course/info/department/{0}'.format(deptCode))
    courses = {}
    courses = r.json()
    return courses

def getCourseData(course):
    r = requests.get('https://hercules-10496.herokuapp.com/api/v1/course/timetable/{0}'.format(course['code']))
    courseData = r.json()
    print(courseData)
    return courseData

#def twerp():

def main():
    departments = getDept()
    for department in departments:
        courses = getCoursesDeptWise(department['code'])
        for course in courses:
            courseData = getCourseData(course)
            #twerp(courseData)
            print(courseData)
            time.sleep(0.5)            

if __name__ == '__main__':
    getCourseData({'code': 'CS60092'})
    #main()