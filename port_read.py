''' 
port csv  enhancement
We need to handle exception for data that is missing etc.
'''
import csv 
import glob
def read_portfolio(filename, error="silent"):
    if error not in  {'warn', 'raise', 'silent'}:
        raise ValueError("error must be one of 'warn','raise','silent'")
    #total = 0.0
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows) # skip the header row
        for rownum , row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if error == "warn":
                    print("Row num:",rownum , "Bad row: ", row)
                    print("Row num:","Reason: ", err)
                elif error == "raise":
                    raise
                else:
                    pass
                continue # skips
            #print(row)
            record = tuple(row)
            portfolio.append(record)
            #total += row[2] * row[3]

    return portfolio


portfolio = read_portfolio("share.csv")
print(portfolio)
total = 0.0
#one way to implement
#for holding in portfolio:
    #total += holding[2] * holding[3]
    
#second way to implement
for name, date, shares, price in portfolio:
    total += shares * price

print("Total Cost: ", total)
#print("Total Portfolio cost: {}".format(port_csvreader("share.csv")))