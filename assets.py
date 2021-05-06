from collections import defaultdict
from datetime import datetime
def assets(filename):
    dates=defaultdict(list)
    with open (filename, 'r') as file:
        header = "Asset# "+file.readline().strip()
        for line in file:
            model, created_date,name= line.strip().split()
            date=datetime.strptime(created_date, "%m/%d/%Y")
            dates[model[1:]].append(str(date) + ' ' + name)
    sorted_dates=sorted(dates.items(), key=lambda x:x[0])
    count=1
    print(header)
    for x,y in sorted_dates:
        y= sorted(y)
        for dates in y:
            date,time,name = dates.split()
            date=datetime.strptime(date, "%Y-%d-%m")
            date=datetime.strftime(date, "%m/%d/%Y")
            print(f'{count:0>6} A{x} {date} {name}')
            count+=1
assets('assets.txt')