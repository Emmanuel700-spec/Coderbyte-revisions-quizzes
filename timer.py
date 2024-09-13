def time_to_minutes(t):
    time, period = t.split()
    hours, minutes = map(int, time.split(':'))
    if period == 'PM':
        if hours != 12:
            hours += 12
    elif period == 'AM':
        if hours == 12:
            hours = 0
    return hours * 60 + minutes

def CountingMinutesI(time_range):
    time1, time2 = time_range.split(' - ')
    minutes1 = time_to_minutes(time1)
    minutes2 = time_to_minutes(time2)
    difference = minutes2 - minutes1
    
    if difference < 0:
        difference += 24 * 60
    
    return difference

# Correctly handle user input
# input = input("Enter time range (e.g., '1:30 PM - 2:45 PM'): ")
print(CountingMinutesI(input()))

