import pywikibot
from pywikibot import pagegenerators
import time
import re
import os
path = os.path.abspath(os.path.dirname(__file__))

import string

from course_details import getDeptList,getCourseData,getCoursesDeptWise
from time_table_to_wiki_table import getTimeTable
from add_timetable_to_wiki import create_course_page, update_with_timetable

site = pywikibot.Site()

def course_department_wise(allcoursesonwiki,existing_course_pages):
    departments = getDeptList()
    course_list_this_sem = []

    for department in departments:
        print('Getting courses from ' + department['name'] )
        courses = getCoursesDeptWise(department['code'])
        for course in courses:
            course['name'] = string.capwords(course['name'])
            if course['code'] not in existing_course_pages:
                course['department'] = department['name']
                print(course)
                timetable = getTimeTable(getCourseData(course))
                create_course_page(site,course,timetable)
            else:
                timetable = getTimeTable(getCourseData(course))
                update_with_timetable(allcoursesonwiki,site,course,timetable)
                time.sleep(10)

            course_list_this_sem.append(course['code'])


    print('\n\nFound ' + str(len(course_list_this_sem)) + ' courses being offered this semester')

    not_this_sem_courses  = [i for i in allcoursesonwiki if i not in course_list_this_sem]

    print(not_this_sem_courses)




#TODO 1) CHECK IF PAGE EXISTS OR NOT--------done
#     2) check if timetable exist or not
#     3) WRITE THE NAME OF THE CURRENT SEM

def main():

    cat = pywikibot.Category(site,'Category:Courses')
    gen = pagegenerators.CategorizedPageGenerator(cat)

    allcoursesonwiki = {i.title()[:7]:i for i in gen}

#    course_page = allcoursesonwiki['CS60092']

    existing_course_pages = []
    for keys in allcoursesonwiki:
        existing_course_pages.append(keys)

#    wiki_text = course_page.text

#    notExistingGrades = [i for i in allcourses if i in newGrades and i not in alreadyExistingGrades]
#    for code in notExistingGrades:
#       print()


#    print(wiki_text)
    #course_page.text = wiki_text + 'a'
    #course_page.save(('Updated on ' + date.today().strftime('%B %d, %Y')))


    print ("phase 1 \n")
    course_department_wise(allcoursesonwiki,existing_course_pages)    



if __name__ == '__main__':
    main()