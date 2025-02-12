#Warning: Greedy matching
import re
x = 'From: Using the : character : show that there are new to add : forget previous'
print('greedy matching:') 
y = re.findall('^F.+:', x)
print(y)

print('\n\n\nnon-greedy matching:')
z = re.findall('^F.+?:', x)
print(z)