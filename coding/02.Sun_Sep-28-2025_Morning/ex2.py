def averageFromFile(file):
    o = open(file, 'r')
    total = 0
    count = 0
    for i in o:
        if (i.startswith('X-DSPAM-Confidence:')):
            f = i.find(':')
            trueLocation = f + 1
            count += 1
            total += float(i[trueLocation:].strip())
    return print(total / count)
while True:
    inp = input('Please enter file path: ')
    try:
        averageFromFile(inp)
        break
    except:
        print('Please enter existing filePath')
        continue