#Expriment No. - 05
#Title - Python program to count the occurrences of each word in a given string sentence.
#Class - SY CSE
#Name -Sumedh Gajanan Kamble
#Roll No. -2005
#Subject - Python Programming


string = input("Enter string: ")
word=input("Enter word:")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Count of the word is:")
print(count)
