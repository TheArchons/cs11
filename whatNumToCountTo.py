num = 0
maxNum = int(input("What number would you like to count to? "))

while num <= maxNum:
    print(num)
    num += 1

#Alternatively:
maxNum = int(input("What number would you like to count to? "))
nums = range(0, maxNum+1)
for num in nums:
    print(num)