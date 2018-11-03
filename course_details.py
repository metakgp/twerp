import requests

def getDeptList():
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
    return courseData

if __name__ == '__main__':
    getCourseData({'code': 'CS60092'})
    #main()