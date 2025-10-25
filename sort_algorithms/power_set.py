def power_set(input):
    all_subsets = [[]]

    for element in input:
        new_subsets = []
        for set in all_subsets:
            set = set + [element]
            new_subsets.append(set)
        all_subsets.extend(new_subsets)

    return all_subsets

def main():
    
    test = [1, 2, 3]
    print(power_set(test))
    
if __name__ == "__main__":
    main()