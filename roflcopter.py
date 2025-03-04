#RUN THIS ON CMD: The famous funny animated roflcopter from the 2000's

import time
import os

copter2 = '''                           
                           
    ROFL:ROFL:LOL:         
           ___^___ _       
       __/      []  \      
 LOL===__            \     
         \____________]    
              I   I        
         ----------/       '''


copter3 = '''                           
                           
             :LOL:ROFL:ROFL
           ___^___ _       
  L    __/      []  \      
  O ===__            \     
  L      \____________]    
              I   I        
         ----------/        '''

t = 0.05
while True:
    print(copter2)
    os.system('cls')
    time.sleep(t)
    print(copter3)
    os.system('cls')
    time.sleep(t)
