import os
import sys
import json
path = os.path.abspath(os.path.dirname(__file__))
PATH_TO_MODULE = os.path.join(path, 'wiki_files')
sys.path.append(PATH_TO_MODULE)


import pywikibot
from pywikibot import pagegenerators
import string

from course_details import getDeptList, getCourseData, getCoursesDeptWise
from time_table_to_wiki_table import getTimeTable
from add_timetable_to_wiki import create_course_page, update_with_timetable, update_without_timetable
from prof_details import get_all_info_of_faculty, get_table_of_prof
from update_prof_table import check_profpage_existence, make_Time_Table_of_prof, update_profpage_with_timetable
from scrape import convert_form_to_dict
from update_course_page_details import append_content_to_page

site = pywikibot.Site()


def course_department_wise(allcoursesonwiki, existing_course_pages):
    departments = getDeptList()
    course_list_this_sem = []
    new_pages_created = []

    for department in departments:
        print('Courses from ' + department['name'])
        courses = getCoursesDeptWise(department['code'])
        for course in courses:
            if course['code'] == 'EA10005':
                continue

            course['name'] = string.capwords(course['name'])
            if course['code'] not in existing_course_pages:
                new_pages_created.append(course['code'])
                course['department'] = department['name']
                timetable = getTimeTable(getCourseData(course))
                create_course_page(site, course, timetable)
            else:
                timetable = getTimeTable(getCourseData(course))
                update_with_timetable(allcoursesonwiki, site, course,
                                      timetable)

            course_list_this_sem.append(course['code'])

    print('\n\nFound ' + str(len(course_list_this_sem)) + ' courses being offered this semester')
    not_this_sem_courses = [i for i in allcoursesonwiki if i not in course_list_this_sem]
    print('Now removing previous year\'s timetable from the courses not in this semester')
    for course in not_this_sem_courses:
        print(allcoursesonwiki[course])
        update_without_timetable(allcoursesonwiki, site, course)

    print('New pages Created = ' + str(len(new_pages_created)))
    print('Courses this semester = ' + str(len(course_list_this_sem)))
    print("\n")


#      TODO : WRITE THE NAME OF THE CURRENT SEM AS HEADING TO THE TIMETABLE
def update_time_table_of_prof():
    info_table = get_all_info_of_faculty()
    for entry in info_table:
        table_json = get_table_of_prof(entry['name'], entry['department']['code'])
        timetable = make_Time_Table_of_prof(table_json)
        prof_existence = check_profpage_existence(entry['name'])
        if(prof_existence == 1):  # 1 means not exist
            print("Page of professor {} not found skipping".format(
                   entry['name']))
        else:
            print('Professor {} page found'.format(entry['name']))
            update_profpage_with_timetable(entry, site, timetable)
        print("Updated time table of {}".format(entry['name']))


def update_course_page_data(allcoursesonwiki, spreadsheetid):
    contents_of_page = [
        '=Syllabus=',
        '=Syllabus mentioned in ERP=',
        '==Concepts taught in class==',
        '===Student Opinion===',
        '==How to Crack the Paper==',
        '=Classroom resources=',
        '=Additional Resources='
        ]
    # Remove the '=' sign
    formatted_contents = []
    for entry in contents_of_page:
        s = []
        for x in entry:
            if x != '=':
                s.append(x)
        st = "".join(s)
        formatted_contents.append(st)
    required_data = convert_form_to_dict(spreadsheetid)
    print('\n\n')
    for entry in required_data:
        course_page = allcoursesonwiki[entry['Course Code']]
        new_text = append_content_to_page(course_page.text, entry,
                                          formatted_contents)
        course_page.text = new_text
        course_page.save('Added data from Google Form')
        print("Updated course data of course code ", entry['Course Code'])


def main():

    print("What do you want to do")
    print("type 1 for updating course page with timetable")
    print("type 2 for updating prof page with timetable")
    print("type 3 for doing both of the above")
    print("type 4 for updating course page data obtained from form")
    answer = input('>')
    # print(answer)
    if(answer == '1'):
        cat = pywikibot.Category(site, 'Category:Courses')
        gen = pagegenerators.CategorizedPageGenerator(cat)

        allcoursesonwiki = {i.title()[:7]: i for i in gen}

        existing_course_pages = []
        for keys in allcoursesonwiki:
            existing_course_pages.append(keys)
        course_department_wise(allcoursesonwiki, existing_course_pages)
    if(answer == '2'):
        print('Starting to update prof pages')
        update_time_table_of_prof()
    if(answer == '3'):
        cat = pywikibot.Category(site, 'Category:Courses')
        gen = pagegenerators.CategorizedPageGenerator(cat)
        allcoursesonwiki = {i.title()[:7]: i for i in gen}
        existing_course_pages = []
        for keys in allcoursesonwiki:
            existing_course_pages.append(keys)
        course_department_wise(allcoursesonwiki, existing_course_pages)
        print('Starting to update prof pages')
        update_time_table_of_prof()
    if(answer == '4'):
        cat = pywikibot.Category(site, 'Category:Courses')
        gen = pagegenerators.CategorizedPageGenerator(cat)

        allcoursesonwiki = {i.title()[:7]: i for i in gen}
        SPREADSHEET_ID = input('Write the spreadsheetID> ')
        update_course_page_data(allcoursesonwiki, SPREADSHEET_ID)

if __name__ == '__main__':
    main()
