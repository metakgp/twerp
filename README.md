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
        &nbsp; &nbsp; &nbsp; &nbsp; family = 5 (it'll be mediawiki)

- It will then generate user files (set username as Twerp) and don't set any bot password yet, it will ask during runtime

- Run the bot :  
    &nbsp; &nbsp; `python3 twerp.py`

### For updating data from form under Course Archiving Drive

We are collecting information from masses to update courses on metakgp wiki in [this form](https://forms.gle/1WcXp8UQ6UpaNF7y9). Below is the process on how to update from the 
sheet to the wiki using twerp.

- First enable the Google Sheets API, check [here](https://developers.google.com/sheets/api/) for its doc.
- Obtain the `credentials.json` file from the **Google API Console**.
- Create a new sheet that is copy of response sheet and delete entries till we have already updated (mentioned below).
- See about the sheetID of the new Google Spreadsheet and basic usage of Google Sheet API [here](https://developers.google.com/sheets/api/guides/concepts)
- It will ask for the sheetID during runtime, make sure you should have the `credentials.json` file in the same folder as `twerp.py`
- If the script stops in between, please remove entries till the row that have been updated during this runtime otherwise duplicate entries will be created.

Once the update is done, manually verify if the update was successful and make edits if any necessary.

**NOTE: Updated till row number 29**

## Contribution

Join the slack channel : metakgp.slack.com
