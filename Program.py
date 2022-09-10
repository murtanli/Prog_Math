i = 0
num3 = 0

while True:
    i += 1
    num = int(input())
    if i == 1:
        num2 = num - 1
    if num > num2:
        num2 = num
        num3 = num + num3
        print(num3)