str = 'X-DSPAM-Confidence: 0.8475'
a = str.find(':')
print(float(str[a+1:].strip()))