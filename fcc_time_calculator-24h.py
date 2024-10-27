def add_time(start, duration, day='today'):
    weekdays = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

    # break into hours and minutes
    if start[:2][1] == ':':
        time_hours = int(start[:1])
        time_minutes = int(start[2:4:1])
    else:
        time_hours = int(start[:2])
        time_minutes = int(start[3:5:1])

    if duration[3] == ':':
        duration_hours = int(duration[:3])
        duration_minutes = int(duration[4:]) 
    elif duration[:2][1] == ':':
        duration_hours = int(duration[:1])
        duration_minutes = int(duration[2:])
    else:
        duration_hours = int(duration[:2])
        duration_minutes = int(duration[3:])

    # convert to 24h time
    if start[-2::1] == 'PM' and time_hours < 12:
        time_hours += 12

    # do math
    new_time = []
    new_time.append(0) # Days elapsed
    new_time.append(time_hours + duration_hours) # Time in hours
    new_time.append(time_minutes + duration_minutes) # Time in minutes
    new_time.append(0) # AM/PM Switch
    new_time.append(-1) # Weekday index (-1 means weekday not specified)

    if new_time[2] > 60:
        new_time[1] += 1
        new_time[2] = new_time[2]-60

    if new_time[1] > 24:
        new_time[0] = int(new_time[1]/24)
        new_time[1] = new_time[1] - (new_time[0]*24)

    # convert back to 12hr
    if new_time[1] >= 12:
        new_time[3] = 1
        new_time[1] -= 12

    # weekdays elapsed logic  
    if day != 'today':
        for d in range(len(weekdays)):
            if day.lower() == weekdays[d].lower():
                today = d
        new_day = new_time[0] + today
        while new_day > 6:
            new_day -= 7
        new_time[4] = new_day

    # build string
    if new_time[1] == 0:
        new_time[1] = 12

    if new_time[3] == 0:
        ampm = 'AM'
    elif new_time[3] == 1:
        ampm = 'PM'

    if new_time[4] != -1:
        dow = f', {weekdays[new_time[4]]}'
    else:
        dow = ''
    
    if new_time[0] == 1:
        new_day = ' (next day)'
    elif new_time[0] >= 2:
        new_day = f' ({new_time[0]} days later)'
    else:
        new_day = ''
    
    new_time_string = f'{new_time[1]}:{new_time[2]:02d} {ampm}{dow}{new_day}'

    
    return new_time_string

    #return new_time


# print(add_time('3:00 PM', '3:10'))
print(add_time('11:43 AM', '00:20'))

# Tests
""" print('FCC Tests:')
if add_time('3:30 PM', '2:12') == '5:42 PM':
    print("Pass")
else: print(f'{add_time('3:30 PM', '2:12')} fails.')
if add_time('11:55 AM', '3:12') == '3:07 PM':
    print("Pass")
else: print(f'{add_time('11:55 AM', '3:12')} fails.')
if add_time('2:59 AM', '24:00') == '2:59 AM (next day)':
    print("Pass")
else: print(f'{add_time('2:59 AM', '24:00')} fails.')
if add_time('11:59 PM', '24:05') == '12:04 AM (2 days later)':
    print("Pass")
else: print(f'{add_time('11:59 PM', '24:05')} fails.')
if add_time('8:16 PM', '466:02') == '6:18 AM (20 days later)':
    print("Pass")
else: print(f'{add_time('8:16 PM', '466:02')} fails.')
if add_time('3:30 PM', '2:12', 'Monday') == '5:42 PM, Monday':
    print("Pass")
else: print(f'{add_time('3:30 PM', '2:12', 'Monday')} fails.')
if add_time('2:59 AM', '24:00', 'saturDay') == '2:59 AM, Sunday (next day)':
    print("Pass")
else: print(f'{add_time('2:59 AM', '24:00', 'saturDay')} fails.')
if add_time('11:59 PM', '24:05', 'Wednesday') == '12:04 AM, Friday (2 days later)':
    print("Pass")
else: print(f'{add_time('11:59 PM', '24:05', 'Wednesday')} fails.')
if add_time('8:16 PM', '466:02', 'tuesday') == '6:18 AM, Monday (20 days later)':
    print("Pass")
else: print(f'{add_time('8:16 PM', '466:02', 'tuesday')} fails.') """