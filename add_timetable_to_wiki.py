import pywikibot

def update_with_timetable(allcoursesonwiki,site,course,timetable):
    course_page = allcoursesonwiki[course['code']]
    if '=Time Table=' in course_page.text:
        course_page.text = course_page.text.rsplit('=Time Table=', 1)[0] + "\n\n=Time Table=\n\n" + timetable + "\n"
    else:
        course_page.text = course_page.text + "\n\n=Time Table=\n\n" + timetable + "\n"

    
    course_page.save(('Add Time Table'))


def update_without_timetable(allcoursesonwiki,site,course):
    course_page = allcoursesonwiki[course]
    if '=Time Table=' in course_page.text:
        course_page.text = course_page.text.rsplit('=Time Table=', 1)[0] + "\n\n"
        course_page.save(('Remove Time Table'))

    else:
        pass

def create_course_page(site,course,timetable):

    course['timetable'] = timetable

# NOTE: The braces are doubled to escape it as string formatting character
    
    course_text = r"""
{{{{Infobox course
| course_code = {code}
| course_name = {name}
| department = [[{department}]]
| credits = {credits}
| ltp = 
| professor =
| venue =
}}}}

=Syllabus=

==Syllabus mentioned in ERP==

==Concepts taught in class==

===Student Opinion===
    
==How to Crack the Paper==

=Classroom resources=
    
=Additional Resources=

[[Category:Courses]][[Category:{department}]]

=Time Table=
{timetable}
    """
    course_text = course_text.format(**course)
    course_page = pywikibot.Page(site, "{}: {}".format(course['code'], course['name']))
    course_page.text = course_text
    msg = "Create Page for {}".format(course['name'])
    course_page.save(msg)

