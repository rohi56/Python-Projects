fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
for line in fh:
    if line.startswith("From "): 
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
max_email = None
max_count = None
for email, count in counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count

print(max_email, max_count)
