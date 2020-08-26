print(["Even" if int(input("Enter a number: "))%2==0  else "Odd" for i in range(1) ][0])
print([i for i in map(lambda a:a%2==0,[int(input("Enter a number: ")) for i in range(1)])][0])
print([i for i in map(lambda a:"Even" if a%2==0 else "Odd",[int(input("Enter a number: ")) for j in range(1)])][0])