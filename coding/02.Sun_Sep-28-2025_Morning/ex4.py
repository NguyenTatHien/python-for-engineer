def checkMailLog(file):
    readFile = open(file, 'r')
    list = []
    for i in readFile:
        if i.startswith('From:'):
            location = i.find(':')
            finalResult = i[location + 1:]
            list.append(finalResult.strip())
            list.sort()
    return print(list)
            
while True:
    inp = input('Please enter file path: ')
    try:
        checkMailLog(inp)
        break
    except:
        print('file path does not exist')
        continue