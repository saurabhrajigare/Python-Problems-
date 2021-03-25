#1)write a Python program to read data from a file which has text containing emails, 
#write only the emails from the file into another file. 
#You can use 're' module to extract emails from the text file.
import re
sp =open("module.txt", 'r')
for line in sp:
    line=line.strip()
    content= re.findall('[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+',line)
    c1= '\n'.join(content)
    print(content)
    f = open("newfile.txt",'w')
    f.write(c1)
    f.close()


# 2)Create a deque and do Queue operations on it based on FIFO approach. 
# use 'time' module to time your python code.
# Display the time taken to insert an item to deque and to remove an item.
from collections import deque
from time import time

q = deque() 
start_time = time()
q.append('A')                                  
q.append('B')
q.append('C')
print("Initial queue :-",q)
print("Time taken to Insert:-", (time() - start_time))

start_time1 = time()

print("\nElements dequeued from the queue")
print(q.popleft())
print("\nQueue after removing elements",q)
print("Time taken to Remove:-", (time() - start_time1))







