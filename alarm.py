import time
time_now = float(input('Whats the current time in hours:'))
hours_waiting = float(input('How long should it wait: '))


alarm_time = (time_now + hours_waiting) % 24


print(f"The alarm will go off at {alarm_time:.2f} hours.")