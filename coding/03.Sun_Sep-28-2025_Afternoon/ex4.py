import re
def readMailLog(file):
    dit = {}
    list = []
    o = open(file, 'r')
    for i in o:
        check = re.findall('(\S+@\S+)', i)
        print(check)
    # return print(list)

readMailLog('../02.Sun_Sep-28-2025_Morning/mbox-short.txt')