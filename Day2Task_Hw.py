# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:26:16 2026

@author: ex409_56
"""

#C1) your younger sibling is packing books into a bag. They don't plan — they just look at two adjacent books, and if the heavier one is on top of the lighter one, they swap. They keep repeating this until no more swaps happen. Heaviest books slowly "bubble up" to the bottom.

booklist=[10,5,20,25,40,52]
print(booklist)
n=len(booklist)
cn=0
for i in range(n-1):
    cn=cn+1
    for j in range(n-1):
        if booklist[j] > booklist[j+1]:
            bk=booklist[j]
            booklist[j]=booklist[j+1]
            booklist[j+1]=bk
            
print(cn)
print(booklist)


#C2) The Scholarship Ranker
#A college must give scholarships to the top 3 scorers. 
# The coordinator scans the entire marksheet, finds the highest scorer,
#  moves them to position 1. Then scans the remaining students for the next highest,
#  and so on. Each pass = one full scan to select the minimum/maximum.

marks = [78, 95, 67, 88, 99, 91, 85]

n = len(marks)

for i in range(3):  
    maxInd = i
    for j in range(i + 1, n):
        if marks[j] > marks[maxInd]:
            maxInd = j
    marks[i], marks[maxInd] = marks[maxInd], marks[i]

print("Top 3 Ranker", marks[:3])

# c3) The Lost Student (Attendance Register)
# Professor Sharma enters class and gets a call from the HOD — 
# "Is Riya Desai present today?" The attendance register is not sorted.
#  Names are written in the order students sat down.

StdAttend=[
    "Darshan Gohil",
    "Riya Desai",
    "Manish Yadav",
    "Raj Gohil",
    "Yadav Kartik"
    ]

student="Riya Desai"

fund=False
for name in StdAttend:
    if name == student:
        found=True
        break
if found:
    print(f"{student}  present today")
else:
    print(f"{student} absent today")
 
# c4) The Dictionary Hunt
# You're in a library with a physical English dictionary. 
# You need to find the word "Ephemeral". 
# You don't start from page 1 — you open the middle, see "M",
# know E comes before M, so you take the left half and repeat.


words =['Ritchi','Global','Ephemeral','Networking','Aritificial']
target = "Ephemeral"

low = 0
high = len(words) - 1

while low <= high:
    mid = (low + high) // 2

    if words[mid] == target:
        print("Word found pos ", mid + 1)
        break
    elif target < words[mid]:
        high = mid - 1
    else:
        low = mid + 1

if low > high:
    print("Word no found")
    
    
    
    
    
    # HOME WORK DAY 2 
    
# h1) - The Spam Detector (Search in Stream) – linear search
# A cybersecurity intern at a startup is building a basic spam filter. 
# Incoming emails are checked against a blacklist of known spam sender IDs. 
# The blacklist has no order.

blacklist = [101, 205, 309, 412, 550]

sndId = int(input("Enter Sender ID: "))

found = False

for id in blacklist:
    if id == sndId:
        found = True
        break

if found:
    print("Spam Sender found!")
else:
    print("Sender safe.")

# h2) The E-Commerce Price Filter (First occurrence ≥ target)
# You're on Flipkart. You filter products: "Show me laptops priced ₹50,000 or above." 
# Products are sorted by price. Flipkart must find the first product ≥ ₹50,000 — 
# classic binary search variant called lower bound.


prices = [25000, 30000, 40000, 50000, 55000, 60000, 70000]

target = 50000

low = 0
high = len(prices) - 1
ans = -1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= target:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

if ans != -1:
    print("First laptop price >= ₹50000 is ₹", prices[ans])
else:
    print("No laptop found.")

# h3) Merge Sort — The IRCTC Waitlist Merger
# # IRCTC has two separately sorted waitlists — 
# one from its mobile app, one from railway counters. 
# To produce a final unified waitlist, they don't re-sort from scratch. They merge both sorted lists in one pass —'
# ' compare the front of each list, pick the smaller token, advance. This is exactly merge sort's merge step.


lst1 = [1, 3, 5, 7]
lst2 = [2, 4, 6, 8]

merged = []

i = 0
j = 0

while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        merged.append(lst1[i])
        i += 1
    else:
        merged.append(lst2[j])
        j += 1


while i < len(lst1):
    merged.append(lst1[i])
    i += 1

while j < len(lst2):
    merged.append(lst2[j])
    j += 1

print("Merged Waitlist:", merged)