import binascii

# this was written to reverse the endianness of a 32 bit file

input_hex_file = open("challengefile", "rb")

input_bytes = binascii.hexlify(input_hex_file.read())

output_bytes = b''

for i in range(0, len(input_bytes), 8):
    output_bytes += input_bytes[i+6: i+8] + input_bytes[i+4: i+6] + input_bytes[i+2: i+4] + input_bytes[i: i+2]

print(output_bytes)

output_hex_file = open("challengefile.jpg", "wb")

output_hex_file.write(binascii.unhexlify(output_bytes))
output_hex_file.close()