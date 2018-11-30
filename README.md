# twerp
Tethering Wiki to ERP

It uses the hercules API to update the 'Metakgp' wiki pages every semester for all the relevant pages with all the possible details. It is aimed at being the one bot that needs to be ran one a semester for updating with all the relevant info, including calling [blackjack](https://github.com/metakgp/blackjack/blob/master/blackjack.py) (bot for grades updation) and performing the duties of [kakashi](https://github.com/metakgp/kakashi) bots

##### Inspiration :
Rajat is a twerp. He complains about the wiki not being updated frequently and is not willing to edit the pages by himself..... Presenting to you twerp - The complete remedy for twerp. Let the bot handle it. 

## Abilities
As of now it can add the timetable for the courses being offered by IITKGP in a semester to the corresponding page on metakgp wiki.
![Example](https://github.com/Ayushk4/twerp/blob/master/twerp.png)



#### To-Dos
* Update the pages on professors with the follwing features (The script written will be running on per semester basis ):
    - Time Table of a prof.
    - Append to his profile, the list of courses that he taught in a semester.

* Call (a modified) Blackjack script to update the grades.

# Using twerp

* Clone and change your directory to this repo and run `pip install -r requirements.txt`

* Clone the pywikibot library :

`git clone https://gerrit.wikimedia.org/r/pywikibot/core.git wiki_files`

`mv wiki_files/* .`

* Generate wiki files :

`python3 generate_family_file.py https://wiki.metakgp.org/w/Main_Page metakgp`

* Generate user files (set username as Twerp) and don't set any bot password yet, it will ask during runtime :

`python3 generate_user_files.py`

* Run the bot :

`python3 twerp.py`

## Contribution
Join the slack channel : metakgp.slack.com
