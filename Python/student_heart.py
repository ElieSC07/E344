import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    ######################################
    #plt.scatter(time, amplitude)
    #plt.show()
    bpm = 0
    Amp_array_length = len(amplitude)     
    time_array_length = len(time)    
    
    junp_time = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    period    = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    j = 0
 
    for i in range(2000, Amp_array_length - 1):
        if ( amplitude[i+1] - amplitude[i] ) > 4.2:
          if time[i] != 0: 
            junp_time[j] = time[i]*100000.0
            j = j + 1  
    
    for i in range(0, len(junp_time) -1 ):
        if junp_time[i] != 0 and junp_time[i+1] != 0:
           period[i] = junp_time[i+1] - junp_time[i]  
    #bpm = round(60000.0/period)
    #print(junp_time)
    #print(period) 
    index = np.count_nonzero(period) - 1
    #print(index)
    average_period = mean(period[0 : index])
    #print(average_period) 
    bpm = round(6000000.0/average_period)
    ######################################
        
    return bpm
        
