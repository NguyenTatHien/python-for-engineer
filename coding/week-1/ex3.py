def grossPayIfOver40(h, r):
    if (h > 40):
        regularPay = 40 * r
        overTimeHour = h - 40
        overTimeRate = r * 1.5
        overTimePay = overTimeHour * overTimeRate
        return regularPay + overTimePay
    return h * r

inputHour = float(input('Enter the hours: '))
inputRate = float(input('Enter the rate: '))

print('Your gross pay is:', grossPayIfOver40(inputHour, inputRate))