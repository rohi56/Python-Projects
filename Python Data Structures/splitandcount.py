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
        val = list()
        val = line.split()
        print(val[1])

average = sum(val)/len(val)
print(average)