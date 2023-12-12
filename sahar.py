### genearate random password ###
import random, string
a = string.ascii_letters + string.digits + string.punctuation
length = int(input('Length password\n'))
password = ''
for _ in range(length):
    password = password + random.choice(a)
print(password)

### blood donation ###
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

### take numbers from string and calc them ###
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


new_dict = {"sahar": 80, "omer": 90}
for key,value in new_dict.items():
    maxi = max(new_dict.values())
print(f"The max vaule is:{maxi, type(maxi)}")


#1. Write a program that takes a list of words as input and counts the frequency of each
#word. Store the word frequencies in a dictionary.

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print(word_freq)


#2. Write a program to find the common elements between two dictionaries and store
#them in a new dictionary.
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
dictt = {}
for word in words:
    if word not in dictt:
        dictt[word] = 1
print(dictt)

#3. Write a program to calculate the sum of all the values in a dictionary that are
#integers.

dictt = {'sahar': 1, 'tom': 2}
summ = 0
for key, value in dictt.items():
    summ = summ + value
print(summ)
