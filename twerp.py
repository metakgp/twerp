import pywikibot
from pywikibot import pagegenerators
import time
import re
import os
path = os.path.abspath(os.path.dirname(__file__))

def getSlotData(slotCodes):

    slots = []
    for slotCode in slotCodes:
        with open(os.path.join(path, 'slots.1')) as f:
            for line in f:
                if line.startswith(slotCode):
                    for slot in (line.split()[1:]):
                        if slot not in slots:
                            slots.append(slot)
    return (slots)


def getSlotCodes(data):
    slotCodes = []
    for day in data:
        #print (days)
        #print(type(data[day]))
        if(data[day] != None):
            for element in data[day]:
                if element['slot']['slot'] not in slotCodes:
                    slotCodes.append(element['slot']['slot'])

    slots  = getSlotData(slotCodes)
    return slots

def createTimeTableFromSlots(slots):
    timetable = []
    for i in range(5):
        dayWiseTimeTable = []
        for j in range(10):
            dayWiseTimeTable.append(0)
        timetable.append(dayWiseTimeTable)

    for hoursAndDay in slots:
        day = int(hoursAndDay[0])
        hour = int(hoursAndDay[1])
        if hour>4:
            hour = hour + 1
        timetable[day][hour] = /

    print(timetable)
    print(slots)

    return timetable


def getTimeTable(data):
    slots = getSlotCodes(data)
    timetable = createTimeTableFromSlots(slots)




def obtainCourseData():
    data ={'Monday': None, 'Tuesday': None, 'Wednesday': None, 'Thursday': [{'course': {'name': 'INFORMATION RETRIEVAL', 'code': 'CS60092', 'credits': 3}, 'slot': {'time': {'day': 'Thursday', 'time': '3 PM '}, 'slot': 'V3'}, 'rooms': ['CSE-120']}, {'course': {'name': 'INFORMATION RETRIEVAL', 'code': 'CS60092', 'credits': 3}, 'slot': {'time': {'day': 'Thursday', 'time': '4 PM '}, 'slot': 'V3'}, 'rooms': ['CSE-120']}], 'Friday': [{'course': {'name': 'INFORMATION RETRIEVAL', 'code': 'CS60092', 'credits': 3}, 'slot': {'time': {'day': 'Friday', 'time': '3 PM'}, 'slot': 'V3'}, 'rooms': ['CSE-120']}]}
    getTimeTable(data)


def UpdateCourses(site):
    cat = pywikibot.Category(site,'Category:Courses')
    gen = pagegenerators.CategorizedPageGenerator(cat)

    allcourses = {i.title()[:7]:i for i in gen}

    course_page = allcourses['CS60092']
    wiki_text = course_page.text

    #course_page.text = wiki_text + 'a'# TODO: Replace random mode by frecency.
    #course_page.save(('Updated on ' + date.today().strftime('%B %d, %Y')))



def main():
    site = pywikibot.Site()

if __name__ == '__main__':
    obtainCourseData()
    main()