text = "X-DSPAM-Confidence:    0.8475"
pos1 = text.find('0')
sflt = text[pos1:]
fltnum = float(sflt)
print(fltnum)
