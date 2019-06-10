import pywikibot
import requests
import json


def check_profpage_existence(name):
    split = name.split()
    join_with_underscore = '_'.join(split)
    r = requests.get('https://wiki.metakgp.org/w/{}'.format(join_with_underscore))
    existence = 1
    if r.status_code == 200:
        existence = 2
    return(existence)


def create_TimeTable_From_Slots_of_prof(slots, venues):

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    hours = ['8', '9', '10', '11', '12', 'LunchBreak', '2', '3', '4', '5']

    timetable = '{| class="wikitable \n|-\n! Day !! 8:00-8:55 am !! 9:00-9:55 am !! 10:00-10:55 am !! 11:00-11:55 am !! 12:00-12:55 pm !!  !! 2:00-2:55 pm !! 3:00-3:55 pm!! 4:00-4:55 pm!! 5:00-5:55 pm'
    currentSlotIndex = 0

    for day in days:
        timetable += '\n|-\n!' + day + "\n"
        hourIndex = 0
        for hourIndex in range(10):
            timetable += '|| '
            if(currentSlotIndex < len(venues)):
                if (day == slots[currentSlotIndex]['day']) and (hours[hourIndex] == slots[currentSlotIndex]['time']):
                    venue_room = venues[currentSlotIndex]['room'][0]
                    venue_course = venues[currentSlotIndex]['course'][0]
                    timetable += '--'.join([str(num) for num in [venue_room,venue_course]])
                    currentSlotIndex += 1
    timetable += '\n|}'
    return timetable


def make_Time_Table_of_prof(data):

    slots = []
    venues = []

    for day in data:
        if data[day] is not None:
            for element in data[day]:
                slot = {}
                slot['time'] = element['slot']['time']['time'].split(' ', 1)[0]
                slot['day'] = element['slot']['time']['day']
                slots.append(slot)
                room_and_course = {'room': [], 'course': []}
                for room in element['rooms']:
                    if room == '0':  # 0 mean the class is in some room "in department"
                        room_and_course['room'].append('IN DEPT')
                    else:
                        room_and_course['room'].append(room)
                    room_and_course['course'].append(element['course']['name'])
                # element['rooms'] = modified_room
                venues.append(room_and_course)

    if len(slots) == 0:
        return ''
    # print(venues)
    # print(slots)
    timetable = create_TimeTable_From_Slots_of_prof(slots, venues)
    # print(timetable)
    if len(timetable) != 0:
        return timetable
    else:
        return ''


def update_profpage_with_timetable(prof_data, site, timetable):
    name = prof_data['name']
    split = name.split()
    join_with_underscore = '_'.join(split)
    page = pywikibot.Page(site, 'https://wiki.metakgp.org/w/{}'.format(join_with_underscore))
    prof_page = pywikibot.Page(site, "{}".format(prof_data['name']))
    if '=Time Table=' in prof_page.text:
        prof_page.text = prof_page.text.rsplit('=Time Table=', 1)[0] + "\n\n=Time Table=\n\n" + timetable + "\n"
    else:
        prof_page.text = prof_page.text + "\n\n=Time Table=\n\n" + timetable + "\n"

    prof_page.save(('Add Time Table'))
