def bubbleSort(alist,size):
    for i in range(size-1,0,-1):
        for j in range(i):
            if alist[j]>alist[j+1]:
                    temp = alist[j]
                    alist[j] = alist[j+1]
                    alist[j+1] = temp


def c_average(alist,size):
    sum = 0
    for val in alist:
        sum = sum + float(val)
    return sum/size

def c_variance(alist,average,size):
    sum = 0
    for val in alist:
        tmp = float(val) - average
        tmp = pow(tmp, 2)
        sum = sum + tmp
    return sum/size

with open("testcase/input.data",'r') as file:

    size = int(file.readline())
    num_sequence = file.readline();
    score_list = []
    # split the number score_list, default is by the whitespace
    for score in num_sequence.split():
        score_list.append(int(score))
    bubbleSort(score_list,size)

file.close()

with open("testcase/output.data",'w') as file:

    for score in score_list:
        file.write(str(score) + ' ')

    average = c_average(score_list, size)
    file.write('\naverage = ' + str(average) + '\n')

    variance = c_variance(score_list, average, size)
    file.write('variance = ' + str(variance) + '\n')

file.close()
