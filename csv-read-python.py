import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('pleiadesdata.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[3]))
        y.append(float(row[1]))
        
plt.scatter(x,y,label='Test')
plt.xlabel('Coulour Index')
plt.ylabel('V mag')
plt.title('Test of a csv data')
plt.legend()
plt.show()
