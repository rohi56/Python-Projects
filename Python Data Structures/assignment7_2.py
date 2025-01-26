
fname = input("Enter file name: ")

try:
   
    fh = open(fname)
except FileNotFoundError:
    print("File not found:", fname)
    quit()

count = 0  
total = 0.0 
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        start = line.find(":") + 1
        value = float(line[start:].strip())
        total += value
        count += 1
if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No lines found with the pattern 'X-DSPAM-Confidence:'")
fh.close()
