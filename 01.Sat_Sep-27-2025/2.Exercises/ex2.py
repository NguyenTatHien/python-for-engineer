def grossPay(h, r):
    return h * r

inputHour = float(input('Enter the hours: '))
inputRate = float(input('Enter the rate: '))

print('Your gross pay is:', grossPay(inputHour, inputRate))