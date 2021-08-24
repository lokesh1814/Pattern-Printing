# Pattern Printing
# take input = integer n
# Take boolean = True or False in form of 0 or 1
# If true and n=4, print
#*
#**
#***
#****

#And if false and n = 4, print
#****
#***
#**
#*

n = int(input("Enter number of rows:- "))
b = int(input("Enter your Boolean value:- "))

if b == 1:
    i = 1
    while i<=n:# n=5 i=5
        j = 1
        while j<=i:#i=5 j=5
            print("*", end=" ")
            j = j + 1

        print("")
        i = i + 1

else:
    i = n
    while i>=1:
        j = i
        while j>=1:
            print("*", end=" ")
            j = j - 1
        print("")
        i = i - 1