#Implement range function
friends = ['Joseph','glenn','sally']
for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year :', friend)

count = 0
for friend in friends :
    count = count + 1
    print(count, ':Happy New Year :', friend)
    
