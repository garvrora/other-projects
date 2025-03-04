import time
import winsound

def clock(clock_signal):
    minutes, seconds = divmod(clock_signal, 60)
    hours, minutes = divmod(minutes, 60)
    return (int(seconds), int(minutes), int(hours))

t0 = time.time()
while True:
    
    t1 = time.time()
    
    s, m, h = clock(t1-t0)
    
    if s < 10:
        s_zero = 0
    else:
        s_zero = ''

    if m < 10:
        m_zero = 0
    else:
        m_zero = ''
        
    
    print(f'{h} : {m_zero}{m} : {s_zero}{s}\n{art}',end = '\r')
    winsound.Beep(16000, 400)
    
    t2 = time.time()

    delta = t2 - t1
    if delta < 1:
        time.sleep(1 - delta)
    


