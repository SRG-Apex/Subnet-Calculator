import math
from os import system,name

IP = input("Enter IP: ")

IP_Array = IP.split(".")
if 224 > int(IP_Array[0]) >= 192:
    CLASS = "C"
elif 127 < int(IP_Array[0]):
    CLASS = "B"
else: CLASS="A"


S = int(input("Enter Subnets (Enter 0 if N/A): "))
H = int(input("Enter Number of Usable Hosts (Enter 0 if N/A): "))

ClassTable = {
    "C" : 3,
    "B" : 2,
    "A" : 1
}
def nCalc(CLASS, S, H):
    print(f"{S}\n{H}")
    if not S==0:
        n = math.ceil(math.log2(S)) + 8*ClassTable[CLASS]
    elif H:
        n = 32-(math.ceil(math.log2(H)))
    return n 

n = nCalc(CLASS, S, H)
H = 2**(32 - n)
S = 2**(n - 8*ClassTable[CLASS])

activeOctet = math.ceil(n/8)
if CLASS == "A":
    subnet3 = 0
    if activeOctet == 4:
        subnet3 = 255
        subnet2 = 255
        subnet1 = 0
        print(n)
        for i in range(n-24):
            print(i)
            subnet1 += (2**(7-i))
            print(subnet1)
    elif activeOctet == 3:
        subnet3 = 255
        subnet2 = 0
        for i in range(n-16):
            subnet2 += (2**(7-i))
        subnet1 = 0 
    else: 
        subnet3 = 0
        for i in range(n-8):
            subnet3 += (2**(7-i))
        subnet2 = 0
        subnet1 = 0
        

if CLASS == "B":
    subnet3 = 255
    print(activeOctet)
    if activeOctet == 4:
        subnet2 = 255
        subnet1 = 0
        print(n)
        for i in range(n-24):
            print(i)
            subnet1 += (2**(7-i))
            print(subnet1)
    else: 
        subnet2 = 0
        for i in range(n-16):
            subnet2 += (2**(7-i))
        subnet1 = 0 
if CLASS == "C":
    subnet3 = 255
    subnet2 = 255
    subnet1 = 0
    for i in range(n-24):
        subnet1 += (2**(7-i))

subnetmask = f"255.{subnet3}.{subnet2}.{subnet1}"
system('cls' if name == 'nt' else 'clear')
print("--- Network Statistics: ---\n")
print(f"Class: {CLASS}")
print(f"Number of Subnets (S): {S}")
print(f"Total Host (H) {H}")
print(f"Number of Usable Hosts: {H-2}")
print(f"Internal N: {n}")
print(f"Bits Borrowed (N): {n-(8*ClassTable[CLASS])}")
print(f"Subnet Mask: {subnetmask}")

# if input("See Ranges? (y/N):") == "y":
#     print("Range(s):")
#     hostsPer = 2**(8-n%8)
#     for subnet in range(S):
#         if activeOctet == 4:
#             suffix = subnet*H
#             print(f"{IP_Array[0]}.{IP_Array[1]}.{IP_Array[2]}.{suffix} to {IP_Array[0]}.{IP_Array[1]}.{IP_Array[2]}.{suffix+(H-1)}") 

#         if activeOctet == 3:
#             suffix = subnet*H
#             print(f"{IP_Array[0]}.{IP_Array[1]}.{IP_Array[2]}.{suffix} to {IP_Array[0]}.{IP_Array[1]}.{IP_Array[2]}.{suffix+(H-1)}") 

#         print(f"")
#         print (f"")

def suffixCalc(subnet: int, hosts: int) -> tuple[int, int, int]:
    suffix = subnet*hosts
    suffix2 = suffix//256
    suffix3 = suffix2//256 
    suffix2 -= suffix3*256
    suffix -= suffix3*256*256 + suffix2*256
    return suffix3, suffix2, suffix

if input("See Ranges? (y/N):") == "y":
    print("Range(s):")
    file = open("out.txt", "wt")
    for subnet in range(S):
        suffix3initial, suffix2initial, suffixinitial = suffixCalc(subnet, H)
        suffix3final, suffix2final, suffixfinal = suffixCalc(subnet+1, H)
        if suffix2final == 0:
            suffix3final -= 1 
        suffix2final -= 1
        
        if suffix2final < 0:
            suffix2final = 255
        suffixfinal -= 1
        if suffixfinal < 0:
            suffixfinal = 255
        
        out = f"Subnet: #{subnet+1} \n{IP_Array[0]}.{suffix3initial}.{suffix2initial}.{suffixinitial} to {IP_Array[0]}.{suffix3final}.{suffix2final}.{suffixfinal}\n"     
        file.write(out)
        print(out)
    file.close()    
