def findUniqueWord(file):
    list = []
    readFile = open(file, 'r')
    for i in readFile:
        spl = i.strip().split(' ')
        for n in spl:
            if n not in list:
                list.append(n)
                list.sort()
    return print(list)

while True:
    inp = input('Please enter the file path to file unique word: ')
    try:
        findUniqueWord(inp)
        break
    except:
        print('file path does not exist')
        continue