count = 0
total = 0
while True:
    try:
        inp = input('Enter a number: ')
        if (inp != 'done'):
            total += float(inp)
            count += 1
        else:
            average = total / count
            print('Count: ', count)
            print('Total: ', total)
            print('Average: ', average)
            break
    except:
        print('Invalid input')
        continue