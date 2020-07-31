massive = []
for i in range(int(input())):
    massive.append(int(input()))
for i in massive:
    if i % 7 == 0:
        print(i ** 2)