### genearate random password ###
# import random, string
# a = string.ascii_letters + string.digits + string.punctuation
# length = int(input('Length password\n'))
# password = ''
# for _ in range(length):
#     password = password + random.choice(a)
# print(password)

### blood donation ###
# type_blood = ['a', 'b', 'ab', 'o']
# donor = input('donor\n')
# recipient = input('recipient\n')
# if donor not in type_blood or recipient not in type_blood:
#     print('invalid input')
# elif donor == recipient:
#     print('yes')
# elif (donor != recipient) and (donor == 'o') and (recipient == 'a' or 'b' or 'ab'):
#     print('yes')
# elif (donor != recipient) and (recipient == 'ab') and (donor == 'a' or 'b' or 'o'):
#     print('yes')
# else:
#     print('no')

### take numbers from string and calc them ###
# strr = "Python31py50"
# new_strr = ''
# summ = 0
# counter = 0
# for digits in strr:
#     if digits.isdigit():
#         new_strr = new_strr + digits
# for number in new_strr:
#     summ = summ + int(number)
#     counter = counter + 1
#     avg = summ / counter
# print(f"The sum of the numbers is: {summ}")
# print(f"The average is: {avg}")

#
# new_dict = {"sahar": 80, "omer": 90}
# for key,value in new_dict.items():
#     maxi = max(new_dict.values())
# print(f"The max vaule is:{maxi, type(maxi)}")


#1. Write a program that takes a list of words as input and counts the frequency of each
#word. Store the word frequencies in a dictionary.
#
# words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# word_freq = {}
# for word in words:
#     if word in word_freq:
#         word_freq[word] += 1
#     else:
#         word_freq[word] = 1
# print(word_freq)


#2. Write a program to find the common elements between two dictionaries and store
#them in a new dictionary.

# words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# dictt = {}
# for word in words:
#     if word not in dictt:
#         dictt[word] = 1
# print(dictt)

#3. Write a program to calculate the sum of all the values in a dictionary that are
#integers.

# dictt = {'sahar': 1, 'tom': 2}
# summ = 0
# for key, value in dictt.items():
#     summ = summ + value
# print(summ)


#1. Extract first letter from each string
strings = ['foo', 'bar', 'baz']
new_strings = [print(letters[0]) for letters in strings]
# for letters in strings:
#     print(letters[0])
#2. Square numbers in list
nums1 = [1, 2, 3, 4, 5]
new_nums1 = [print(num**2) for num in nums1]
#3. Filter even numbers
nums2 = [1,2,3,4,5,6,7,8]
new_nums2 = [print(num) for num in nums2 if num % 2 == 0]
#4. Concatenate two lists
list1 = [1,2,3]
list2 = [4,5,6]
lst = []
#new_lst = [for num in list1]
for num in list1, list2:
    a = lst.append(num)
print(lst)


#5. String lengths to values dictionary (3:’foo’, 3:’bar’, 3:’baz’,’5:Messi’)
strings1 = ['foo', 'bar', 'baz', 'Messi']


#6. Filter strings without “mad”
strings2 = ['bad', 'mad', 'glad']
new_strings2 = []
for strr in strings2:
    if strr == "mad":
        new_strings2.append(strr)
print(new_strings2)

#7. Count strings with “a”
#List Comprehensions Exercises 2
strings3 = ['foo', 'bar', 'baz']

#8. Add trailing zeros (10, 20 , 30 , 40)
nums = [1, 2, 3, 4]
new_nums = []
for num in nums:
    num = str(num)+"0"
    print(num)

#9. Filter out empty strings
strings4 = ['', 'foo', '', 'bar', 'baz']
new_strings4 = []
for strr in strings4:
    if strr != '':
        new_strings4.append(strr)
print(new_strings4)
