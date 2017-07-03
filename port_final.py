
import csv
import glob
import os

def read_portfolio(path=os.getcwd()):
    ''' Read the portfolio from a file'''

    portfolio = []
    files = glob.glob(path +"/*.csv")
    for filename in files:
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            header = next(rows)
            for row in rows:
                try:
                    row[2] = int(row[2])
                    row[3] = float(row[3])
                except ValueError as err:
                    continue
                
                record = {
                    'name': row[0],
                    'date':row[1],
                    'quantity': row[2],
                    'price': row[3]
                }
                portfolio.append(record)
                
    return portfolio
            



read_portfolio()