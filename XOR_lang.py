RANGE_1 = [i for i in range(35, 48)]
RANGE_2 = [i for i in range(58, 65)]
RANGE_3 = [i for i in range(93, 97)]
RANGE_4 = [i for i in range(123, 127)]
AVAILABLE_CHARCODES = [33] + RANGE_1 + RANGE_2 + [91] + RANGE_3 + RANGE_4

# ' " \ are forbidden chars because they will mess up our payload

d_outp = input('Desired output: ')

input_1 = ''
input_2 = ''

for char in d_outp:
    for i in AVAILABLE_CHARCODES:
        j = ord(char) ^ i
        if j in AVAILABLE_CHARCODES:
            input_1 += chr(i)
            input_2 += chr(j)
            break

if len(input_1) != len(d_outp):
    print("Unachievable string...")
    exit()  

else:
    print(f'Here is your translated code: "{input_1}" ^ "{input_2}"')


# print out the available chars
# b = ''
# for num in AVAILABLE_CHARCODES:
#     b += chr(num)
# print(b)