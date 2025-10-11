def computePay(h, r):
    if (h > 40):
        regularPay = 40 * r
        overTimeHour = h - 40
        overTimeRate = r * 1.5
        overTimePay = overTimeHour * overTimeRate
        return regularPay + overTimePay
    return h * r

while True:
    try:
        inputHour = float(input('Enter the hour: '))
        inputRate = float(input('Enter the rate: '))
        print('Your gross pay is:', computePay(inputHour, inputRate))
        break
    except:
        print('Error, please enter numeric input')
        continue
    
