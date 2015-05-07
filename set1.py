#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (1)
cnt = 0
for i, line in enumerate(open("address.txt","r")):
    cnt += 1
print cnt

# (2)
for line in open('address.txt', 'r'):
    itemList = line[:-1].split('\t')
    for item in itemList:
        print item + "",
    print ""


# (3)
c1 = open("col1.txt", "w")
c2 = open("col2.txt", "w")
for line in open("address.txt","r"):
    itemList = line[:-1].split("\t")
    c1.write(itemList[0]+"\n")
    c2.write(itemList[1]+"\n")


# (4)
data =[]
c1 = open("col1.txt","r")
c2 = open("col2.txt","r")
col1 = c1.readlines()
col2 = c2.readlines()

for i in range(len(col1)):
    line = []
    line.append(col1[0])
    line.append(col1[1])
    data.append(line)
print data


# (5)
import sys
f = open("address.txt","r")
if len(sys.argv) > 1:
    N = int(sys.argv[1])
    for i in range(N):
        line = f.readline()
        print line
else:
    print("Please enter arg int")



# (6)
import sys

num_lines = sum(1 for line in open("address.txt","r"))
if len(sys.argv) > 1:
    N = int(sys.argv[1])
    for i,line in enumerate(open("address.txt","r")):
        if i >= num_lines - N:
            print line
else:
    print("Please enter arg int")

# (7)
data = []
for line in  open("address.txt", "r"):
    itemList = line[:-1].split("\t")
    data.append(itemList)

li = []
for i in range(len(data)):
    li.append(data[i][0])

li_uniq = list(set(li))
print len(li_uniq)


# (8)
data = []
for line in  open("address.txt", "r"):
    itemList = line[:-1].split("\t")
    data.append(itemList)

data.sort(key=lambda x:x[1])
print data

# (9)
data = []
for line in  open("address.txt", "r"):
    itemList = line[:-1].split("\t")
    data.append(itemList)

data.sort(key=lambda x:(x[1],x[0]), reverse=True)
print data


# (10)
data = []

for line in open("col2.txt", "r"):
    data.append(line)

word_count = {}
for word in data:
    if word_count.has_key(word):
        word_count[word] += 1
    else:
        word_count[word] = 1
for w, c in sorted(word_count.iteritems(), key=lambda x: x[1], reverse=True):
    print w, c