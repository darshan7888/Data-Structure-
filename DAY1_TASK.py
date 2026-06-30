# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:10:44 2026

@author: Dell
"""
# (1) Student Atteendence Array 


# ---

# **Roll No. 1 → Index 0**

# **Roll No. 2 → Index 1**

# ...

# **Roll No. 30 → Index 29**

# Since every student has a fixed slot (index), the teacher can directly go to any student's attendance without checking the previous records.

# **For example:**

# If the teacher wants to mark the attendance of Roll No. 16, they can directly access **Index 15**.

# There is no need to search from Roll No. 1 to Roll No. 16.

# This is called **direct (random) access**, which is the most important feature of an array.

# ---

attendance = ["Absent"] * 30

while True:
    print("\n1. Mark Attendance")
    print("2. Check Attendance")
    print("3. Display All")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter Roll No (1-30): "))
        if 1 <= roll <= 30:
            attendance[roll - 1] = "Present"
            print("Attendance Marked")
        else:
            print("Invalid Roll Number")

    elif choice == 2:
        roll = int(input("Enter Roll No: "))
        if 1 <= roll <= 30:
            print("Attendance:", attendance[roll - 1])
        else:
            print("Invalid Roll Number")

    elif choice == 3:
        for i in range(30):
            print(f"Roll No {i+1}: {attendance[i]}")

    elif choice == 4:
        break

    else:
        print("Invalid Choice")
        
#
# C2) The Undo Machine

# You're building a lightweight text editor for a startup. Every time a user types a character, it gets recorded. When they press **Ctrl+Z (Undo)**, the last action must be reversed. The editor must support:

# * `type(char)` — records a character
# * `undo()` — removes the last typed character
# * `getText()` — returns the current text

# ---
stack = []

while True:
    print("\n1. Type Character")
    print("2. Undo")
    print("3. Get Text")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        ch = input("Enter Character: ")
        stack.append(ch)

    elif choice == 2:
        if stack:
            print("Removed:", stack.pop())
        else:
            print("Nothing to Undo")

    elif choice == 3:
        print("Current Text:", "".join(stack))

    elif choice == 4:
        break

    else:
        print("Invalid Choice")
        


# C3) The Smart Printer Queue (Priority Queue)

# An office printer handles jobs in order, **BUT** jobs marked **URGENT** must be printed before normal jobs. Design a system using **two queues** — one for urgent, one for normal — and always drain urgent first.

# ---

# If you want, I can also provide the **Python solutions** for **C2 (Undo Machine using Stack)** and **C3 (Smart Printer Queue using Queue)**.

urgent = []
normal = []

while True:
    print("\n1. Add Urgent Job")
    print("2. Add Normal Job")
    print("3. Print Job")
    print("4. Display Queue")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        job = input("Enter Urgent Job: ")
        urgent.append(job)

    elif choice == 2:
        job = input("Enter Normal Job: ")
        normal.append(job)

    elif choice == 3:
        if urgent:
            print("Printing Urgent:", urgent.pop(0))
        elif normal:
            print("Printing Normal:", normal.pop(0))
        else:
            print("No Jobs to Print")

    elif choice == 4:
        print("Urgent Queue:", urgent)
        print("Normal Queue:", normal)

    elif choice == 5:
        break

    else:
        print("Invalid Choice")