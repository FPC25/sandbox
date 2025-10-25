def merge_sort(nums):
    if len(nums) < 2:
        return nums

    median = len(nums) // 2

    sorted_left_part = merge_sort(nums[:median])
    sorted_right_part = merge_sort(nums[median:])

    return merge(sorted_left_part, sorted_right_part)
        
def merge(first, second):
    final = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i+=1
        else:
            final.append(second[j])
            j+=1
            

    final.extend(first[i:])
    final.extend(second[j:])
    
    return final

def main():
    test = [2, 4, 5, 1, 15, 10]
    test2 = [4, 6, 1, -1, 0, 100]
    
    sorted_test = merge_sort(test)
    sorted_test2 = merge_sort(test2)
    
    print(sorted_test)
    
    print(sorted_test2)

if __name__ == "__main__":
    main()