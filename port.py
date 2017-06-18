

# f = open('share.csv')

# for line in f:
#     print(line)


with open("share.csv", 'r') as f:
    headers = next(f)
    for line in f:
        line = line.strip() # strip of wite spaces
        parts = line.split(',')
        parts[0] = parts[0].strip('"')
        parts[1] = parts[1].strip('"')
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        print(parts)    