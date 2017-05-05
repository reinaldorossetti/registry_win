import re

#s =   "00-44  48 5555 8361"
s = "0 - 22 1985--324"

"""
004-448-555-583-61 - > 14 number
022-198-53-24 - > 10 number
555-372-654 -> 9 number
"""

result = re.findall(r'\d+', s)
test1 = ''.join(result)
list_numbers = [int(i) for i in test1]
# print(list_numbers)
# print(len(list_numbers))
# print('-'.join(result))

if len(list_numbers)==14:
    print("%s-%s-%s-%s-%s" % (test1[0:3], test1[3:6], test1[6:9], test1[9:12], test1[12:14]))
elif len(list_numbers)==10:
    print("%s-%s-%s-%s" % (test1[0:3], test1[3:6], test1[6:8], test1[8:10]))
elif len(list_numbers)==9:
    print("%s-%s-%s" % (test1[0:3], test1[3:6], test1[6:9]))

