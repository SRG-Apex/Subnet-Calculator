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

if CLASS == "C":
    if S:
        S = int(S)
        n = math.ceil(math.log2(S))
        S = 2**n
        H = 2**(8-n)
        print(n)
    elif H:
        H = int(H)+2
        n = 8-(math.ceil(math.log2(H)))
        S = 2**n
        H = 2**(8-n)
    subnetsum = 0
    for i in range(n):
        subnetsum += (2**(7-i))

    input()
elif CLASS == "B":
    pass
elif CLASS == "A":
    pass
else:
    pass
subnetmask = f"255.255.255.{subnetsum}"
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