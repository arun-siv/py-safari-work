

#set initial values

emi = 27000
rate = 0.0995
principle = 2800000
total_paid = 0

#month = 0 
month = 0 

#output to file
out = open("schedule.txt", 'w') #open file for writing

#print the header
print('{:>5s} {:>10s} {:>10s} {:>10s}'.format("Month", "Interest", "Principle", "Outstanding"), file=out)
while principle > 0: 
    month += 1
    interest = principle * (rate/12)
    principle = principle + interest - emi
    total_paid += emi
    print('{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}'.format(month, interest , emi-interest , principle), file=out)
    #print(month, interest, emi - interest , principle)
out.close()
print("Total paid is = {}".format(total_paid));