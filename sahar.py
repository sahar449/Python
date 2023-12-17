# # ## genearate random password ###
# # import random, string
# # a = string.ascii_letters + string.digits + string.punctuation
# # length = int(input('Length password\n'))
# # password = ''
# # for _ in range(length):
# #     password = password + random.choice(a)
# # print(password)
# #
# # ## blood donation ###
# # type_blood = ['a', 'b', 'ab', 'o']
# # donor = input('donor\n')
# # recipient = input('recipient\n')
# # if donor not in type_blood or recipient not in type_blood:
# #     print('invalid input')
# # elif donor == recipient:
# #     print('yes')
# # elif (donor != recipient) and (donor == 'o') and (recipient == 'a' or 'b' or 'ab'):
# #     print('yes')
# # elif (donor != recipient) and (recipient == 'ab') and (donor == 'a' or 'b' or 'o'):
# #     print('yes')
# # else:
# #     print('no')
# #
# # ## take numbers from string and calc them ###
# # strr = "Python31py50"
# # new_strr = ''
# # summ = 0
# # counter = 0
# # for digits in strr:
# #     if digits.isdigit():
# #         new_strr = new_strr + digits
# # for number in new_strr:
# #     summ = summ + int(number)
# #     counter = counter + 1
# #     avg = summ / counter
# # print(f"The sum of the numbers is: {summ}")
# # print(f"The average is: {avg}")
# #
# #
# # new_dict = {"sahar": 80, "omer": 90}
# # for key,value in new_dict.items():
# #     maxi = max(new_dict.values())
# # print(f"The max vaule is:{maxi, type(maxi)}")
# #
# #
# # #1. Write a program that takes a list of words as input and counts the frequency of each
# # #word. Store the word frequencies in a dictionary.
# #
# # words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# # word_freq = {}
# # for word in words:
# #     if word in word_freq:
# #         word_freq[word] += 1
# #     else:
# #         word_freq[word] = 1
# # print(word_freq)
# #
# #
# # #2. Write a program to find the common elements between two dictionaries and store
# # #them in a new dictionary.
# #
# # words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# # dictt = {}
# # for word in words:
# #     if word not in dictt:
# #         dictt[word] = 1
# # print(dictt)
# #
# # #3. Write a program to calculate the sum of all the values in a dictionary that are
# # #integers.
# #
# # dictt = {'sahar': 1, 'tom': 2}
# # summ = 0
# # for key, value in dictt.items():
# #     summ = summ + value
# # print(summ)
# #
# #
# # #1. Extract first letter from each string
# # strings = ['foo', 'bar', 'baz']
# # new_strings = [print(letters[0]) for letters in strings]
# # # for letters in strings:
# # #     print(letters[0])
# # #2. Square numbers in list
# # nums1 = [1, 2, 3, 4, 5]
# # new_nums1 = [print(num**2) for num in nums1]
# # #3. Filter even numbers
# # nums2 = [1,2,3,4,5,6,7,8]
# # new_nums2 = [print(num) for num in nums2 if num % 2 == 0]
# # #4. Concatenate two lists
# # list1 = [1,2,3]
# # list2 = [4,5,6]
# # lst = []
# # #new_lst = [for num in list1]
# # for num in list1, list2:
# #     a = lst.append(num)
# # print(lst)
# #
# #
# # #5. String lengths to values dictionary (3:’foo’, 3:’bar’, 3:’baz’,’5:Messi’)
# # strings1 = ['foo', 'bar', 'baz', 'Messi']
# #
# #
# # #6. Filter strings without “mad”
# # strings2 = ['bad', 'mad', 'glad']
# # new_strings2 = []
# # for strr in strings2:
# #     if strr == "mad":
# #         new_strings2.append(strr)
# # print(new_strings2)
# #
# # #7. Count strings with “a”
# # #List Comprehensions Exercises 2
# # strings3 = ['foo', 'bar', 'baz']
# #
# # #8. Add trailing zeros (10, 20 , 30 , 40)
# # nums = [1, 2, 3, 4]
# # new_nums = []
# # for num in nums:
# #     num = str(num)+"0"
# #     print(num)
# #
# # #9. Filter out empty strings
# # strings4 = ['', 'foo', '', 'bar', 'baz']
# # new_strings4 = []
# # for strr in strings4:
# #     if strr != '':
# #         new_strings4.append(strr)
# # print(new_strings4)
# #
# # ### question from interview ###
# # version = 'build.1.17.18'
# # split = version.split('.')
# # new_version = int(split[3])
# # print(new_version, type(new_version))
# # for num in range(11):
# #     new_version = new_version + 1
# #     print(f"The num version is: {new_version}")
# #
# #
# # dictt = {'sahar': 40, 'omer': 50}
# # maxi = dictt['sahar']
# # print(maxi, type(dictt))
# # for k, v in dictt.items():
# #     if v > maxi:
# #         maxi = v
# #         name = k
# # print(f"The max number is: {maxi} and the name is: {name}")
# #
# #
# # visits = {'Monday': 5000,
# #           'Tuesday': 3000,
# #           'Wednesday': 4000,
# #           'Thursday': 4500,
# #           'Friday': 5000,
# #           'Saturday': 2000,
# #           'Sunday': 1500
# #           }
# # total = 0
# # for k, v in visits.items():
# #     total = total + v
# # print(total)
# #
# # words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# # words_and_length = dict()
# # for w in words:
# #     words_and_length[w] = len(w)
# # print(words_and_length)
# #
# #
# # dictt = {'sahar': 33, 'tom': 23}
# # dictt['moshe'] = 28
# # print(dictt)
# #
# # names = {'sahar': 33, 'tom': 24}
# # names['moshe'] = 29
# # print(names)
#
# people = ['tom', 'sahar', 'moshe', 'moshe']
# new_people = {}
# for name in people:
#     if name in new_people:
#         new_people[name] = new_people[name] + 1
#     else:
#         new_people[name] = 1
# print(max(new_people, key=new_people.get))


# text = "aaabbbccccbb"
# letters = {}
# count = []
# for letter in range(len(text)-1):
#     if text[letter] == text[letter + 1]:
#         count.append(text[letter])
# print(count)
#
# def maxi (lst):
#     maxi = lst[0]
#     for number in lst:
#         if number > maxi:
#             maxi = number
#     return maxi
# print(f"The max number is: {maxi([5 ,3, 8])}")

# def fibo(lst):
#     for num in range(len(lst)-2):
#         if lst[num] + lst[num+1] == lst[num+2]:
#             print('Fibo')
#         else:
#             print('not fibo')
#             #break
# print(fibo([1, 2, 3, 4]))

# def fact(lst):
#     summ = 0
#
# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# dictt = {}
# for letter in words:
#     dictt[letter] = len(letter)
# print(dictt)
#
# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash', 'Python']
# dictt = {}
# for element in words:
#     if element in dictt:
#         dictt[element] = dictt[element] + 1
#     else:
#         dictt[element] = 1
# print(dictt)
#


#1. Write a program that takes a list of words as input and counts the frequency of each
#word. Store the word frequencies in a dictionary.

words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash', 'Python']
dictt = {}
for element in words:
    if element in dictt:
        dictt[element] = dictt[element] + 1
    else:
        dictt[element] = 1
print(dictt)

#2. Write a program to find the common elements between two dictionaries and store
#them in a new dictionary.

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 3, "d": 4}
common = {}
for k, v in dict1.items():
    if [k, v] in dict2.items():
        common[k, v] = k, v
print(common)

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 1, "c": 1, "d": 4}
common_elements = {}
for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        common_elements[key] = dict1[key]
print(common_elements)

#3. Write a program to calculate the sum of all the values in a dictionary that are
#integers.
dict1 = {"a": 1, "b": 2, "c": 3}
summ = 0
for k, v in dict1.items():
    summ = summ + v
print(summ)

#4. Write a program that takes a sentence as input and counts the frequency of each
#word. Store the word frequencies in a dictionary, where the keys are the words and
#the values are the frequencies.

sentence = "My name is: Sahar and My last name is: Bittman"
dict_names = {}
lst = sentence.split()
for word in lst:
    if word in dict_names:
        dict_names[word] = dict_names[word] + 1
    else:
        dict_names[word] = 1
print(dict_names)


#5. Write a program that takes a dictionary as input and swaps the keys and values.
#The resulting dictionary should have the original values as keys and the original
#keys as values.

dictt = {'sahar': 34, 'tom': 24}
new_dictt = {}
for k, v in dictt.items():
    new_dictt[v] = k
print(new_dictt)


#6. Write a program that takes a dictionary as input and returns a list of keys sorted in
#descending order based on their associated values.
os = {'ubuntu': 2, 'centos': 1, 'redhat' :3}
dict_os = sorted(os.keys(), reverse=True)
print(dict_os)

#7. Write a program that takes a list of dictionaries as input and sorts them based on a
#specific key in each dictionary.
lst_dict = [{'sahar': 34, 'adam': 24}, {'סהר': 0, 'תום': 1}]
lst_dict_sorted_names = sorted(lst_dict[0].items())
print(lst_dict_sorted_names)
