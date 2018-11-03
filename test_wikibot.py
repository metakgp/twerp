import pywikibot
from pywikibot import pagegenerators
import time
import re



def main():
    site = pywikibot.Site()
    cat = pywikibot.Category(site,'Category:Courses')
    gen = pagegenerators.CategorizedPageGenerator(cat)

    allcourses = {i.title()[:7]:i for i in gen}

    course_page = allcourses['CS60092']
    wiki_text = course_page.text

    #course_page.text = wiki_text + 'a'# TODO: Replace random mode by frecency.
    #course_page.save(('Updated on ' + date.today().strftime('%B %d, %Y')))


if __name__ == '__main__':
    main()