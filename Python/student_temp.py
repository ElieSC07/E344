import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    ######################################
    
    temperature = 0    
    Amp_array_length = len(amplitude) 
      
    average = mean(amplitude[Amp_array_length-100 : Amp_array_length])

    temperature_prior_calibration = (5/3)*average + (203/6)  
    temperature = round(temperature_prior_calibration)    
        
    ######################################
        
    return temperature
        
