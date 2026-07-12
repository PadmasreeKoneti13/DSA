nums = [1,43,34,67,34,87,98,92]
largest = float('-infinity')
second_largest = float('-infinity')
for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num < largest:
        second_largest = num
print(second_largest)
