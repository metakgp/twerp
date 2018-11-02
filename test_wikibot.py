import pywikibot
from random import randint
from datetime import date
from pywikibot import pagegenerators
import time
import re
from tqdm import tqdm




def main():
    site = pywikibot.Site()
    
    cat = pywikibot.Category(site,'Category:Courses')
    #print(cat.text)
    gen = pagegenerators.CategorizedPageGenerator(cat)
    #print(gen)
#    allcourses = gen
    allcourses = {i.title()[:7]:i for i in gen}


    print(type(allcourses['CS60092']))
    course_page = allcourses['CS60092']
    wiki_text = course_page.text
    print(wiki_text)

    #print(wpage.text)

    course_page.text = wiki_text + 'a'# TODO: Replace random mode by frecency.
    course_page.save(('Updated on ' + date.today().strftime('%B %d, %Y')))


if __name__ == '__main__':
    main()



# def genFormattedGradeText(courseCode,new=False):
#     # If new course, then text for the grades is different.
#     stats = newGrades[courseCode]['grades']
#     if new:
#         text = u'\n| grades = {{Grades\n'+ ' '*11 +'| EX = '+ str(stats['EX']) +'\n'+ ' '*11 +'| A = '+ str(stats['A']) +'\n'+ ' '*11 +'| B = '+ str(stats['B']) +'\n'+ ' '*11 +'| C = '+ str(stats['C']) +'\n'+ ' '*11 +'| D = '+ str(stats['D']) +'\n'+ ' '*11 +'| P = '+ str(stats['P']) +'\n'+ ' '*11 +'| F = '+ str(stats['F']) +'\n'+ ' '*11 +'}}\n'
#     else:
#         text = u'{{Grades\n'+ ' '*11 +'| EX = '+ str(stats['EX']) +'\n'+ ' '*11 +'| A = '+ str(stats['A']) +'\n'+ ' '*11 +'| B = '+ str(stats['B']) +'\n'+ ' '*11 +'| C = '+ str(stats['C']) +'\n'+ ' '*11 +'| D = '+ str(stats['D']) +'\n'+ ' '*11 +'| P = '+ str(stats['P']) +'\n'+ ' '*11 +'| F = '+ str(stats['F']) +'\n'+ ' '*11 +'}}'
#     return text

# oldGrade = re.compile('{{Grades.*[0-9].* }}',re.DOTALL)

# def updateGrades(code):
#     temp = allcourses[code]
#     temp.text = oldGrade.sub(genFormattedGradeText(code),temp.text)
#     temp.save(summary='Updated grades',botflag=True)

# def currentGradesOnWiki(code):
#     g = re.findall(r'{{Grades.*[0-9].* }}',allcourses[code].text,re.DOTALL)[0]
#     tupl = re.findall('([A-Z]+) = ([0-9]+)',g)
#     return {i[0]:int(i[1]) for i in tupl}

# def insertBefore(data, pattern, newText):
#     i = data.find(pattern)
#     return data[:i] + newText + data[i:]

# def genPageNewText(courseCode):
#     return insertBefore(allcourses[courseCode].text,'\n}}',genFormattedGradeText(courseCode,True))

# def addGrades(courseCode):
#     temp = allcourses[courseCode]
#     temp.text = genPageNewText(courseCode)
#     temp.save(summary='Added previous year\'s grade distribution',botflag=True)

