#Implement list:
count = 0
luggage = ['shirt','pants','socks','watch','sweater']
for items in luggage :
    count = count + 1
    print(count, ':', items)
    #print('You have put', items, 'in luggage')
print('You have put', count, 'items in lugguage')
print('Done')
#Instead of pants put jeans.
luggage[1] = 'jeans'
print('Below is updated list:')
count = 0
for items in luggage :
    count = count + 1
    print(count, ':', items)
print('We have seen list is mutable')
#Let's also check the length of list
print('The Lenght of the list luggage is :', len(luggage))

