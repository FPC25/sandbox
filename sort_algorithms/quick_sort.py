def quick_sort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[high] = pivot, nums[i+1]

    return i+1

def main():
    tests = ([2, 4, 5, 1, 15, 10], [4, 6, 1, -1, 0, 100])
    
    for test in tests:
        arg = (test, 0, len(test) - 1)

        quick_sort(*arg)
    
        print(test[0])

if __name__ == "__main__":
    main()