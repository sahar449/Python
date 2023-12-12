import random, string
a = string.ascii_letters + string.digits + string.punctuation
length = int(input('Length password\n'))
password = ''
for _ in range(length):
    password = password + random.choice(a)
print(password)
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
