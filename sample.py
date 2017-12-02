# -*- coding: utf-8 -*-
import os
import sys
import heapq
import getopt
import math
"""
读取文件按照给出的行作为key
每个key中取出N行
"""

def init():
    '''
    #获取配置参数
    '''
    row = "1"
    delimiter = r"\t"
    number = "1"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hk:t:n:")
        for opt, arg in opts:
            if opt in ("-h"):
                print """
                      Command:
                         cat file |  python sample_tool.py [-k num,num | -t delimiter | -n quantity | -h ]
                      Options and arguments:
                         -h              :  help
                         -k num,num      :  sort by row number (default 1)
                         -t delimiter    :  delimiter (default table)
                         -n quantity     :  extract Specific quantity from every key's value(default 1)
                      """
                sys.exit()
            #按照哪行排序
            elif opt in ("-k"):
                row = arg
            #分隔符
            elif opt in ("-t"):
                delimiter = arg
            #每个key抽样数
            elif opt in ("-n"):
                number = arg
            else:
                print "wrong command,-h for help"
    except Exception as e:
        print e
    return [row, delimiter, number]

'''
main
'''
#配置文件处理
conf = init()
if conf != 0:
    #处理key
    rows = conf[0].split(",")
    s = ""
    max = 0
    keys = []
    for row in rows:
        keys.append(row)
        if(min < int(row)):
            max = int(row)

#读取标准输入
counter = 1
list = []
dict = {}
while True:
    line = sys.stdin.readline()
    if not line:
            break
    values = line.split()
    key = ""
    if(len(values)-1 < max):
         print "-k value larger than row the number of rows"
         sys.exit()

    #合成新key
    for row in keys:
        key += values[int(row)-1]
    if dict.has_key(key):
        dict[key].append(line)
    else:
        dict[key] = [line]

for (k,v) in dict.items():
    size = min(len(v), int(conf[2]))
    for l in range(0,size):
#strip去掉读取时候带的空格
        print v[l].strip()

