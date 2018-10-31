import numpy as np
import matplotlib.pyplot as plt
import csv

#Prepare data
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


#plt.figure(dpi=300)
fig, axes = plt.subplots(2, 1)
axes[0].plot(time,temp, color='#00aa00', label='Line 1')
axes[1].plot(time,press, color='#ff007f', label='Line 2')
#plt.plot(time,etotal, color='#bc007f', label='Line 3')

#axes[0].legend(loc=2, title='abc', frameon=False)
#axes[0].title('time v.s. temperature')
axes[0].axis([0, 200000, 260, 340])
#axes[0].set_xlabel('time')
axes[0].set_ylabel('temperature (K)')
axes[0].grid(True, color='#ECE5DE', linestyle='solid')
axes[0].tick_params(axis='x', bottom=True, top=True)
axes[0].tick_params(axis='y', left=True, right=True)

#axes[1].legend(loc=2, title='abc', frameon=False)
#axes[1].title('time v.s. temperature')
axes[1].axis([0, 200000, -20000, 20000])
axes[1].set_xlabel('time')
axes[1].set_ylabel('presure (bars)')
axes[1].grid(True, color='#ECE5DE', linestyle='solid')
axes[1].tick_params(axis='x', bottom=True, top=True)
axes[1].tick_params(axis='y', left=True, right=True)
#plt.title('time v.s. temperature')
plt.show()        
plt.savefig('time-thermo.png',dpi=300)


#
#fig, ax1 = plt.subplots()
#
#color = 'tab:red'
#ax1.set_xlabel('time (s)')
#ax1.set_ylabel('exp', color=color)
#ax1.plot(t, data1, color=color)
#ax1.tick_params(axis='y', labelcolor=color)
#
#ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#
#color = 'tab:blue'
#ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
#ax2.plot(t, data2, color=color)
#ax2.tick_params(axis='y', labelcolor=color)
#
#fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()