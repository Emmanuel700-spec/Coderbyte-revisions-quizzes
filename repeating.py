# def duplicates(nums):
#     number = set()
#     for num in nums:
#         if num in number:
#             return True  
#         number.add(num)
#     return False  

def duplicates(nums):
    return len(nums) != len(set(nums))

array1 = [1, 2, 3, 3, 4, 5, 2]
print(duplicates(array1))  

array2 = [1, 2, 3, 4, 5]
print(duplicates(array2))
