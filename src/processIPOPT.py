import os
import sys

log_file = sys.argv[1]
option = sys.argv[2]
f = open(log_file, "r")

print("Results:")
for line in f:
    if "Number of Iterations....:" in line and option=="-i":
        print(line)
    elif "Time to Solution........:" in line and option=="-t":
        print(line)