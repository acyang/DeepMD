import matplotlib.pyplot as plt
import csv

plt.figure(dpi=300)
axes = plt.subplots(2, 1)

time = []
temp = []
press = []
etotal = []

with open('tdo.txt','r') as csvfile:
    for _ in range(1):
        next(csvfile)
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        time.append(float(row[0]))
        temp.append(float(row[2]))
        press.append(float(row[3]))
        etotal.append(float(row[8]))

#plt.plot(time,temp, color='#00aa00', label='Line 1')
plt.plot(time,press, color='#ff007f', label='Line 2')
#plt.plot(time,etotal, color='#bc007f', label='Line 3')

plt.legend(loc=2, title='abc', frameon=False)
plt.title('time v.s. temperature')
plt.axis([0, 200000, 260, 340])
plt.xlabel('time')
plt.ylabel('temperature (K)')
plt.grid(True, color='#ECE5DE', linestyle='solid')
plt.tick_params(axis='x', bottom=True, top=True)
plt.tick_params(axis='y', left=True, right=True)
plt.show()        
plt.savefig('time-thermo.png',dpi=300)