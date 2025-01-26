#concatenating list using +
lugguage = ['shirts', 'jeans', 'jackets', 'watch', 'socks']
babylugguage = ['shirts', 'jeans', 'jackets', 'watch', 'socks','diaper']
finallugguage = lugguage + babylugguage
print('Complete lugguage to carry :', finallugguage)
count = 0
print('Below is the final list we have to carry')
for i in finallugguage :
    count = count + 1
    print(count, ':', i)

#Let's use slicing too :
print(finallugguage[4:])
print(finallugguage[2:8])
print(finallugguage[0:5])
print(finallugguage[:11])