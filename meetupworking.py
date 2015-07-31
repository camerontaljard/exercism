__author__ = 'cameron'


from datetime import timedelta
import datetime
import calendar


def meetup_day(year, month, day, place):

    thedate = datetime.date(year, month, day=1)
    print thedate

    alldays = list()
    alldates = list()

    daysdict = dict()


    #prints the names of the first day and number of days
    print calendar.monthrange(year, month)

    startday = int(calendar.monthrange(year, month)[0])

    noofdays = int(calendar.monthrange(year, month)[1])

    startdayname = calendar.day_name[startday]

    days = [datetime.date(year, month, i).strftime('%A') for i in range(1, noofdays+1)]
    index = days.index(startdayname)
    alldays = days[index:] + days[:index]

    for i in range(noofdays):
        alldates.append(thedate + timedelta(days=i))

    i = alldates
    j = alldays



    b = dict(zip(i,j))
    for k,v in enumerate(b):
        print k,v

    # print alldays
    # print alldates
    #print len(alldays)

    #print calendar.Calendar.itermonthdays(year, month
    #print calendar.day_name[startday]


    if place == '1st':
        print(place)
    if place == '2nd':
        pass
    if place == '3rd':
        pass
    if place == '4th':
        pass
    if place == 'last':
        pass


meetup_day(2013, 5, 'Tuesday', '1st')
meetup_day(2012, 2, 'Wednesday', 'last')
meetup_day(2013, 9, 'Thursday', '3rd')


__author__ = 'cameron'


from datetime import timedelta
import datetime
import calendar
from dateutil import parser
import itertools


def meetup_day(year, month, day, place):

    thedate = datetime.date(year, month, day=1)
    #print thedate

    alldates = list()


    #prints the names of the first day and number of days
    #print calendar.monthrange(year, month)

    startday = int(calendar.monthrange(year, month)[0])

    noofdays = int(calendar.monthrange(year, month)[1])

    startdayname = calendar.day_name[startday]

    days = [datetime.date(year, month, i).strftime('%A') for i in range(1, noofdays+1)]
    index = days.index(startdayname)
    alldays = days[index:] + days[:index]

    for i in range(noofdays):
        alldates.append(str(thedate + timedelta(days=i)))

    daypos = [i for i, x in enumerate(alldays) if x == day]


    if place == '1st':
        when = alldates[int(daypos[0])]
        then = datetime.datetime.strptime(when, '%Y-%m-%d').date()
        return then

    if place == '2nd':
        when = alldates[daypos[1]]
        then = datetime.datetime.strptime(when, '%Y-%m-%d').date()
        return then

    if place == '3rd':
        when = alldates[daypos[2]]
        then = datetime.datetime.strptime(when, '%Y-%m-%d').date()
        return then

    if place == 'teenth':
        pass


    if place == '4th':
        when = alldates[daypos[3]]
        then = datetime.datetime.strptime(when, '%Y-%m-%d').date()
        return then

    if place == 'last':
        when = alldates[daypos[4]]
        then = datetime.datetime.strptime(when, '%Y-%m-%d').date()
        return then



#meetup_day(2013, 5, 'Tuesday', '1st')
# meetup_day(2012, 2, 'Wednesday', '1st')
# meetup_day(2013, 9, 'Thursday', '1st')

from datetime import timedelta, date
from calendar import monthrange

oneday = timedelta(days=1)
dayIndex = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}


def meetup_day(year, month, weekday, selector):
    selectorStart = {'1st':1, '2nd':8, '3rd':15, '4th':22, 'teenth':13, 'last':monthrange(year, month)[1]-6} # the first possible day of the month for any given selector

    day = date(year, month, selectorStart[selector])
    while day.weekday() != dayIndex[weekday]:
        day += oneday
    return day
