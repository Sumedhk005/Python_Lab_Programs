#Expriment No. - 06
#Title - Python program to check if a substring is present in a given string.
#Class - SY CSE
#Name -Sumedh Gajanan Kamble
#Roll No. -2005
#Subject - Python Programming


string=input("Enter string:")
sub_str=input("Enter word:")
if(string.find(sub_str)==-1):
      print("Substring not found in string!")
else:
      print("Substring in string!")
