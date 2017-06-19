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
            record = {
                "name" : row[0],
                "date": row[1],
                "shares": row[2],
                "price": row[3]
            }
            portfolio.append(record)
            #total += row[2] * row[3]

    return portfolio


portfolio = read_portfolio("share.csv")


total = 0.0

for holding in portfolio:
    total += holding['shares'] * holding['price']
    


print("Total Cost: ", total)
#print("Total Portfolio cost: {}".format(port_csvreader("share.csv")))

#dict 
#import json
#json.dumps(portfolio)
#json.loads("json file")


# few data calculation

for holding in portfolio:
    print(holding)

# example 1 -> collects all share names
shares = [] 
for holding in portfolio:
    shares.append(holding['name'])
print(shares)

#exampl 2 -> does some filtering

more100  = []
for holding in portfolio:
    if holding['shares'] > 100:
        more100.append(holding)
print(more100)