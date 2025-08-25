#1. Convert the time entered in hh,min and sec into seconds.
H = int(input("Enter Hours - "))
M = int(input("Enter Minutes - "))
S = int(input("Enter Seconds - "))

T = H*3600 + M*60 + S
print ('Total Time in Seconds is ',T)
