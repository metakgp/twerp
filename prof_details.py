import requests
import json
def get_all_info_of_faculty():
    r=requests.get("https://hercules-10496.herokuapp.com/api/v1/faculty/info/all")
    info_table=r.json()
    return info_table
def get_table_of_prof(faculty_name,department_code):
    r=requests.get("https://hercules-10496.herokuapp.com/api/v1/faculty/timetable?name={}&dept={}".format(faculty_name,department_code))
    timetable=r.json()
    return timetable