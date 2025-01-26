text = "X-DSPAM-Confidence:    0.8475"
pre = text.find('0')
pos = (text[pre:pre+10])
i = float(pos)
print(i)