# def poli (abba):
#     return abba == abba[::-1]
# print(poli("abba"))

# type_blood = ['a', 'b', 'ab', 'o']
# print(f'This type of blood: {type_blood}')
# donor = input("donor\n")
# recipient = input("recipient\n")
# if recipient or donor != type_blood:
#   print("invalid input")
# elif recipient != donor:
#   print("recipient != donor")
#   if donor == 'ab' and recipient == 'b' or 'a' or 'o':
#     print('yes')
#   elif recipient == 'o' and donor == 'a' or 'b' or 'ab':
#     print('yes')
# else:
#   print('yes')


# def summ():
#     #summ = float(a) + float(b)
#     a = float(input("Add number\n"))
#     b = float(input("Add number\n"))
#     c = a + b
#     return c
# print(f"Your sum is: {summ()}")


# lst1 = [1, 2, 3, 4, 5]
# lst2 = [4, 5, 6, 7, 8]
# lst3 = []
# for num in lst1:
#     if num == lst2:
#         lst3.append(num)
# print(lst3)


# lst4 = [1, 2, 3, 2, 4, 3, 5]
# lst5 = []
# for num in lst4:
#     if num not in lst5:
#         lst5.append(num)
# print(lst5)
#
# words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# count = 0
# for word in words:
#     if word == "apple":
#         count = count + 1
#     if word == "b"
# print(count)
#
# number = int(input("Input number\n"))
# print(f"The sum of your number is: {sum(range(number+1))}")
#
# list1 = [10, 20, 30, 40, 50]
# print(list1[::-1])
#
# for num in range(-10, 0):
#     print(num)
#
# for i in range(5):
#     print(i)
# else:
#     print("Done")
#
# fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for num in range(len(fibo)):
#     if fibo[num - 1] - fibo[num - 2] == fibo[num - 3]:
#         print("Fibo")
#     else:
#         print("Not Fibo")
#
# fact = 1
# for num in range(1, 5):
#     fact = fact * num
# print(fact)

#
# tot = ""
# new_tot = "****"
# # for _ in range(0, 6):
# #     tot = tot + "*"
# #     print(tot)
# for _ in range(0, 4):
#     new_tot = new_tot - "*"
#     print(new_tot)
# num = int(input("input number\n"))
# lst = [1, 2, 3, 4, 5]
# for _ in lst:
#     if num % 3 == 0:
#         print(f"Your num is: {num}, is divided by 3")

# strr = input("Add string with capital letters")
# lst = []
# for letter in strr:
#     if letter.isupper():
#         lst.append(lst)
# print(f"The amount of capital letters is: {len(lst)}")

# strr = "Python31py50"
# lst = []
# for digits in strr:
#     if digits.isdigit():
#         lst.append(digits)
# new_strr = "".join(lst)
# summ = 0
# for number in new_strr:
#     summ = summ + int(number)
# print(summ)

#
strr = "Python31py50"
new_strr = ''
summ = 0
counter = 0
for digits in strr:
    if digits.isdigit():
        new_strr = new_strr + digits
for number in new_strr:
    summ = summ + int(number)
    counter = counter + 1
    avg = summ / counter
print(f"The sum of the numbers is: {summ}")
print(f"The average is: {avg}")

type_blood = ['a', 'b', 'ab', 'o']
donor = input('donor\n')
recipient = input('recipient\n')
if donor not in type_blood or recipient not in type_blood:
    print('invalid input')
elif donor == recipient:
    print('yes')
elif (donor != recipient) and (donor == 'o') and (recipient == 'a' or 'b' or 'ab'):
    print('yes')
elif (donor != recipient) and (recipient == 'ab') and (donor == 'a' or 'b' or 'o'):
    print('yes')
else:
    print('no')

# print('#'*5)
# fruits = ['apple', 'banana', 'cherry']
# fruits.append('date')
# print(fruits)
# print(len(fruits))
# fruits.remove('apple')
# print(fruits)
# order = fruits.sort()
# print(order)
# sett = {3, 1, 4, 1, 5, 9}
# print(7 in sett)
# tuplee = ('dog', 'cat', 'fish')
# print(tuplee[2])
# lst = list(tuplee)
# print(lst, type(lst))
# lstt = [[10, 20], [30, 40]]
# print(lstt[1][1])
# print(max(12, 5, 8))
#
# def multiply_numbers(num1, num2):
#     # num1 = input("input num1\n")
#     # num2 = input("input num2\n")
#     return num1*num2
# print(multiply_numbers(4,7))
#
# def calculate_square(num):
#     return num**2
# print(calculate_square(6))
#
# def calculate_average(lst):
#     counter = 0
#     summ = 0
#     for num in lst:
#         summ = summ + num
#         counter = counter + 1
#     return summ/counter
# print(calculate_average([3, 4, 5]))
#
#
import random, string
a = string.ascii_letters + string.digits + string.punctuation
length = int(input('Length password\n'))
password = ''
for _ in range(length):
    password = password + random.choice(a)
print(password)


#1. Write a program that checks if a given number is positive, negative, or zero.
# num = float(input('num\n'))
# if num < 0:
#     print(f"Your name is:{num} and it's negative")
# elif num > 0:
#     print(f"Your name is:{num} and it's positive")
# else:
#     print(print(f"Your name is:{num} and it's zero"))


#2. Write a program that determines whether a given year is a leap year or not.


#3. Write a program that checks if a given number is even or odd.

lst = [1, 2, 4.5]
odd = []
for num in lst:
    if num % 2 == 0:
        odd.append(num)
print(f"Your name is: {odd} and it's odd number ")

#4. Write a program that determines the largest of three given numbers.

lst = [1, 4, 3.5]
maxi = lst[0]
for num in lst:
    if num > maxi:
        maxi = num
print(maxi)

#5. Write a program that checks if a given character is a vowel or a consonant.


#6. Write a program that determines if a given string is a palindrome.


#7. Write a program that calculates the grade based on a given percentage.
#8. Write a program that determines if a given year is a century year or not.
#9. Write a program that checks if a given number is a perfect square.
#10. Write a program that determines the type of triangle based on given side lengths(equilateral, isosceles, or scalen)


# strr1 = 'sadfsdf'
# strr2 = 'azggza'
# print(strr2[0:2])
# print(strr2[-1:-3])
# #str1[:2] == str1[-1:-3:-1]
# if (len(strr1) % 2 == 0) and (strr1[0:2] == strr1[-2:]) and (strr1[3] == 'g' or 'G'):
#     print('yes')
# else:
#     print('no')
# if (len(strr2) % 2 == 0) and (strr2[0:2] == strr2[-1:-3:-1]) and (strr2[2] == 'g' or 'G'):
#     print('yes')
# else:
#     print('no')

lst1 = [1, 3, 5]
lst2 = [1, 7, 3]
new_lst = []
for num in lst1:
    if num in lst2:
        new_lst.append(num)
print(new_lst)

# לשאול את תום מה זה prime number
# לא הבנתי את התשובה שת chatgpt
