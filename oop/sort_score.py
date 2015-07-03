import sys
from string import rstrip

class student(object):
    def __init__(self, name = None, studentid = 0, score = 0):
        self.name = name
        self.studentid = studentid
        self.score = score

def read_score(alist,size):
    for i in range(size):
        line = sys.stdin.readline().rstrip('\n') # read a line from stdin
        data = line.split(' ')
        alist.append(student(str(data[0]), int(data[1]), float(data[2])))
    return alist

num_stu = int(input()) # read a int
studentlist = []
studentlist = read_score(studentlist, num_stu)

import operator
studentlist.sort(key = operator.attrgetter('score','studentid'))

for student in studentlist:
    print "%s %s %s" % (student.name, student.studentid, student.score)
