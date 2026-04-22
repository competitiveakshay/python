nums = [1,5,7,4,3,6,9,2,8]
n = len(nums)

def selection_sort(nums):
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]

def bubble_sort(nums):
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

def insertion_sort(nums):
    for i in range(1,n):
        key = nums[i]
        j = i - 1

        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            j -= 1
        
        nums[j+1] = key

insertion_sort(nums)
print(nums)