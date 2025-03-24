import time
import winsound

#The clock function that takes number of seconds elapsed as input and converts it to minutes and hours
def clock(clock_signal):
    minutes, seconds = divmod(clock_signal, 60)
    hours, minutes = divmod(minutes, 60)
    return (int(seconds), int(minutes), int(hours))

#t0 is the beginning time of the timer
t0 = time.time()
i = 0

while True:
    
    t1 = time.time()
    
    s, m, h = clock(t1-t0)

    colons = [True, False]

    #for formatting, a zero is present as the ten's digit if seconds or minutes are in single digits
    if s < 10:
        s_zero = 0
    else:
        s_zero = ''

    if m < 10:
        m_zero = 0
    else:
        m_zero = ''
        
    #display the time in the form of a watch which beeps at every second
    if colons[i%2]:
        print(f'{h} : {m_zero}{m} : {s_zero}{s}',end = '\r')
    else:
        print(f'{h}   {m_zero}{m}   {s_zero}{s}',end = '\r')

    frequency = 12000 #in hertz
    duration = 400 #in milliseconds
    winsound.Beep(frequency, duration)
    
    t2 = time.time()

    #delta is the time taken by 1 while loop iteration to execute, and this is lesser than 1 second.
    #to make sure that this iteration is exactly one second, the remaining time delay is added to each iteration of the loop
    
    delta = t2 - t1
    if delta < 1:
        time.sleep(1 - delta)
    
    i += 1

