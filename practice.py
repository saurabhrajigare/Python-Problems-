# 1) Implement Python's Range() Function.
x= range(3, 20, 2)
for n in x:
    print(n)

# 2) Write the generator Function to print prime Numbers.
def prime_num(n):
    prime=True
    i=2
    while(i<n):
        for a in range(2,i):
            if(i%a==0):
                prime=False
                break
        if(prime):
            yield i
# 3) Use Generators to read the file And Print all the words in a file.

file = open("assignment.txt", "r")
content=file.readline()
for line in content:
    words=line.split()
    for word in words:
        print(word+" ", end='')

#Q.Problem 1
import operator
def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

#Q.Problem 2    
def wrapper(f):
    def fun(l):
        ret_n= []
        for number in l:
            c = ""
            c = number[::-1][0:10][::-1]
            c= " ".join(["+91"] + [c[0:5], c[5:]])
            ret_n.append(c)
        f(ret_n)
    return fun

@wrapper
def sort_phn(l):
    print(*sorted(l), sep='\n')

