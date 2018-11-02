#import pywikibot

data ={'Monday': [{'course': {'name': 'TRANSFER PROCESS IN FOOD ENGINEERING', 'code': 'AG60097', 'credits': 4}, 'slot': {'time': {'day': 'Monday', 'time': '8 AM'}, 'slot': 'A3'}, 'rooms': ['0']}, {'course': {'name': 'TRANSFER PROCESS IN FOOD ENGINEERING', 'code': 'AG60097', 'credits': 4}, 'slot': {'time': {'day': 'Monday', 'time': '9 AM'}, 'slot': 'A3'}, 'rooms': ['0']}, {'course': {'name': 'TRANSFER PROCESS IN FOOD ENGINEERING', 'code': 'AG60097', 'credits': 4}, 'slot': {'time': {'day': 'Monday', 'time': '5 PM'}, 'slot': 'S3'}, 'rooms': ['0']}], 
    'Tuesday': [{'course': {'name': 'TRANSFER PROCESS IN FOOD ENGINEERING', 'code': 'AG60097', 'credits': 4}, 'slot': {'time': {'day': 'Tuesday', 'time': '12 PM'}, 'slot': 'A3'}, 'rooms': ['0']}],
    'Wednesday': None,
    'Thursday': [{'course': {'name': 'TRANSFER PROCESS IN FOOD ENGINEERING', 'code': 'AG60097', 'credits': 4}, 'slot': {'time': {'day': 'Thursday', 'time': '5 PM '}, 'slot': 'S3'}, 'rooms': ['0']}],
    'Friday': [{'course': {'name': 'TRANSFER PROCESS IN FOOD ENGINEERING', 'code': 'AG60097', 'credits': 4}, 'slot': {'time': {'day': 'Friday', 'time': '5 PM'}, 'slot': 'S3'}, 'rooms': ['0']}]
    }

slots = []
for day in data:
    #print (days)
    #print(type(data[day]))
    if(data[day] != None):
        for element in data[day]:
            slots.append(element['slot']['slot'])
slots = set(slots)

def twerpUpdate():
    pass