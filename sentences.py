import re
import csv


file = open('Sapiens.txt')

book = file.read()

sentences = re.findall(r"([^(.|?)]*?years ago[^.]*\.)", book)

count = 0
dates = list()
for x in sentences:
    before = x.split("years ago")[0]
    after = x.split("years ago")[1]
    last = before.split()[-1]

    if "," in last:
        last = last.replace(",", "")

    if last.isdigit():
        count += 1
        last = int(last)
    elif 'million' in last:
        count += 1
        last = 1000000
        if before.split()[-2] == 'Two':
            last *= 2
        elif before.split()[-2] == 'Sixty-five':
            last *= 65
        else:
            if before.split()[-2] != 'a':
                last *= int(before.split()[-2])
    elif 'billion' in last:
        count += 1
        last = 1000000000
        last *= int(before.split()[-2])
    elif 'thousand' in last:
        count += 1
        last = 1000
        if before.split()[-2] == 'Two':
            last *= 2
        elif before.split()[-2] == 'Thirty':
            last *= 30
        elif before.split()[-2] == 'Ten':
            last *= 10
        else:
            if before.split()[-2] != 'a':
                last *= int(before.split()[-2])
    else:
        continue
    pair = [last, x.strip()]
    dates.append(pair)
dates = sorted(dates)
print("expected: " + str(count))
print("actual: " + str(len(dates)))

with open('dates.csv', 'w') as csvfile:
    fieldnames = ['date', 'events']
    writer = csv.writer(csvfile)
    for row in dates:
        writer.writerow(row)
