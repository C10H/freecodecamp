def add_time(start_time:str,duration:str,week:str=''):
    AM_PM = start_time.split(' ')[1]
    hour,min = start_time.split(' ')[0].split(':')
    weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    is_AM_or_PM = ['AM','PM']
    week = week.title()
    day = 0
    min = int(min)
    hour = int(hour)
    index = 0
    duration_hour, duration_min = duration.split(':')
    duration_hour = int(duration_hour)
    duration_min = int(duration_min)
    hour = hour + duration_hour
    min = min + duration_min
    if AM_PM == 'AM':
        AM_PM = 0
    elif AM_PM == 'PM':
        AM_PM = 1
    hour = hour + min // 60
    min = min % 60
    AM_PM = AM_PM + hour // 12
    hour = hour % 12
    if hour == 0:
        hour = 12
    day = day + AM_PM // 2
    AM_PM = AM_PM % 2
    if week != '':
        week = week.title()
        index = weeks.index(week)
    index_after = (index + day) % 7
    if week == '':
        if day == 0:
            return 'Returns: {}:{:02d} {}'.format(hour,min, is_AM_or_PM[AM_PM])
            # add_time("3:00 PM", "3:10")
            # Returns: 6:10 PM
        elif day == 1:
            return 'Returns: {}:{:02d} {} (next day)'.format(hour,min,is_AM_or_PM[AM_PM])
            # add_time("10:10 PM", "3:30")
            # Returns: 1:40 AM (next day)
        else:
            return 'Returns: {}:{:02d} {} ({} days later)'.format(hour,min,is_AM_or_PM[AM_PM],day)
            # Returns: 7:42 AM (9 days later)
    else:
        if day == 0:
            return 'Returns: {}:{:02d} {}, {}'.format(hour,min,is_AM_or_PM[AM_PM],weeks[index_after])
            # Returns: 2:02 PM, Monday
        elif day == 1:
            return 'Returns: {}:{:02d} {}, {} (next day)'.format(hour,min,is_AM_or_PM[AM_PM],weeks[index_after])
            # Returns: 12:03 AM, Thursday (next day)
        else:
            return 'Returns: {}:{:02d} {}, {} ({} days later)'.format(hour,min,is_AM_or_PM[AM_PM],weeks[index_after],day)
            # Returns: 12:03 AM, Thursday (2 days later)
