# twerp
Tethering Wiki to ERP

It uses the hercules API to update the 'Metakgp' wiki pages every semester for all the relevant pages with all the possible details. It is aimed at being the one bot that needs to be ran one a semester for updating with all the relevant info, including calling [blackjack](https://github.com/metakgp/blackjack/blob/master/blackjack.py) (bot for grades updation) and performing the duties of [kakashi](https://github.com/metakgp/kakashi) bots

## Inspiration

Rajat is a twerp. He complains about the wiki not being updated frequently and is not willing to edit the pages by himself..... **Presenting to you twerp** - The complete remedy for twerp. Let the bot handle it.

## Abilities

As of now it can

- Add the timetable for the courses being offered by IITKGP in a semester to the corresponding page on metakgp wiki.
![Example](https://github.com/Ayushk4/twerp/blob/master/twerp.png)

- Update the time-table of existing prof pages.
- Updates the course pages with the data obtained from the google form.

## To-Dos

- Update the pages on professors with the following features (The script written will be running on per semester basis ):
  - Time Table of non-existing prof pages by creating the page first and adding to it.
  - Append to his profile, the list of courses that he taught in a semester.

- Call (a modified) Blackjack script to update the grades.

## Using twerp

- Running using pipenv:  
    &nbsp; &nbsp; Clone and change your directory to this repo and run `pipenv install`:  
            &nbsp; &nbsp; &nbsp; &nbsp; This will install the requirements and will create a virtual environment

    &nbsp; &nbsp; Run `pipenv shell`:  
            &nbsp; &nbsp; &nbsp; &nbsp; This will activate the virtualenv

- Running using pip:  
    &nbsp; &nbsp; Clone and change your directory to this repo and run `pip install -r requirements.txt`

- Run the setup.py file if you have downloaded first time  or want to add a new wiki or modify an old wiki configurations:  
    &nbsp; &nbsp; `python3 setup.py`

- It will first clone pywikibot repo in folder named `wiki_files` in your current directory

- It will ask for the link of the wiki and the with which you want to save it:  
    &nbsp; &nbsp; For metakgp write:  
        &nbsp; &nbsp; &nbsp; &nbsp; link = `https://wiki.metakgp.org/w/Main_Page`  
        &nbsp; &nbsp; &nbsp; &nbsp; name = `metakgp`

- It will then generate user files (set username as Twerp) and don't set any bot password yet, it will ask during runtime

- Run the bot :  
    &nbsp; &nbsp; `python3 twerp.py`

### For updating data from forms

- First enable the Google Sheets API, check [here](https://developers.google.com/sheets/api/) for its doc.
- Obtain the `credentials.json` file from the **Google API Console**.
- See about the sheetID of a Google Spreadsheet and basic usage of Google Sheet API [here](https://developers.google.com/sheets/api/guides/concepts)
- It will ask for the sheetID during runtime, make sure you should have the `credentials.json` file in the same folder as `twerp.py`

## Contribution

Join the slack channel : metakgp.slack.com
