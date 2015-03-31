import sys

def bubbleSort(alist,size):
    for i in range(size):
        for j in range(i):
            if alist[j]>alist[j+1]:
                    temp = alist[j]
                    alist[j] = alist[j+1]
                    alist[j+1] = temp


file = open("input.data",'r')
size = int(file.readline())
num = file.readline();
sequence = []
for val in num.split():
    sequence.append(int(val))
bubbleSort(sequence,size)
file.close()

sum = 0
file = open("output.data",'w')
for val in sequence:
    sum = float(sum) + int(val)
    file.write(str(val))
    file.write(' ')
average = sum/size
file.write('\naverage = ')
file.write(str(average))
for val in sequence:
    t1 = float(val) - average
    t1 = t1 * t1
    sum = sum + t1
variance = sum/size
file.write('\nvariance = ')
file.write(str(variance))
file.close()
