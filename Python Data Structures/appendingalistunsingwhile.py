#appending a list unsing while
numlist = list()
while True :
    inp = input('Enter a number:')
    if inp == 'done' :break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average:', average)
minimum = min(numlist)
print('Minimum:',minimum)
maximum = max(numlist)
print('Maximum:', maximum)
total = sum(numlist)
print('Total:', total)