# def FizzBuzz (lst):
#     for number in lst:
#         if number % 3 == 0 and number % 5 == 0:
#             print(f"The number is: {number}, FizzBuzz")
#         elif number % 3 == 0:
#             print(f"The number is: {number}, Fizz")
#         elif number % 5 == 0:
#             print(f"The number is: {number}, Buzz")
#         else:
#             print(f"The number is: {number} Not Fizz or Buzz ot FIzzBuzz")
#     return lst
# print(FizzBuzz(range(0, 10)))
#
#
# def odd_number(lst):
#     new_lst = []
#     for number in lst:
#         if number % 2 == 0:
#             new_lst.append(number)
#     return new_lst
# lst = [1, 4, 5]
# print(f"The number is: {odd_number(lst)} and is odd number")

#
lst = [1, 3, 5, 7]
new_lst = []
total = 0
for number in lst:
    if number > 3:
        total = total + number
#         new_lst.append(number)
#         print(new_lst)
# for new in range(len(new_lst)):
#     calc = new_lst[new - 1] + new_lst[new - 2]
print(total)
#
#

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
lst = my_str.split()
print(f"my mac adderss is: {lst[4]}", type(lst))

name = "sahar"
check_name = name[::-1]
test = "aa"
check_test = test[::-1]

if name == check_name:
    print('its polindrom')
else:
    print("it's not a polindrom")

if test == check_test:
    print('its polindrom')
else:
    print("it's not a polindrom")


# strr = input("add string\n")
# print(strr[0:2]+strr[-1])

lst = ["sahar", "moshe", "yakov"]
strr = " ".join(lst)
print(strr, type(strr))

type_blood = ['a', 'b', 'ab', 'o']
print(f'This type of blood: {type_blood}')
donor = input("donor\n")
recipient = input("recipient\n")
if recipient or donor != type_blood:
  print("invalid input")
elif recipient != donor:
  print("recipient != donor")
  if donor == 'ab' and recipient == 'b' or 'a' or 'o':
    print('yes')
  elif recipient == 'o' and donor == 'a' or 'b' or 'ab':
    print('yes')
else:
  print('yes')

strr = "dsaf324dsf"
new_strr = []
for digit in strr:
    if digit.isdigit():
        new_strr.append(digit)
print(new_strr)
##################
num = 0
while 10 > num:
    num = num + 1
    print(num)
##################
lst = []
for num in range(1, 6):
    lst.append(num)
    print(lst)
#######################
# n = int(input("Input number"))
# calc = sum(range(1, n+1))
# print(calc)
# #######################
# store = 0
# num = int(input("Add number"))
# for n in range(1, num):
#     store = n * num
#     print(store)
#########################
numbers = [12, 75, 150, 180, 145, 525, 50]
new_num = []
#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop
for num in numbers:
    if num % 5 == 0 and num < 150:
        new_num.append(num)
    elif num > 150:
        continue
    elif num > 500:
        break
print(new_num)
#############################
str1 = "123asdfgh45"
str2 = "123asedfde45"
if str1[6] == "d" and str1[7] == "e" or str1[7] == "f":
    print("version A")
else:
    print("version B")

if str2[6] == "d" and (str2[7] == "e" or str2[7] == "f"):
    print("version A")
else:
    print("version B")

# import random, string
# chars = string.ascii_letters + string.digits + string.punctuation
# c = int(input("How many chars?\n"))
# lst = ''
# for char in range(c):
#     password = random.choice(chars)
#     lst = lst + password
print(lst)
name = "sahar"
new_name = name.isupper()
print(new_name)
name = "Alex Kuznetsov"
upper = []
lower = []
for letter in range(len(name)):
    if name[letter].isupper():
        upper.append(name[letter])
    elif name[letter].islower():
        lower.append(name[letter])
print(f"The amount of upper is: {len(upper)} and lower is :{len(lower)}")

# Input_list = [1,2,3,3,3,3,4,5]
# new_lst = []
# for number in range(len(Input_list)):
#     if Input_list[number] != :
#         new_lst.append(Input_list[number])
# print(new_lst)
# lst = ''
# for num in range(1, 9):
#     lst = lst + str(num)
#     print(lst)
#
# counter = 0
# for num in range(1, 11):
#     print(num)
#     print("################")
#     counter = counter + num
# print(counter)
#
# strr = "asdrwaqaq"
# if len(strr) < 10:
#     print("Please insert minimum 10 letter")
#     counter = 0
#     for letter in strr:
#         if letter == "a":
#             counter = counter + 1
#     print(counter)
#
# s = input("Add string\n")
# new_s = s[-2:]
# print("moshe"+new_s)
#
# a = "asdf"
# print(a[-2:])


a = 3
summ = 0
for i in range(1, a+1):
    summ = summ + i
print(summ)



lst1 = [1, 2, 3, 3, 5]
lst2 = []
for num in lst1:
    if num != lst1:
        lst2.append(num)
print(lst2)


def poli (strr):
    if strr == strr[::-1]:
        print(True)
    else:
        print(False)
print(poli(("211112")))
print(poli("AlulA"))
print(poli("AnnA"))
print(poli("DeifieD"))
