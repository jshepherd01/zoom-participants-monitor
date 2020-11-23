from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

headerstring = "timestamp (s),participants"

inp = input("Paste the output from retrieve.js : ")
inp = inp.strip()
inp = inp.split(",")

values = []
for i in range(0,len(inp),2):
    values.append([int(inp[i])//1000, int(inp[i+1])])

values.sort(key=lambda x: x[0])

try:
    f = open("output.csv")
    if f.read().startswith(headerstring):
        f.close()
        f = open("output.csv",'a')
        print("Updating output.csv")
        writebuff = "\n".join([""]+[",".join([datetime.fromtimestamp(i[0]).isoformat(' '), str(i[1])]) for i in values])
        f.write(writebuff)
        f.close()
    else:
        print("output.csv found but not valid, aborting save")
except FileNotFoundError:
    print("Creating output.csv")
    f = open("output.csv",'w')
    writebuff = "\n".join([headerstring]+[",".join([datetime.fromtimestamp(i[0]).isoformat(' '), str(i[1])]) for i in values])
    f.write(writebuff)
    f.close()

dates = [datetime.fromtimestamp(values[0][0])]
numbers = [values[0][1]]

for i in values[1:]:
    dates.append(datetime.fromtimestamp(i[0]))
    numbers.append(numbers[-1])
    
    dates.append(datetime.fromtimestamp(i[0]))
    numbers.append(i[1])

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.plot(dates,numbers)
plt.show()
