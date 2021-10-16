import random
import numpy as np
import time


def months4car(price, down_pay, monthlysaving, annualreturn):
    current_savings = 0
    months = 0
    
    while (current_savings < price):
        current_savings = current_savings + monthlysaving
        current_savings = current_savings + (current_savings * (annualreturn/12))
        months = months + 1
        if (current_savings >= down_pay):
            current_savings = current_savings - down_pay
            price = price - down_pay
            down_pay = price
    return months




start1 = time.time() # record start time
print( months4car(50000, 10000, 200, 0.04) )
end1 = time.time()  # record end time
time1 = end1 - start1 # test timing
print(time1)


start2 = time.time() # record start time
print( months4car(50000, 10000, 2000, 0.04) )
end2 = time.time()  # record end time
time2 = end2 - start2 # test timing
print(time2)