from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import json
# from google.auth.transport.requests import Request

# Better to use read only scope for not modifying the contents accidentally
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.

RANGE_NAME = "A:Z"

# If run this function directly then it will generate two filders in the PWD
# one containing the data (modified, see below) from sheets API and the other
# containing the required dict


def convert_form_to_dict(SPREADSHEET_ID):
    """Uses sheets API to obtain result

    Returns the required formatted list containing
    nested dicts of responses obtained from the google sheet
    """
    creds = None
    flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
    creds = flow.run_local_server()

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME,
                                majorDimension='ROWS').execute()
    values = result.get('values', [])
    # Sheets api removing trailing empty spaces in the result
    # If somebody has not filled some columns at the end
    # then it will not be there in the json data
    # example only till column[2] is filled then the rest will not
    # be there in the json data of the API
    # We will add a "" instead
    # This is not the case when some data between is missing inbetween
    # for example column[2] is missing but onwards are filled
    # sheet automatically adds "" in this case
    for item in result['values']:
        length = len(item)
        if (length < 7):
            while(length != 7):
                item.append("")
                length = length + 1

    print('{} values received'.format(len(values)))
    all_responses = []
    # Obtaining all course codes and making primary keys in Dict, appending
    # this into the list
    # Also renaming headings as they are in the wiki
    values[0][2] = 'Concepts taught in class'
    values[0][3] = 'Student Opinion'
    values[0][4] = 'How to Crack the Paper'
    values[0][5] = 'Classroom resources'
    for item in values[1:]:
        dict_format = {}
        dict_format['Course Code'] = item[1]
        dict_format['Timestamp'] = []
        for element in values[0][2:]:
            dict_format[element] = []
        all_responses.append(dict_format)
    # filling all the data into the required course code
    for item in values[1:]:
        for course_data in all_responses:
            if(course_data['Course Code'] == item[1]):
                course_data['Timestamp'].append(item[0])
                index = 2
                # ignoring the empty entries
                for element in values[0][2:]:
                    if(item[index] != ""):
                        course_data[element].append(item[index])
                        index = index + 1
                break
    total = [all_responses, result]
    return total[0]


if __name__ == '__main__':
    answer = convert_form_to_dict()
    with open('result.json', 'w') as f:
        json.dump(answer[1], f, indent=2)
    with open('required_dict.json', 'w') as f:
        json.dump(answer[0], f, indent=2)
