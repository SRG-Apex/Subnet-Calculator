import math
from os import system,name
CLASS = input("Enter Class: ").upper()
IP = input("Enter IP: ")

IP_Array = IP.split(".")
if 224 > int(IP_Array[0]) >= 192:
    CLASS = "C"

IP = IP_Array[0] + "." + IP_Array[1] + "." + IP_Array[2] + "."

S = input("Enter Subnets (Leave Blank if N/A): ")
H = input("Enter Number of Usable Hosts (Leave Blank if N/A): ")

ClassTable = {
    "C" : 3,
    "B" : 2,
    "A" : 1
}
def nCalc(CLASS, S, H):
    if S:
        n = math.ceil(math.log2(S)) + 8*ClassTable[CLASS]
    elif H:
        n = 32-(math.ceil(math.log2(H))) + 8*ClassTable[CLASS]
    return n 

n = nCalc(CLASS, S, H)
H = 2**(32 - n - 8*ClassTable[CLASS])
S = 2**(n - 8*ClassTable[CLASS])

activeOctet = math.ceil(n/4)

if CLASS == "B":
    subnet3 = 255
    if activeOctet == 4:
        subnet2 = 255
        subnet1 = 0
        for i in range(n):
            subnet1 += (2**(7-i))
    else: 
        subnet2 = 0
        for i in range(n-16):
            subnet2 += (2**(7-i))
        subnet1 = 0 
if CLASS == "C":
    subnet3 = 255
    subnet2 = 255
    subnet1 = 0
    for i in range(n):
        subnet1 += (2**(7-i))

subnetmask = f"255.{subnet3}.{subnet2}.{subnet1}"
system('cls' if name == 'nt' else 'clear')
print("--- Network Statistics: ---\n")

print(f"Number of Subnets (S): {S}")
print(f"Total Host (H) {H}")
print(f"Number of Usable Hosts: {H-2}")
print(f"Bits Borrowed (N): {n}")
print(f"Subnet Mask: {subnetmask}")

if input("See Ranges? (y/N):") == "y":
    print("Range(s):")
    for subnet in range(S):
        suffix = subnet*H
        print(IP + str(suffix) + "-" + IP + str(suffix+H-1))