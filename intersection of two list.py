#Expriment No. - 03
#Title - Python program to find the intersection of two lists.
#Class - SY CSE
#Name-Sumedh Gajanan Kamble
#Roll No. -2005
#Subject - Python Programming
def intersection_list(l1, l2):
   return list(set(l1) & set(l2))
  
l1 = []
num1 = int(input('Enter size of list 1: '))
for n in range(num1):
    numbers1 = int(input('Enter any number:'))
    l1.append(numbers1)
print('The lists is:',l1)

l2 = []
num2 = int(input('Enter size of list 2:'))
for n in range(num2):
    numbers2 = int(input('Enter any number:'))
    l2.append(numbers2)
print('The lists is:',l2)
  
print('The intersection of two lists is:', intersection_list(l1, l2))  

