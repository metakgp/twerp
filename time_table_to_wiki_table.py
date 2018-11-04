import os
path = os.path.abspath(os.path.dirname(__file__))

#0 MEAN IN DEPT

def createTimeTableFromSlots(slots,venues):

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    hours = ['8','9','10','11','12','LunchBreak','2','3','4','5'] #here Lunchbreak could have been replaed with any string not between the hours that class goes on

    timetable = '{| class="wikitable \n|-\n! Day !! 8:00-8:55 am !! 9:00-9:55 am !! 10:00-10:55 am !! 11:00-11:55 am !! 12:00-12:55 pm !!  !! 2:00-2:55 pm !! 3:00-3:55 pm!! 4:00-4:55 pm!! 5:00-5:55 pm'
    currentSlotIndex = 0

    for day in days:
        timetable +='\n|-\n!' + day + "\n"
        hourIndex = 0
        #while (day == slots[currentSlotIndex]['day']):
        for hourIndex in range(10):
            timetable += '|| '
            if(currentSlotIndex < len(venues)):
                if (day == slots[currentSlotIndex]['day']) and (hours[hourIndex] == slots[currentSlotIndex]['time']):
                    timetable += ','.join(venues[currentSlotIndex])
                    currentSlotIndex += 1
    timetable += '\n|}'
    return timetable


def getTimeTable(data):

    slots = []
    venues = []

    for day in data:
        if(data[day] != None):
            for element in data[day]:
                slot = {}
                slot['time'] = element['slot']['time']['time'].split(' ', 1)[0]
                slot['day'] = element['slot']['time']['day']
                slots.append(slot)
                modified_room = []
                for room in element['rooms']:
                    if room == '0':
                        modified_room.append('In Dept')
                    else:
                        modified_room.append(room)
                element['rooms'] = modified_room
                venues.append(element['rooms'])

    if len(slots) == 0:
        return ''
    timetable = createTimeTableFromSlots(slots,venues)

    if len(timetable) != 0:
        return timetable
    else :
        return ''