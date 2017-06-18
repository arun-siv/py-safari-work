''' 
we do not need the clean up when using csv module
#line = line.strip() # strip of white spaces
#parts = line.split(',') # split by comma
#parts[0] = parts[0].strip('"') # strips "
#parts[1] = parts[1].strip('"') # strips "

Also we can write a function
'''
import csv 
import glob
def port_csvreader(filename):
    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows) # skip the header row
        for row in rows:
        
            row[2] = int(row[2])
            row[3] = float(row[3])
            #print(row)
            total += row[2] * row[3]

    return total

shares = glob.glob('./*.csv')
for num in range(len(shares) - 1):
    print("The file name is {} and the portfolio cost is {}".format(shares[num], port_csvreader(shares[num])))

#print(shares)
#print("Total Portfolio cost: {}".format(port_csvreader("share.csv")))