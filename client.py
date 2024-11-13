import struct
import sys 

param1 = sys.argv[1]
param2 = sys.argv[2]
param3 = sys.argv[3]
param4 = sys.argv[4]

# *** pack ((b'elso', 57, True)) ........FAILED:
#      b'first\x00\x00\x009\x00\x00\x00\x01'

# *** pack ((60.5, False, b'X')) ........OK

# *** pack ((48, b'masodik', 67.9)) ........FAILED:
#      b'0\x00\x00\x00masodik\x00\xcd\xcc\x87B'

# *** pack ((b'Z', 79, b'harmadik')) ........FAILED:
#      b'Z\x00\x00\x00O\x00\x00\x00harmadik'


str1 = struct.Struct('I f ?')
with open(param1, 'rb') as f1:
    param1_data = f1.read(str1.size)
    unpacked_data1 = str1.unpack(param1_data)
    print(unpacked_data1)

str2 = struct.Struct('? c 9s')
with open(param2, 'rb') as f2:
    param2_data = f2.read(str2.size)
    unpacked_data2 = str2.unpack(param2_data)
    print(unpacked_data2)

str3 = struct.Struct('9s f I')
with open(param3, 'rb') as f3:
    param3_data = f3.read(str3.size)
    unpacked_data3 = str3.unpack(param3_data)
    print(unpacked_data3)

str4 = struct.Struct('? I c')
with open(param4, 'rb') as f4: 
    param4_data = f4.read(str4.size)  
    unpacked_data4 = str4.unpack(param4_data)
    print(unpacked_data4)

# - "first" (17), 57, True
# - 60.5, False, 'X'
# - 48, "second" (15), 67.9
# - 'Z', 79, "third" (18)


packer1 = struct.Struct('17s i ?')
values1 = (b'elso', 57, True)
print(packer1.pack(*values1))

packer2 = struct.Struct('f ? c')
values2 = (60.5, False, b'X')
print(packer2.pack(*values2))

packer3 = struct.Struct('i 15s f')  
values3 = (48, b'masodik', 67.9)
print(packer3.pack(*values3))

packer4 = struct.Struct('c i 18s') 
values4 = (b'Z', 79, b'harmadik')
print(packer4.pack(*values4))



