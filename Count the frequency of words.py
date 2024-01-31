#Expriment No. - 08
#Title - Python program to count the frequency of words appearing in a string using a dictionary.
#Class - SY CSE
#Name -Sumedh Gajanan Kamble
#Roll No. -2005
#Subject - Python Programming

test_string=input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))
