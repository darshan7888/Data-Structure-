# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:22:15 2026

@author: Dell
"""

# H1) Amazon Fulfillment Centre

# An Amazon fulfillment centre has a conveyor belt with exactly 8 slots numbered 0–7. Each slot holds one product. The warehouse manager needs to:

# Check what's at a slot
# Find a product
# Update a slot
# Check if the belt is full

# The conveyor belt has fixed 8 slots.

belt = ["Empty"] * 8

while True:
    print("\n1. Update Slot")
    print("2. Check Slot")
    print("3. Find Product")
    print("4. Check Belt Full")
    print("5. Display Belt")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        slot = int(input("Enter slot (0-7): "))
        if 0 <= slot < 8:
            product = input("Enter product name: ")
            belt[slot] = product
        else:
            print("Invalid slot!")

    elif choice == 2:
        slot = int(input("Enter slot (0-7): "))
        if 0 <= slot < 8:
            print("Product:", belt[slot])
        else:
            print("Invalid slot!")

    elif choice == 3:
        product = input("Enter product to find: ")
        if product in belt:
            print("Found at slot", belt.index(product))
        else:
            print("Product not found!")

    elif choice == 4:
        if "Empty" in belt:
            print("Belt is NOT Full")
        else:
            print("Belt is Full")

    elif choice == 5:
        for i in range(8):
            print(f"Slot {i}: {belt[i]}")

    elif choice == 6:
        break

    else:
        print("Invalid choice!")
        
# H2) Toll Plaza Simulation (Circular Queue)

# A toll plaza has a fixed capacity of 5 vehicles. If full, new vehicles must wait.

# Implement a Circular Queue to simulate this, since it reuses empty slots without wasting memory.

MAX = 5
queue = [None] * MAX
front = -1
rear = -1

while True:
    print("\n1. Enqueue Vehicle")
    print("2. Dequeue Vehicle")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        vehicle = input("Enter vehicle number: ")

        if (rear + 1) % MAX == front:
            print("Queue is Full")

        else:
            if front == -1:
                front = rear = 0
            else:
                rear = (rear + 1) % MAX

            queue[rear] = vehicle
            print("Vehicle Added")

    elif choice == 2:
        if front == -1:
            print("Queue is Empty")

        else:
            print("Vehicle Left:", queue[front])

            if front == rear:
                front = rear = -1
            else:
                front = (front + 1) % MAX

    elif choice == 3:
        if front == -1:
            print("Queue is Empty")

        else:
            i = front
            while True:
                print(queue[i], end=" ")
                if i == rear:
                    break
                i = (i + 1) % MAX
            print()

    elif choice == 4:
        break

    else:
        print("Invalid Choice")

# H3) The GPS Navigation System (Backtracking)

# You're building a GPS app like Google Maps for a hiking trail. The hiker moves through checkpoints. If they take a wrong turn, they hit "Go Back" to return to the previous checkpoint. But once they go back, they can also "Go Forward" if they change their mind again — just like a browser's back/forward buttons.

# Operations:
# visit(place) — move to a new place
# back() — go to previous place
# forward() — go forward if available


back_stack = []
forward_stack = []
current = "Home"

while True:
    print("\n1. Visit Place")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Current Location")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        place = input("Enter place: ")
        back_stack.append(current)
        current = place
        forward_stack.clear()

    elif choice == 2:
        if back_stack:
            forward_stack.append(current)
            current = back_stack.pop()
        else:
            print("No previous location")

    elif choice == 3:
        if forward_stack:
            back_stack.append(current)
            current = forward_stack.pop()
        else:
            print("No forward location")

    elif choice == 4:
        print("Current Location:", current)

    elif choice == 5:
        break

    else:
        print("Invalid choice")