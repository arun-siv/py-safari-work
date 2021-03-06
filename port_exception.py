''' 
port csv  enhancement
We need to handle exception for data that is missing etc.
'''
import csv 
import glob
def port_csvreader(filename, error="warn"):
    if error not in  {'warn', 'raise', 'silent'}:
        raise ValueError("error must be one of 'warn','raise','silent'")
    total = 0.0
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
            total += row[2] * row[3]

    return total

shares = glob.glob('./*.csv')
for share in shares:
    print("The file name is {} and the portfolio cost is {}".format(share, port_csvreader(share, error="silent")))

#print(shares)
#print("Total Portfolio cost: {}".format(port_csvreader("share.csv")))