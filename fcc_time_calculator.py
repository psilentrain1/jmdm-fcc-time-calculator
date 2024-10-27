def add_time(start, duration, day='today'):
    weekdays = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    days_elapsed = 0

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

    # do math
    new_time = []
    new_time.append(time_hours + duration_hours)
    new_time.append(time_minutes + duration_minutes)

    if new_time[1] > 60:
        new_time[0] += int(new_time[1]/60)
        new_time[1] = new_time[1]-60

    # logic to detect am/pm and change if needed
    if start[-2::1] == 'AM':
        time_suffix = 0
    else:
        time_suffix = 1

    #logic to tell what day it is and how many days elapsed    
    if day != 'today':
        for d in range(len(weekdays)):
            if day.lower() == weekdays[d].lower():
                today = d
        new_day_i = days_elapsed + today
        if new_day_i > 6:
            new_day_i -= 7
        new_day = weekdays[new_day_i]
    elif day == 'today':
        if days_elapsed == 1:
            new_day == 'next day'
        elif days_elapsed >= 2:
            new_day = f'{days_elapsed} days later'



    new_time = new_time


    return new_time


add_time('3:00 PM', '3:10')

# Tests
print('FCC Tests:')
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
else: print(f'{add_time('8:16 PM', '466:02', 'tuesday')} fails.')