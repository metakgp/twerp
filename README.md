# twerp
Tethering Wiki to ERP

This is supposed to use the hercules API to update the 'Metakgp' wiki pages every semester for all the relevant pages with all the possible details.

##### Inspiration :
Rajat is a twerp. He complains about the wiki not being updated frequently and is not willing to edit the pages by himself..... Presenting to you twerp - The complete remedy for twerp. Let the bot handle it. 

## Abilities
As of now it can add the timetable for the courses being offered by IITKGP in a semester to the corresponding page on metakgp wiki.

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
