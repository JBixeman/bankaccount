# def myfunc(*args):
#      mylist=[num for num in args if num % 2 == 0]     print(mylist)

# def lesser_of_two_evens(a,b):
# #     if a % 2 == 0 and b % 2 ==0:
# #         print(min(a,b))
# #     else:
# #         print(max(a,b))
# #
# # lesser_of_two_evens()
# # #
# #
# # def animal_crackers(str):
# #      mystr = str.lower().split()
# #      print(mystr[0][0] == mystr[1][0])
# #
# #
# # animal_crackers('Lovely lady')


# def makes_twenty(a,b):
#     if a+b==20 or a == 20 or b==20:
#         print(True)
#     else:
#         print(False)
# makes_twenty(9,11)

# def old_macdonald(str):
#     first_half = name[:3]
#     second_half = name[3:]
#     return first_half + second_half.capitalize()
# old_macdonald('macdonald')
#
#
# def master_yoda(str):
#     mystr = str.split()
#     mystr.reverse()
#     print(' '.join(mystr))
#
#
# master_yoda('we are ready')
#
# def almost_there(n):
#     return (abs(100-n) <= 10) or (abs(200 - n) <= 10)
# almost_there(210)
#
#
# def has_33(nums):
#     for i in range(0,len(nums)-1):
#         if nums[i] == 3 and nums[i+1] == 3:
#             return True
#     return False
# has_33()
#
#
# def paper_doll()
#     result = ''
#     for char in text:
#         result += char*3
#     return result
#
# paper_doll()
#
# def blackjack(a,b,c):
#
#     if sum([a,b,c]) <= 21:
#         return sum([a,b,c])
#     elif 11 in [a,b,c] and sum([a,b,c]) - 10 <= 21:
#         return sum([a,b,c])
#     else:
#         return 'Bust'
#
# blackjack(10,10,11)
#
#
# def summer_of_69(arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total
#
#
#
#
# # challenging Problem solutions
#
# def spy_game():
#     code = [0,0,7,'x']
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)
#     return len(code) == 1

# def count_primes(num):
#
#     if num < 2:
#         print(0)
#     primes = [2]
#     x = 3
#     while x <= num:
#         for y in range(3,x,2):
#             if x%y == 0:
#                 x += 2
#                 break
#         else:
#             primes.append(x)
#             x += 2
#     print(primes)
# count_primes(5000)


# def vol(rad):
#     v = (4/3)*3.1416*(rad**3)
#     print(v)
#
# vol()
# def ran_check(num,low,high):
#     if num in range(low,high):
#         print('ye')
#     else:
#         print('naw')
# ran_check(4,2,5)
#
# def ran_bool(num,low,high):
#     print(num in range(low,high))
#
# ran_bool(-3,1,15)

# def up_low(str):
#     upper = [l for l in str if l.isupper()]
#     lower = [l for l in str if l.islower()]
#     count1 = 0
#     count2 = 0
#     for l in upper:
#         count1 += 1
#     for l in lower:
#         count2 += 1
#     message = (
#         f"No. of Upper case characters : {count1}"
#         '\n'
#         f"No. of Lower case characters : {count2}"
#     )
#
#     print(message)
# up_low()
#
#
# def unique_list(list):
#     the_list=[]
#     for x in list:
#         if x not in the_list:
#             the_list.append(x)
#     print(the_list)
# unique_list([1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6])


# def multiply(numbers):
#     result = 1
#     for num in numbers:
#         result = result * num
#     print(result)
#
# multiply([3,2,7])
#



# def toJadenCase(string):
# #     print(" ".join([w[0:].capitalize() for w in string.split()]))
# #
# #
# #
# # toJadenCase("People Tell Me To Smile I Tell Them The Lack Of Emotion In My Face Doesn'T Mean I'M Unhappy")

# def friend(x):
# #     the_list = [name for name in x if len(name) == 4]
# #     print(the_list)
# # friend(["Ryan", "Kieran", "Mark", ])

# def nb_year(p0,percent,aug,p):


# def nb_year(p0, percent, aug, p):
#     begin = p0
#     n = 0
#     while p > begin:
#         increase = begin * (percent / 100) + aug
#         begin += increase
#         n+=1
#         print(n)
#
#
# nb_year(1500,5,100,5000)

# def Descending_Order(num):
#     x = list(map(int, str(num)))
#     x.sort(reverse = True)
#     print(int(''.join(str(y) for y in x)))
#
# Descending_Order(15)

#def binary_array_to_number(arr):
#     x = arr[::-1]
#     final_count = 0
#     for index, binary in enumerate(x, start=0):
#         final_count += binary*(2**index)
#     print(final_count)
# binary_array_to_number([1,1,1,1])

# def dig_pow(n,p):
#     a  = [int(x) for x in list(str(n))]
#     total = 0
#     power = p
#     for y in a:
#         total += y**power
#         power += 1
#     if total % n == 0:
#         print(total/n)
#     else:
#         print(-1)

# def unicode_test(value):
#     import unicodedata as ud
#     name = ud.name(value)
#     value2 = ud.lookup(name)
#     print('value="%s", name="%s", value2="%s"' % (value,name,value2))
#
#
# unicode_test('\u0000')
import re


# def binary(a,b):
#     print("{0:b}".format(a + b))
#
#
# binary(210000000000,910000000000000)

# def high_and_low(numbers):
#     nums = [int(x) for x in numbers if x != ' ']
#
#     print(nums)
#
# high_and_low("1 2 3 4 5")
#
# import re
# def high_and_low(numbers):
#     nums = re.sub(r"\s+", "", numbers)
#     print(int(nums))
# high_and_low("-1 2 -3")


import re
# def high_and_low(numbers):
#
#     nums = [int(x) for x in numbers.split() if x != ' ']
#
#
#     print(nums)
#
# high_and_low("-1 2 -3 -5 -5 -20 -984")

# def accum(s):
#     x = []
#     factor = 1
#
#     for letter in s:
#         x.append(factor * letter)
#         factor+=1
#         y = '-'.join(x).title()
#     return y
#
# accum("abcde")

# def alphabet_position(text):
#     alphabet = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     print(" ".join(str(x) for x in [alphabet.index(l) for l in text.lower() if l in alphabet]))
#
#
#
# alphabet_position("The sunset sets at twelve o' clock.")


# def sort_array(x):
#     x.sort()
#
#     print(x)
#
#
#
# sort_array([3,4,6,8,9,12,15])


# import string
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     if ''.join(sorted(str1.lower())) == alphabet:
#         print(True)
#     else:
#         print(False)
#
#
#
#
# ispangram('acbefdhgijklmnopqrstuuvwxyy')


#


def foo ( n ):
  times_table = [ n * i for i in range (1 , 11) ]
  for num in times_table :
    print ( num )
foo(5)





