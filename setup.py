import os
from git import Repo
import sys
path = os.path.abspath(os.path.dirname(__file__))
PATH_TO_MODULE=os.path.join(path,'wiki_files')
sys.path.append(PATH_TO_MODULE)
if(os.path.exists(PATH_TO_MODULE)):
    print('You have pywikibot repo downloaded')

else:
    print('Downloading pywikibot github repository')
    Repo.clone_from('https://gerrit.wikimedia.org/r/pywikibot/core.git', 'wiki_files')
    print("Downloaded pywikibot code from Github into the folder named wiki files")

    link=input('Write the link for the wikipage : ')
    name=input('What do you want to give the name : ')
    os.chdir(PATH_TO_MODULE)
    output=os.system('python3 generate_family_file.py {} {}'.format(link,name))

user_files_output=os.system('python3 generate_user_files.py -dir:{}'.format(path))
os.chdir(path)