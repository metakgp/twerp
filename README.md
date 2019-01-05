# twerp
Tethering Wiki to ERP

It uses the hercules API to update the 'Metakgp' wiki pages every semester for all the relevant pages with all the possible details. It is aimed at being the one bot that needs to be ran one a semester for updating with all the relevant info, including calling [blackjack](https://github.com/metakgp/blackjack/blob/master/blackjack.py) (bot for grades updation) and performing the duties of [kakashi](https://github.com/metakgp/kakashi) bots

##### Inspiration :
Rajat is a twerp. He complains about the wiki not being updated frequently and is not willing to edit the pages by himself..... Presenting to you twerp - The complete remedy for twerp. Let the bot handle it. 

## Abilities
As of now it can add the timetable for the courses being offered by IITKGP in a semester to the corresponding page on metakgp wiki.
![Example](https://github.com/Ayushk4/twerp/blob/master/twerp.png)



#### To-Dos
* Update the pages on professors with the following features (The script written will be running on per semester basis ):
    - Time Table of a prof (Right now works only for existing prof pages).
    - Append to his profile, the list of courses that he taught in a semester.

* Call (a modified) Blackjack script to update the grades.

# Using twerp

* Running using pipenv:<br>
    &nbsp; &nbsp; Clone and change your directory to this repo and run `pipenv install`:<br>
            &nbsp; &nbsp; &nbsp; &nbsp; This will install the requirements and will create a virtual environment

    &nbsp; &nbsp; Run `pipenv shell`:<br>
            &nbsp; &nbsp; &nbsp; &nbsp; This will activate the virtualenv


* Running using pip:<br>
    &nbsp; &nbsp; Clone and change your directory to this repo and run `pip install -r requirements.txt`


* Run the setup.py file if you have downloaded first time  or want to add a new wiki or modify an old wiki configurations:<br>
    &nbsp; &nbsp; `python3 setup.py`
 
* It will first clone pywikibot repo in folder named `wiki_files` in your current directory

* It will ask for the link of the wiki and the with which you want to save it:<br>
    &nbsp; &nbsp; For metakgp write:<br>
        &nbsp; &nbsp; &nbsp; &nbsp; link = `https://wiki.metakgp.org/w/Main_Page`<br>
        &nbsp; &nbsp; &nbsp; &nbsp; name = `metakgp`

* It will then generate user files (set username as Twerp) and don't set any bot password yet, it will ask during runtime

* Run the bot :<br>
    &nbsp; &nbsp; `python3 twerp.py`
 
## Contribution
Join the slack channel : metakgp.slack.com
