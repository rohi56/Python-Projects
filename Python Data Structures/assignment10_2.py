name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts = dict()
for line in fh:
    if line.startswith("From "): 
        words = line.split()
        time = words[5]
        hours = time.split(':')
        act = hours[0]
        counts[act] = counts.get(act, 0) + 1

for k,v in sorted(counts.items()) :
    print(k,v)

#lst= list()
#lst = sorted([(v,k) for k,v in counts.items()])

#lst = sorted(lst, reverse=True)
#for v,k in lst :
    #print(k,v)
